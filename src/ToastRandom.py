from Toast import *
from random import randrange, shuffle
import math
import config


class ToastRandom(Toast):

    def __init__(self, semester):

        # Call the parent init
        super().__init__(semester)


    def createSchedule(self):

        #get needed input data
        self.datesList      = self.createDatesList(self.startDate, self.endDate)
        self.programs       = self.getPrograms(self.semester)
        self.telShutdowns   = self.getTelescopeShutdowns(self.semester)
        self.instrShutdowns = self.getInstrumentShutdowns(self.semester)

        #create new blank schedule
        self.initSchedule()

        #get list of program portions blocks
        blocks = self.getRandomProgramBlocks(self.programs)

        #for each block, init slots to try and score each slot
        for block in blocks:
            self.initBlockSlots(block)
            self.scoreBlockSlots(block)
            slot = self.pickRandomBlockSlot(block)
            if slot == None: 
                print (f"No valid slots found for block program {block['progId']}")
                continue
            self.assignToSchedule(block['telNum'], 
                                  slot['date'], 
                                  slot['index'], 
                                  block['portion'], 
                                  block['progId'],
                                  block['instr'])


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
                    block['telNum']  = config.kInstruments[instr]['telNum']
                    block['num']     = 1
                    blocks.append(block)

        #todo: psuedo-randomize blocks in groups by order of size from biggest to smallest
        shuffle(blocks)

        return blocks


    def initBlockSlots(self, block):

        #for each portion in each date, create a little slot object to track its fitness score
        block['slots'] = []
        for date in self.datesList:
            for pIndex in range(0, config.kNumPortions):
                slot = {}
                slot['date']  = date
                slot['index'] = pIndex
                slot['instr'] = block['instr']
                slot['progId'] = block['progId']
                block['slots'].append(slot)


    def scoreBlockSlots(self, block):
        
        #For each slot, score it from 0 to 1 based on several factors
        for slot in block['slots']:
            print (f"scoring slot: {slot}")

            slot['score'] = 1

            #check for block length versus portion available length
            #todo: test
            portionRemain = 1 - (slot['index'] * config.kPortionPerc)
            if (block['portion'] > portionRemain):
                slot['score'] = 0
                # print ("\tTOO LONG")
                continue

            #check for telescope shutdowns
            shutdownDates = self.telShutdowns[block['telNum']]
            if slot['date'] in shutdownDates:
                slot['score'] = 0
                # print ("\tTELESCOPE SHUTDOWN")
                continue

            #check for instrument unavailability
            instrShutdowns = self.instrShutdowns
            if slot['date'] in instrShutdowns:
                slot['score'] = 0
                # print ("\tINSTRUMENT UNAVAILABLE")
                continue

            #check for assigned
            if not self.isSlotAvailable(block['telNum'], slot['date'], slot['index'], block['portion']):
                slot['score'] = 0
                # print ("\tOVERLAP")
                continue

            #todo: check for program dates to avoid
            # prog = self.getProgram(block['progId'])
            # if slot['date'] in prog['datesToAvoid']:
            #     slot['score'] = 0
            #     # print ("\tBAD PROGRAM DATE")
            #     continue


            print (f"\tscore = {slot['score']}")


    def pickRandomBlockSlot(self, block):

        #todo: pick with weighted randomness with weight based on score

        #Filter out scores zero or less and order slots by score
        slots = block['slots']
        slotsFiltered = []
        for slot in slots:
            if slot['score'] > 0: slotsFiltered.append(slot)
        slotsSorted = sorted(slotsFiltered, key=lambda k: k['score'], reverse=True)

        #Check for no valid slots
        if len(slotsSorted) == 0:
            return None

        #
        num = len(slotsSorted)
        max = math.ceil(num/10)
        randIndex = randrange(0, max)
        return slotsSorted[randIndex]






