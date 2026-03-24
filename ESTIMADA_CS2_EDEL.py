#Mini-Dataset Project: Weekly Test Scores of 3 subjects for 3 students

import numpy as np

#Creating a 2D array
scores_2d = np.array([
    [85, 90, 88], #Alex
    [78, 82, 80], #Bea
    [92, 89, 94], #Carl
])

subjects = ["Math", "English", "Science"]
students = ["Alex", "Bea", "Carl"]

#Function Definitions
def print_data ():
    print (f"\n-------Student Scores-------")
    print (f"Alex - ", scores_2d [0, :])
    print (f"Bea - ", scores_2d [1, :])
    print (f"Carl - ", scores_2d [2, :]) 

def select_data (): 
    print ("\n--------------Select a Student----------------")
    choice = int(input(" Please enter the number of the student [0] Alex [1] Bea [2] Carl: "))
    choices = [0, 1, 2]
    if choice not in choices:
        print ("Invalid, try again.")
    elif choice in choices:
        if choice == 0:
            print ("Alex  : ", scores_2d [0])
        elif choice == 1: 
            print ("Bea  : ", scores_2d [1])
        elif choice== 2:
            print ("Carl : ", scores_2d [2])
        else:
            print ("Invalid, try again.")
    else:
        print ("Invalid input, enter a number.")

def update_data():
    print("\nSelect a student to update:")
    for i in range(len(students)):
        print(f"[{i}] {students[i]}")
    s = int(input("Enter number: "))

    print("Subjects: [0] Math  [1] Science  [2] English")
    subj = int(input("Enter subject number: "))
    new_score = int(input("Enter new score: "))

def summarize_data ():
    print ("\n------------------Data Summary-------------------")

    max_score = np.max (scores_2d, axis=0)
    min_score = np.min (scores_2d, axis=0)
    avg_score = np.mean (scores_2d, axis=0)
    
    for i in range (len(students)):
        print (f"{students[i]} - Highest Score: {max_score[i]} | Lowest Score: {min_score[i]} | Average Score: {avg_score[i]}")
        print ("<---------------------------------------------------------->")

    
#--------MAIN MENU---------
while True:
    print ("\n***WEEKLY SCORES***\n")
    print ("[1] Display All Students")
    print ("[2] Select a Student")
    print ("[3] Update Scores")
    print ("[4] Summarize Scores")
    print ("[5] Exit\n")
    choice = input("Enter choice: ")
    if choice == '1':
        print_data ()
    elif choice == '2':
        select_data ()
    elif choice == '3':
        update_data ()
    elif choice == '4':
        summarize_data ()
    elif choice == '5':
        print ("\nGoodbye!")
        break
    else:
        print ("Invalid, try again.")

#Reflection Questions
# a) Why did you choose this dataset?
    # I chose this dataset because temperature data is commonly collected and helps track weather patterns. This dataset
    # made it easy to manipulate temperatures across different cities over a week. It allows efficient access, updates to
    # specific cities and days, and data summarization. Additionally, it provides clean codes that make the dataset suitable for
    # temperature monitoring system.
# b) How does a 2D array help organize and work with this kind of data?
    # Using a 2D array allows organization, each row for a city and each column for a day. It makes accessing, updating, and
    # summarizing the data easy. With this, users can quickly analyze and compare daily temperatures between cities.
