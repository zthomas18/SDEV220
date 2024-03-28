#Zach Thomas
#M02 Lab - Case Study: if...else and while
#3-28-2024
# GPA Program that accepts student names and their GPA scores. It will tell them if they qualify for the Dean's List or Honor Roll.


while True: 
    last_name = input("Enter your last name (enter 'ZZZ' to quit): ")
    if last_name == 'ZZZ':
        break
    else:
        first_name = input("Enter your first name: ")
        gpa = float(input("Enter your GPA: "))

        if gpa >= 3.5:
            print(f"Congratulations, {first_name} {last_name} has made it to the Dean's List!")
        elif gpa > 3.25:
            print(f"Congratulations, {first_name} {last_name} has made it to the Honor Roll!")
        else:
            print(f"Sorry, {first_name} {last_name} does not qualify for the Dean's List or Honor Roll!")
        

