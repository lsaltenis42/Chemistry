from enum import Enum
"""
class arrow_info(Enum):
    TYPE = 0
    SIZE = 1
"""
    
class arrow:
    arrow_types = ["--><-","-><--","-><-","->","<-"]

    def __init__(self, arrow_type):
        self.type = arrow_type



