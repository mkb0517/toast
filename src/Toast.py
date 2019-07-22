class Toast(object):
  
    def __init__(self, semester, method):
    
        #class vars
        self.semester = semester
        self.method = method
  
        #calc start and end date
        self.startDate, self.endDate = self.getSemesterDates(self.semester)
        
        #do it
        self.programs = loadPrograms(semester)
        self.schedule = createSchedule(self.programs, self.semester, self.method)
  
  
  
  def loadPrograms(semester):
      
      #todo: query proposals database for all approved programs for semester
      query = f"select * from ClassicalInformation_TAC where semester='{semester}' and DelFlag=0"
      data = dbConn.query(query)
      return data
  
  
  def createSchedule(self, semester, method):

      schedule = None
      if   method == 'random': schedule = self.createScheduleRandom(semester)
      elif method == 'XXX'   : self.createScheduleXXX(semester)
      return schedule


  def createScheduleRandom(self, semester):
  
      #todo: 
      
      

  def printSchedule(self, telNum=None):
      '''
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
      print ('Schedule: ')
      for night in self.schedule.nights:
          print(f'==={night.date}===)
          for visit in night.visits:
              print(f"{visit.progId}\t{visit.")
  
  

##-------------------------------------------------------------------------
##  main
##-------------------------------------------------------------------------
if __name__ == "__main__":
    '''
    Run in command line mode
    '''

    # arg parser
    parser = argparse.ArgumentParser(description="Start Keck auto-scheduler.")
    parser.add_argument("semester",   type=str,                      default=None          help="Semester.")
    parser.add_argument("--method",   type=str,    dest="method",    default='random',     help="Algorithm method.")
    args = parser.parse_args()

    #go
    toast = new Toast(semester, method)
    toast.printSchedule()
    
    
