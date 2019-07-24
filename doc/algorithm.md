# Basic plan
- Get program data
- Create list of program portions to schedule, ie 
	[
		{progId:'N123', 'instr':'OSIRIS',  portion:0.5, num:2}, 
		{progId:'C123', 'instr':'MOSFIRE', portion:0.5, num:1}
	]
 -- Note: for some instruments, we want to schedule runs, so we add a 'num' so we can try to schedule consecutive nights.  Sometimes we might want to force schedule a run as well.
- Psuedo-Randomize portions array in order with full nights grouped first, then 3/4, 1/2, 1/4.
- For each portion:
  - Get list of all remaining valid dates slots and score each one based on several factors (pref, etc) and sort by score.
  - Pick a slot using a weighted randomness based on score
- Score schedule
- Repeat X number of times and take best or repeat until high score converges

- If there are more requests than space in calendar:
  -- Shorten full nights and 3/4 nights to fit in remaining quarter nights.
  -- Shorten full nights to fit in remaining half nights.

- If there is remaining space in calendar:
  -- Bump up quarter nights to half nights first.
  -- Bump up halfs and 3/4 to fulls.


# Factors in scoring a schedule
- number of instrument switches
- visit is on preferred/acceptable/neutral/bad date
- visit date and time has priority target visible

