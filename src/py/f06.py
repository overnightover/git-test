class Person(object):
    nation = "China"

    # def __new__(cls):
    #     pass

    def __init__(self, age, name, gender):
        self.__gender = gender
        self.age = age
        self.name = name

    def __str__(self):
        return 'name:{0},age:{1}'.format(self.name,self.age)

    def __eq__(self, obj) -> bool:
        p = Person(obj)
        return self.age == p.age & self.name == p.age & self.__gender == p.__gender

    def __len__(self):
        return len(self.name)


A = Person(18, 'Scott', "man")
print(A)
print(dir(A))
print(A.__dict__)
