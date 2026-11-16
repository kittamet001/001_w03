#Subject
#-subjectCode
#-subjectName
#-subjectUnit
class Subject:
    def __init__(self,subjectCode,subjectName,subjectUnit):
        self.subjectCode = subjectCode
        self.subjectName = subjectName
        self.subjectUnit = subjectUnit
    def __str__ (self):
        return f"subject : {self.subjectCode}: {self.subjectName} ({self.subjectUnit}): "