# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.


# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.

class Employees:
    def __init__(self, name, ID_number, department, job_title):
        self.__name = name
        self.__ID_number = ID_number
        self.__department = department
        self.__job_title = job_title

    def get_attributes(self):
        return self.__name, self.__ID_number, self.__department, self.__job_title

def main():
    susan = Employees("Susan Meyers", "47899", "Accounting", "Vice President")
    mark = Employees("Mark Jones", "39119", "IT", "Programmer")
    joy = Employees("Joy Rogers", "81774", "Manufacturing", "Engineer")
    print(f"{susan.get_attributes()}\n{mark.get_attributes()}\n{joy.get_attributes()}")

if __name__ == "__main__":
    main()
