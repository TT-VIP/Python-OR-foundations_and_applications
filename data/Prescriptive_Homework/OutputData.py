import sys
import csv

from InputData import *

class OutputJob(DataJob):

    def __init__(self, dataJob):
        super().__init__(dataJob.JobId, dataJob.ProcessingTimes, dataJob.MachineSequence)
           
        self.StartTimes = [0]*len(self.ProcessingTimes)
        self.EndTimes = [0]*len(self.ProcessingTimes)

class Solution:
    def __init__(self, jobList, permutation):
        self.OutputJobs = {}
        for jobId, job in enumerate(jobList):
            self.OutputJobs[jobId] = OutputJob(job)
        self.Permutation = permutation
        self.Makespan = -1

    def __str__(self):
        return "The permutation " + str(self.Permutation) + " results in a Makespan of " + str(self.Makespan)

    def SetPermutation(self, permutation):
        self.Permutation = permutation