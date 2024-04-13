class Person:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
    def introduce(self):
        print(f"My name is  {self.name} I am a {self.gender} and I am {self.age} years old")

        
person1=Person("Emmaculate",21,"female")
person1.introduce()
