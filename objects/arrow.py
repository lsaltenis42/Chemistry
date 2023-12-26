from enum import Enum

class arrow_info(Enum):
    TYPE = 0
    SIZE = 1

class arrow:
    def __init__(self, arrow_properties, index):
        self.type = arrow_properties[arrow_info.TYPE.value]
        self.length = arrow_properties[arrow_info.SIZE.value]
        self.index = index



