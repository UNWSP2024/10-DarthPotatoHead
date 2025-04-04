#Program Written By: Ainsley Bellamy
#Date Written: 04/03/2025
#Program Title: Compiled_Code


#I chose to try some of the code from the Programiz video.

class Student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

def main():
    student1 = Student("Harry", 85)
    student2 = Student("Janet", 30)
    student3 = Student("French Fry Flinger the 31st", 100)
    print(f"{student1.check_pass_fail()}\n{student2.check_pass_fail()}\n{student3.check_pass_fail()}")

if __name__ == "__main__":
    main()