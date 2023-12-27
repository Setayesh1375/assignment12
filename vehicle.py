class vehicle:
    def __init__(self) :
       self.speed =...
       self.color =...
       self.model =...
    

    def turn_on(self):
        ...
    def turn_off(self):
        ...

class airplane(vehicle):
    def __init__(self) :
        super().__init__()
        self .capacity = ...
        self.country = ...



    def fly(self):
        ...


class car(vehicle):
    def __init__(self) :
        super().__init__()
        self.number_of_wheels = ...
        self.license_plate =...



jinbo = airplane()                       
pride= car()
pride.license_plate = "123123"
