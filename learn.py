class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age 
        
    def introduce(self):
        print("Hi my name is "+ self.name+" and I am ",self.age," years old")

p1=person("jake",13)
p2=person("emilly",15)

p1.introduce()
p2.introduce()
        