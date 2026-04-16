class Phone :
    category = "Electronic"
    #constructor
    def __init__(self, model, battery, camera, better_parentage = 100):
        self.model = model
        self.battery = battery
        self.camera = camera
        self.better_parentage = better_parentage

    #method
    def charge(self, hour):
        if self.battery>0:
           if self.better_parentage==100:
               print("better is full")
        self.better_parentage += hour
    def capture(self, totalPhoto):
        if self.better_parentage<=0:
            print("No Battery")
            return 
        self.better_parentage -= totalPhoto
    ##create object 


apple = Phone("app-17", "1000mah", "12mp")
print(apple.camera)

apple.capture(5)
print(apple.better_parentage)

oppo = Phone("oppo-17", "1000mah", "64mp")
oppo.category = "Super Electronic"
print(oppo.camera)
print(oppo.better_parentage)


# inheritance 
class SmartPhone(Phone):
    def __init__(self, model, battery, camera, better_parentage = 100):
        super().__init__(model, battery, camera, better_parentage)
        self.model = model