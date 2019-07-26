import json
import argparse
import pandas
from random import randrange, shuffle
import config
from ToastRandom import *


class Toast(object):

    def __init__(self, semester):
    
        #input class vars
        self.semester = semester
  
        #calc start and end date
        self.startDate, self.endDate = self.getSemesterDates(self.semester)
        
        #todo: check if they total proposed hours exceeds semester hours

        #do it
        self.schedule = self.createSchedule()
  
    
    #abstract methods that must be implemented by inheriting classes
    def createSchedule(self) : raise NotImplementedError("Abstract method not implemented!")


    def getSemesterDates(self, semester):
        #todo: calc from semester
        # return '2019-08-01', '2019-08-01'
        return '2019-08-01', '2019-08-07'
        return '2019-08-01', '2020-01-31'


    def getPrograms(self, semester):

        #todo: generate random data for testing?

        #todo: temp: get test data for now
        with open('../test/test-data-programs.json') as f:
            data = json.load(f)
        return data
        
        #todo: query proposals database for all approved programs for semester
        #todo: query for all the other auxilliary info needed
        # query = f"select * from ClassicalInformation_TAC where semester='{semester}' and DelFlag=0"
        # data = dbConn.query(query)
        # return data
  

    def getTelescopeShutdowns(self, semester):

        #todo: temp: test data one random shutdown date per telescope
        shutdowns = {}
        for telNum in config.kTelescopes:
            shutdowns[telNum] = []
            index = randrange(0, len(self.datesList))
            randDate = self.datesList[index]
            shutdowns[telNum].append(randDate)
        return shutdowns

        #query for known telescope shutdowns
#        shutdowns = {}
#        for telNum in config.kTelescopes:
#            shutdowns[telNum] = []
#            #todo: query
#        return shutdowns


    def getInstrumentShutdowns(self, semester):

        #todo: temp: test data one random shutdown date per telescope
        shutdowns = {}
        for instr in config.kInstruments:
            shutdowns[instr] = []
            index = randrange(0, len(self.datesList))
            randDate = self.datesList[index]
            shutdowns[instr].append(randDate)
        return shutdowns

        #query for known telescope shutdowns
#        shutdowns = {}
#        for instr in config.kInstruments:
#            shutdowns[instr] = []
#            #todo: query
#        return shutdowns


    def initSchedule(self):

        #create blank schedule for each telescope
        self.schedules = {}
        for key, tel in config.kTelescopes.items():
            self.schedules[key] = {}
            self.schedules[key]["nights"] = {}
            for date in self.datesList:
                night = {}
                night['visits'] = []
                self.schedules[key]['nights'][date] = night
      

    def assignToSchedule(self, telNum, date, index, portion, progId, instr):
        schedule = self.schedules[telNum]
        night = schedule['nights'][date]
        data = {
            'index': index,
            'portion': portion,
            'progId': progId,
            'instr': instr
        }
        night['visits'].append(data)


    def isSlotAvailable(self, telNum, date, index, portion):

        #see if slot requested overlaps any visit assignments
        night = self.schedules[telNum]['nights'][date]
        for visit in night['visits']:
            vStart = visit['index']
            vEnd = vStart + int(visit['portion'] / config.kPortionPerc) - 1
            sStart = index 
            sEnd = sStart + int(portion / config.kPortionPerc) - 1

            if (sStart >= vStart and sStart <= vEnd) or (sEnd >= vStart and sEnd <=vEnd):
                return False

        return True


    def createDatesList(self, startDate, endDate):

        startDate = startDate.replace('-','')
        endDate   = endDate.replace('-','')
        dates = [d.strftime('%Y-%m-%d') for d in pandas.date_range(startDate, endDate)]
        return dates

      
    def scoreSchedule(self, schedule):

        #TODO: finish this psuedocode
        gInstrSwitchesFactor = -1.5
        gVisitPrefFactor = {'P': 10,  'A': 5,  'N': 0,  'X': -20}

        score = 0
        for night in schedule:

            # deduct score based on number instrument switches
            numInstrSwitches = night.getNumInstrSwitches()
            score += numInstrSwitches * gInstrSwitchesFactor

            # for each visit, alter score based on assignment preference [P,A,N,X]
            for visit in night:
                pref = self.getAssignmentPref(visit.date, visit.progId)
                score += gVisitPrefFactor[pref]

            #todo: alter score based on priority RA/DEC list?

            #todo: can a program get a portion of night greater or less than requested?

            #todo: score based on minimal runs for instruments that want runs

            return score



    def printSchedule(self, telNum=None, format='txt'):
        '''
        Print out a schedule in text or html.
        
        Sample output:
          Semester: 2019B
          Method  : Random
          Schedule: 
            2019-08-01  K1  [             N123             ]
            2019-08-01  K2  [         N111         ][ C222 ]
            2019-08-02  K2  [     N111     ][     C222     ]
            2019-08-02  K2  [ N123 ][ C123 ][ U123 ][ K123 ]
        '''        
        print ('Semester: ', self.semester)
        for schedKey, schedule in self.schedules.items():            
            schedName = config.kTelescopes[schedKey]['name']
            print (f'\nSchedule for {schedName}:')
            print (f'--------------------------')

            for date in self.datesList:
                night = schedule['nights'][date]
                print(f"==={date}===")

                if date in self.telShutdowns[schedKey]:
                    print(" *** SHUTDOWN ***")

                visits = night['visits']
                visitsSorted = sorted(visits, key=lambda k: k['index'], reverse=False)
                for visit in visitsSorted:
                    print(f"{visit['index']}\t{visit['portion']}\t{visit['progId']}\t{visit['instr']}")
    
    

##-------------------------------------------------------------------------
##  main
##-------------------------------------------------------------------------
if __name__ == "__main__":
    '''
    Run in command line mode
    '''

    # arg parser
    parser = argparse.ArgumentParser(description="Start Keck auto-scheduler.")
    parser.add_argument("semester",   type=str,                                            help="Semester.")
    parser.add_argument("--method",   type=str,    dest="method",    default='random',     help="Algorithm method.")
    args = parser.parse_args()

    #go
    if   args.method == 'random': toast = ToastRandom(args.semester)
    elif args.method == '???'   : toast = ToastXXX(args.semester)
    else:
        print (f"Unknown method {args.method}")
        sys.exit(0)

    #result
    toast.printSchedule()
    
    
