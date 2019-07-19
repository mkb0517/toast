# toast
Telescope Observing Automated Scheduling Tool


# Overview: 
Given a list of approved observing programs for a period of time, generate an observing schedule meeting each program's constraints as best as possible.  

# Main Tasks:
Define inputs and outputs.
Define phases and scope of project
Research existing techniques and algorithms for general scheduling problems. 
Define data model and object classes
Define criteria for scoring a schedule
Create test input data
Start coding, see how far we get


# Description:
PIs submit proposals before each semester for each of their observing programs.  Programs can cover one or more nights and request one or more instruments.  Proposals can also provide, based on the moon phase, preferred nights and nights to avoid.  Proposals can also provide info on priority ra/decs targets.

Other considerations come into play, such as holidays, telescope shutdowns, instrument downtime, ???.

Scheduled observing nights can be divided and shared into full, half, and/or quarter portions of the night.
The output from the code should be a list of night observing programs that fill the schedule for each observing night in the date range.  

An nightProgram will consist simply of the following data for each record:
ProgId
Date
StartTime
EndTime
Portion


# Full Project Phases
The number of factors to consider when evaluating each program and where to schedule it is quite large.  So, we will break the complexity up into stages in order that we can create a working prototype quickly and fill in the complexity later on:

Phase 1: Create scaffolding: Basic classes and code to take inputs (program data, date range, etc) and produce simple output schedule with little to no considerations for constraints.
Phase 2: Easy stuff: Add in the non-negotiable constraints (holidays, shutdowns, segment exchange) and important constraints (dates to avoid, unacceptable instrument dates)
Phase 3: Basic Algorithms: Consider program preferences (preferred, acceptable)
Phase 4: Advance Algorithms: Consider scheduling optimizations (instrument runs, minimize instrument reconfigs
Phase 5: Bells and Whistles: Consider special requests, PI particularness
Phase 6: GUI


# TIME LOG:
Jul 17: 1 HOUR


# MISC / NOTES
Ability to pre-lock certain program assignments before builder is run (ie manual intervention)
Meetings/PI conflicts
Holidays
PI particularness
Offline instruments (sometimes defined, sometimes Carolyn picks downtime
Segex defined dates
special requests
date specific requests (should be cadence but they put them in as classical)
minimize instrument reconfigs, schedule runs (nirspao minimize runs, consolidate esi runs)
machine learning?

# Classes
Toast: Main program that builds schedule
Semester


Program: An approved proposal
progId: Unique program code (semester + program name)
type: [classical, cadence, too]
portionOfNight:
numNights
instrumentPrefs
badDates
priorityTargets: array of priority ra/decs
InstrumentPref: A requested instrument and preferred night range data 
instrument
preferredRanges: [array of date ranges that are preferred]
acceptableRanges:
unacceptableRanges:
