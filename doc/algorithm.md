# Basic plan
- Get program data
- Create list of program portions to schedule, ie 
	[
		{progId:'N123', portion:0.5, num:2}, 
		{progId:'C123', portion:0.5, num:1}
	]
 -- Note: for some instruments, we want to schedule runs, so we add a 'num' so we can try to schedule consecutive nights.  Sometimes we might want to force schedule a run as well.
- Randomize portions array
- For each portion, 
  - Get list of all remaining slots and score each one based on several factors and sort by score.
  - Pick a slot using a weighted randomness based on score
- Score schedule
- Repeat X number of times and take best or repeat until high score converges


# Factors in scoring a schedule
- number of instrument switches
- visit is on preferred/acceptable/neutral/bad date
- visit date and time has priority target visible

