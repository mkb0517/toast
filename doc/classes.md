
# Toast: Main program that builds schedule    
    semester            str     Semester code  (ie 2019B)
    programs            list    List of approved proposal program objects
    schedule            list    List of scheduled visits (ie The output schedule we will build)
    __constructor(semester)
    getPrograms()
    buildSchedule()


# Schedule
    semester            str     Semester code
    startDateHst        date    Scheduling start date (derive from semester if given)
    endDateHst          date    Scheduling end date (derive from semester if given)
    badHolidayDates     list    List of holiday dates
    badTelescopeDates   list    List of telescope shutdown dates {date, telNum}
    badInstrumentDates  list    List of dates where instruments unavailable {date, instr}
    visits              list

# Night: A night on the schedule
    dateHst         
    startTimeUtc    time
    endTimeUtc      time
    visits          list    List of visits for the night (ie observing period for a program)

# Visit: An observing period for a program on a particular night
    dateHst         
    startTimeUtc    time
    endTimeUtc      time
    portions        int     Portions of night (1,2,3,4)
    telNum          int     Which Keck telescope (1, 2)
    instrument      str     Which instrument

# Program: An approved proposal
    progId          str     Unique program code (semester + program name)
    type            str     [classical, cadence, too]
    instruments     list

# ProgramInstrument: 
    instruments     str     
    portionOfNight  str     :
    numNights       int     
    instrumentPrefs list    List of instrument date range preferences
    badDates        list    List of bad dates
    priorityTargets list    List of priority ra/decs

# InstrumentPref: A requested instrument and preferred night range data 
    instrument          str     
    preferredRanges     list    List of date ranges that are preferred
    acceptableRanges    list    List of date ranges that are acceptable 
    unacceptableRanges  list    List of date ranges that are unacceptable
