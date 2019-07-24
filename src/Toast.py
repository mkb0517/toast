import json
import argparse
import pandas
import config

class Toast(object):


    def __init__(self, semester, method):
    
        #class vars
        self.semester = semester
        self.method = method
  
        #calc start and end date
        self.startDate, self.endDate = self.getSemesterDates(self.semester)
        
        #do it
        self.programs = self.loadPrograms(semester)
        self.createSchedule(self.programs, self.semester, self.method)
  
    
    def getSemesterDates(self, semester):
        #todo: calc
        return '2019-08-01', '2019-08-03'
        return '2019-08-01', '2020-01-31'


    def loadPrograms(self, semester):

        #todo: generate random data for testing?

        #todo: temp: get test data for now
        with open('../test/test-data-programs.json') as f:
            data = json.load(f)
        return data
        
        #todo: query proposals database for all approved programs for semester
        #todo: query for all the other auxilliary info needed
        query = f"select * from ClassicalInformation_TAC where semester='{semester}' and DelFlag=0"
        data = dbConn.query(query)
        return data
  
  
    def createSchedule(self, programs, semester, method):

        #todo: check if they total proposed hours exceeds semester hours
      
        #todo: execute method
        schedule = None
        if   method == 'random': schedule = self.createScheduleRandom(programs, semester)
        elif method == 'XXX'   : schedule = self.createScheduleXXX(programs, semester)

        #todo: score schedule here

        return schedule


    def createScheduleRandom(self, programs, semester):

        #create new blank schedule
        self.initSchedule()

        #get list of program portions blocks
        blocks = self.getRandomProgramBlocks(programs)

        #for each block, pre-score every date visit candidate
        for block in blocks:
            self.initBlockDates(block)


    def getRandomProgramBlocks(self, programs):

        #For each program, get all program portion objects (ie blocks)
        #todo: for instruments that prefer runs, use 'num' to group together consecutive blocks
        blocks = []
        for program in programs:
            for instr, progInstr in program['instruments'].items():
                for n in range(0, progInstr['nights']):
                    block = {}
                    block['instr']   = instr
                    block['progId']  = program['progId']
                    block['portion'] = progInstr['portion']
                    block['num']     = 1
                    blocks.append(block)

        #todo: psuedo-randomize blocks in groups by order of size from biggest to smallest

        return blocks


    def initSchedule(self):

        #generate list of night dates
        dates = self.createDatesList(self.startDate, self.endDate)

        #create blank schedule for each telescope
        self.schedules = {}
        for key, tel in config.kTelescopes.items():
            self.schedules[key] = {}
            self.schedules[key]["nights"] = []
            for date in dates:
                night = {}
                night['date'] = date
                night['visits'] = []
                self.schedules[key]['nights'].append(night)
      

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
        print ('Method  : ', self.method)
        for schedKey, schedule in self.schedules.items():            
            schedName = config.kTelescopes[schedKey]['name']
            print (f'Schedule for {schedName}:')
            for night in schedule['nights']:
                print(f'==={night.date}===')
                for visit in night['visits']:
                    print(f"{visit.index}\t{visit.portion}\t{visit.progId}")
    
    

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
    toast = Toast(args.semester, args.method)
    toast.printSchedule()
    
    
