- Get array of visit units (Program + Portion, ie {'N123', 0.5}
- Randomize visits array
- For each programUnit


    def solveSchedule(programs, technique='random'):

      schedule = None
      if   technique == 'random': schedule = solveScheduleRandom(programs)
      elif technique == 'ai'    : schedule = solveScheduleAi(programs)
      return schedule


    def solveScheduleRandom(programs):



    def scoreSchedule(schedule):

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
