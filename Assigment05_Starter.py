# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# K. Sinkevitch,8/9/20,Added code to complete Assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# Declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
objFile = None
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strTask = "" # Task value input from user
strPriority = "" # Priority value from user


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try: # Try to perform the indented code
    # Read file into a list of dictionaries
    objFile = open(strFile, "r") # Open file
    for row in objFile: # Loop through rows in the file
        lstRow = row.split(",")  # Returns a list of the row values
        dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()} # Set row in dictionary to the row values
        lstTable.append(dicRow) # Add dictionary row to the list
    objFile.close() # Close file
except: # Handle any errors that result from trying to run the indented code above
    print(" Unable to read file, please check that file exists and is in the correct folder")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input(" Which option would you like to perform? [1 to 5] - "))
    print()  # Adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Task | Priority") # Print a header
        for dicRow in lstTable: # For each row in list
            print(dicRow.get('Task'), " | ", dicRow.get('Priority')) # Print the dictionary values
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input(" Enter a new task: ") # Prompt user for new task description
        strPriority = input(" Enter the task's priority: ") # Prompt user for priority
        lstTable.append({"Task": strTask, "Priority": strPriority}) # Append to the list
        print(" ", strTask, "has been added to list")
        continue
    # Step 5 - Remove an item (row) from the list/table
    elif (strChoice.strip() == '3'):
        boolItemFound = False
        strTask = input(" Enter task to remove from list: ") # Prompt user for input
        for row in lstTable: # For every row in the list
            if row["Task"].lower() == strTask.lower(): # Check the value of the key Task to see if it matches user input
                lstTable.remove(row) # Remove row from the list
                print(" ", strTask, "removed from list")
                boolItemFound = True
            elif (not boolItemFound):
                print("Task not found")
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        try:
            objFile = open(strFile, "w") # Open file
            for row in lstTable: # for each row (dictionary) in list, write to file
                objFile.write(str(row["Task"]) + "," + str(row["Priority"])+ "\n")
            objFile.close() # Close file
            print(" Your data has been saved!")
        except:
            print(" Sorry, not able to save your data")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print(" Exiting program, have a nice day!")
        break  # Exit the program
