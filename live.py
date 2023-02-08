
class Car:
    """description of a car"""
    def __init__(self, make , model , year):
        self.make = make 
        self.model = model 
        self.year = year 
        self.odometer_reading = 0
    
    def getDescription(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    