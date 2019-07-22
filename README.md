# TOAST
Telescope Observing Automated Scheduling Tool


# Overview: 
Given a list of approved observing program proposals for a period of time, generate an observing schedule meeting each program's constraints as best as possible.  


# Description:
PIs submit proposals before each semester for each of their observing programs.  Programs can request one or more nights using one or more instruments on both of the Keck telescopes.  Proposals can also provide, based on the moon phase, preferred nights and nights to avoid.  Proposals can also provide info on priority targets as RA/DEC.  Scheduled observing nights can be divided and shared into full, half, and/or quarter portions of the night.

Other considerations come into play, such as holidays, telescope shutdowns, instrument downtime, popular scientific conferences, etc.

The output will  be a list of Visits (ie night program portions) that fill the schedule for each observing night in the semester date range.  A Visit will consist simply of the following data for each record:
- ProgId
- Date
- StartTime
- EndTime
- Portions


# Full Project Phases
The number of factors to consider when evaluating each program and where to schedule it is quite large.  So, we will break the complexity up into stages in order that we can create a working prototype quickly and fill in the complexity later on:

- Phase 1: Create scaffolding: Basic classes and code to take inputs (program data, date range, etc) and produce simple output schedule with little to no considerations for constraints.
- Phase 2: Easy stuff: Add in the non-negotiable constraints (holidays, shutdowns, segment exchange) and important constraints (dates to avoid, unacceptable instrument dates)
- Phase 3: Basic Algorithms: Consider program preferences (preferred, acceptable)
- Phase 4: Advance Algorithms: Consider scheduling optimizations (instrument runs, minimize instrument reconfigs
- Phase 5: Bells and Whistles: Consider special requests, PI particularness
- Phase 6: GUI



