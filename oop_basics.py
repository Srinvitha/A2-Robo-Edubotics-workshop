class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return sum(self.scores) / len(self.scores)

    def summary(self):
        return f"{self.name}: average {self.average():.1f}"

aditi = Student("Aditi", [82, 91, 76])
rahul = Student("Rahul", [70, 65, 80])

print(aditi.summary())
print(rahul.summary())

students = [aditi, rahul]

for student in students:
    print(student.name, student.average())
