class programmers():
    species = "mammals"
    salary_increment = 1.1
    def __init__(self, name, age, gender, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary

    def generate_email(self):
        return self.name + str(self.age) + "@gmail.com"

    def incremented(self):
        return self.salary * self.salary_increment
    
class designers(programmers):
    species = "reptiles"
    salary_increment = 1.05

    def __init__(self, name, age, gender, salary, design_software):
        super().__init__(name, age, gender, salary)
        self.design_software = design_software

        @classmethod
        def species_change(cls, new_species):
            cls.species = new_species
            return f"changed specied to {cls.species}"
        
designer1 = designers("hope",24,"female",10000,"adobe")
designer2 = designers("john",21,"male",200000,"illustrator")

programmer1 = programmers("mike", 20, "male", 2000)
programmer2 = programmers("kanoel", 19, "female", 1000)
programmer3 = programmers("mercy", 23, "female", 2000)
print(programmer1.name)
print(programmer1.generate_email())
print(programmer2.incremented())
print(designer1.design_software)
print(getattr(designer1, "design_software"))
designer1.design_software = "illastrator"
setattr(designer1, "design_software","illastrator")
print(designer1.design_software)
print(designer1.species)
designer1.species_change