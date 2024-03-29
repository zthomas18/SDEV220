#Zach Thomas
#M02 Lab - Case Study: if...else and while
#3-28-2024
# GPA Program that accepts student names and their GPA scores. It will tell them if they qualify for the Dean's List or Honor Roll.

def gpa_awards(): # A function that accepts names and GPA scores. It will let the user know if they qualify for the Dean's List or Honor Roll.
    while True: # While loop that runs until user enters 'ZZZ'.
        last_name = input("Enter your last name (enter 'ZZZ' to quit): ") # Asks user for their last name.
        if last_name == 'ZZZ': # If the user enters 'ZZZ', the while loop ends.
            break
        else: #  Processes names and GPA only if 'ZZZ' is not entered.
            first_name = input("Enter your first name: ") # Asks user for their first name.
            gpa = float(input("Enter your GPA: ")) # Asks user for their GPA.

            if gpa >= 3.5: # If the user's GPA is greater than or equal to 3.5, print that the user has made it to the Dean's List.
                print(f"Congratulations, {first_name} {last_name} has made it to the Dean's List!")
            elif gpa >= 3.25: # If the user's GPA is greater than or equal to 3.25, print that the user has made it to the Honor Roll.
                print(f"Congratulations, {first_name} {last_name} has made it to the Honor Roll!")
            else: # If the user's GPA is less than 3.25, print that the user does not qualify for the Dean's List or Honor Roll.
                print(f"Sorry, {first_name} {last_name} does not qualify for the Dean's List or Honor Roll!")

if __name__ == "__main__": # Initializes the program and runs the function.
    gpa_awards()
        

