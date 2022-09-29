import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")

import time
import datetime as dt
import numpy as np

import threading
from forward_testing.new_forwardtestscraperclass import ForwardTest

class ForwardTestManager:
    def __init__(self, slots_count, duration, stocks: list[str], *, start_time_bias = 15, end_time_bias = 10):
        """
        Assigns stocks to slots and manages them

        Parameters
        (positional)
        slots_count    : Number of slots to be created in the given duration
        duration       : Denotes how often the predictions are made. Passed as minutes
        stocks         : List of stocks code 
        
        (keyword only)
        start_time_bias: Time in seconds after which the first slot runs. Leading time delay
        end_time_bias  : Time in seconds to wait before starting the next duration after the last slot. Trailing time delay
        """

        self.slots_count = slots_count
        self.duration = duration
        self.stocks = stocks
        self.slots : list[list[str]] = [[] for i in range(self.slots_count)]
        self.start_time_bias = start_time_bias
        self.end_time_bias = end_time_bias

        self.assign_slots()

    def assign_slots(self):
        """
        Assign stocks to certain time slots
        """

        i = 0
        for stock in self.stocks:
            self.slots[i].append(stock)
            i = (i+1) % self.slots_count

    def run_slot(self, slot: list[str]):
        """
        Runs all stocks in a slot as ForwardTest instance with threading
        """

        print(f"run_slot {slot}")
        tests = []
        for stock in slot:
            test = ForwardTest(stock, duration=self.duration)
            tests.append(test)
            test.start()

        for test in tests:
            test.join()

        # So that run_slot doesn't run again at the same timestamp
        time.sleep(1)

    def start(self):
        """
        Decides when to run each slot
        """
        
        timeslot_biases = np.linspace(0 + self.start_time_bias, 60*self.duration - 1 - self.end_time_bias, num=self.slots_count+1, dtype=int)
        timeslot_biases = timeslot_biases[:-1]
        print(timeslot_biases)
        print(self.slots)
        
        while True:
            current_timestamp = int(dt.datetime.now().timestamp())
            start_timestamp = current_timestamp - (current_timestamp % (60*self.duration))
            slot_index = np.where(timeslot_biases + start_timestamp == current_timestamp)
            if len(slot_index[0]) != 0:
                print(timeslot_biases+start_timestamp, current_timestamp)        
                self.run_slot(self.slots[slot_index[0][0]])

# m = ForwardTestManager(1, 5, ["DRREDDY", "ADANIPORTS", "HINDUNILVR", "AXISBANK","INFY", "BAJFINANCE", "TATAMOTORS"])
m = ForwardTestManager(1,5,["BAJFINANCE"])
m.start()
