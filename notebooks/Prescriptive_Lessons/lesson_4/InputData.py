import json

class DataMachine:

    def __init__(self, machineId):
        self.MachineId = machineId

    def __str__(self):
        result = "Machine " + str(self.MachineId)

        return result

class DataJob:
    
    def __init__(self, idJob, processingTimes, setupTimes, dueDate, tardinessCost):
        self.JobId = idJob
        self.ProcessingTimes = processingTimes
        self.DueDate = dueDate
        self.SetupTimes = setupTimes
        self.TardCost = tardinessCost
        
    def __str__(self):
        result = f"Job {self.JobId} with {len(self.ProcessingTimes)} Operations:\n"

        for opId, processingTime in enumerate(self.ProcessingTimes):
            result += f"Operation {opId} with Processingtime: {processingTime} \n"

        return result

    def Operations(self):
        return [(opId, processingTime) for opId, processingTime in enumerate(self.ProcessingTimes)]
    

class InputData:

    def __init__(self, path):
        self.Path = path
        self.TotalProcessingTime = None
        self.DataLoad()

    def DataLoad(self):

        with open(self.Path, "r") as inputFile:
            inputData = json.load(inputFile)
        
        self.n = inputData['nJobs']
        self.m = inputData['nMachines']
        
        self.InputJobs = list()
        self.InputMachines = list()

        for job in inputData['Jobs']:
            self.InputJobs.append(DataJob(job['Id'], job['ProcessingTimes'], job["SetupTimes"], job['DueDate'], job['TardCosts']))
        
        for k in range(self.m):
            self.InputMachines.append(DataMachine(k))

        self.TotalProcessingTime = sum(x.ProcessingTimes[i] for x in self.InputJobs for i in range(len(x.Operations())))
