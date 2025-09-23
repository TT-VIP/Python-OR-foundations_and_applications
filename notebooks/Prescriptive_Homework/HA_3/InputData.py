import json

class DataJob:
    
    def __init__(self, idJob, processingTimes, machineSequence):
        self.JobId = idJob
        self.ProcessingTimes = processingTimes
        self.MachineSequence = machineSequence
        
    def __str__(self):
        result = f"Job {self.JobId} with {len(self.ProcessingTimes)} Operations:\n"

        for opId in range(len(self.ProcessingTimes)):
            machId = self.MachineSequence[opId]
            result += f"Operation {opId} on machine {machId} with Processingtime: {self.ProcessingTime(machId)} \n"

        return result
    
    def Operations(self):
        return [(opId, processingTime) for opId, processingTime in enumerate(self.ProcessingTimes)]
    
    def ProcessingTime(self, position):
        return self.ProcessingTimes[position]

class InputData:

    def __init__(self, path):
        self.Path = path
        self.DataLoad()

    def DataLoad(self):

        with open(self.Path, "r") as inputFile:
            inputData = json.load(inputFile)
        
        self.n = inputData['nJobs']
        self.m = inputData['nMachines']
        
        self.InputJobs = list()
        self.InputMachines = list()

        for job in inputData['Jobs']:
            self.InputJobs.append(DataJob(job['Id'], job['ProcessingTimes'], job["MachineSequence"]))