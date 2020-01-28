class Job:
    def __init__(self, position="", salary = 0 , location="Chicago"):
        self.position = position
        self.location = location
        self.salary = salary

        ## Experience Level Attributes
        self.entryLevel = True
        self.midLevel = True
        self.seniorLevel = True


        ## JobType status
        self.fullTime = True 
        self.partTime = True
        self.contract = True
        self.internship = True


    #Modify Experience level Attributes
    def flipEntryLevel(self):
    	self.entryLevel = not self.entryLevel

    def flipMidlevel(self):
    	self.midLevel = not self.midLevel

    def flipSeniorLevel(self):
    	self.seniorLevel = not self.seniorLevel


    #modify JobType Status
    def flipFullTime(self):
    	self.fullTime = not self.fullTime
    
    def flipPartTime(self):
    	self.partTime = not self.partTime
    
    def flipContract(self):
    	self.contract = not self.contract
    
    def flipInternship(self):
    	self.internship = not self.internship



