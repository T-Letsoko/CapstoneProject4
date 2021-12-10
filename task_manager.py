import datetime
import os.path
"""
This program will help to create and manage tasks assigned to each member of
the team. The user will be able to register users, add task, view tasks and
exit the program.
"""


# This function is called when the user selects ‘r’ to register a new user.
# It will take a username as a parameter
def reg_user(user_name):
    # Check if 'username' is equal to admin then allow
    # username to register new users. Or tell the user
    # is not authorised to register new users.
    if user_name == "admin":
        # While response == y ask user to register another user until user
        # enters n(no)
        response = "y"
        while response == "y":
            flag1 = 0
            print("\nRegister a new user")

            # Request username from the user
            # Call the 'check_username_exists()' function and pass
            # new_username as an argument
            new_username = input("Enter a new username: ")

            # Since check_username_exists function returns a boolean value
            # We use the function as conditional statement for the 'while' loop
            # If the function returns 'True' display error message and request
            # another username
            while check_username_exists(new_username):
                new_username = input("Enter a new username: ")

            # Request a new password from the user
            new_password = input("Enter a new password: ")

            # Request a user to confirm password until it matches 1st password
            while flag1 == 0:
                # Request user to confirm password
                confirm_pass = input("Confirm new password: ")

                # Check if new password matches the confirmed one
                if new_password == confirm_pass:
                    flag1 = 1
                else:
                    print("\nError!\nPasswords do not match!\n")

            # Open and write into 'user.txt' file
            with open("user.txt", "a") as file1:
                file1.writelines(f"\n{new_username}, {new_password}")
                print("\nUser registered successful.")

            # Ask a user to register another user
            response = input("Do you want to register another user? "
                             "(n - no, y - yes): ").lower()
    else:
        print("\nWarning\nYou are not authorised to register new users.")


# The function is called when a user selects ‘a’ to add a new task.
def add_task():
    user_response = "y"

    # This while loop will run until user enters a letter 'n' for no,
    # to stop entering new tasks
    while user_response == "y":
        print("\nAdd a new task")

        # Open and write/append new info to tasks.txt
        with open("tasks.txt", "a") as input_file:
            # Request user to enter task details
            task_username = input("Enter username of the "
                                  "person to assign task to: ")
            task_name = input("Enter task name: ")
            task_description = input("Enter task description: ")
            assigned_date = datetime.date.today().strftime("%d %b %Y")
            due_date = input("Enter task due date E.g (1 Nov 2021): ")
            task_completed = "No"

            # Write the captured data to tasks.txt file
            input_file.writelines(
                f"\n{task_username}, {task_name}, "
                f"{task_description}, {assigned_date}, "
                f"{due_date}, {task_completed}")

        # Ask the user if they want to enter another task
        user_response = input("\nDo you want to enter another task? "
                              "(Yes - y or No - n): ").lower().strip()

        # Check if user entered a correct response (y or n).
        # If 'user_response' is not found in 'responses' list then
        # go through the 'while' loop and ask user to enter correct
        # letter(y or n)
        responses = ["y", "n"]
        if user_response not in responses:
            while True:
                # This while will run until user enter a correct letter: y or n
                user_response = input("\nPlease enter a 'y' or 'n'."
                                      "\nDo you want to enter another task?"
                                      "(Yes - y or No - n): ").lower()

                # Check if user has enter a correct response(y/n)
                # and then break this while loop
                if user_response in responses:
                    break


# This function is called when users type ‘va’ to view all
# the tasks listed in ‘tasks.txt’.
def view_all():
    print("Tasks List")
    # Open the 'tasks.txt' file
    with open("tasks.txt", "r") as input_file:
        # Assign all the file content to 'input_tasks' variable
        # and create list from each line of string
        input_tasks = input_file.read().strip().split("\n")

        # Iterate through each line and display task details
        # File opened at the beginning of the 'while' loop
        for user_task in input_tasks:
            task_line = user_task.split(", ")

            # Display all the task for each username
            print(f"Task: \t\t\t\t{task_line[1]}")
            print(f"Assigned to: \t\t{task_line[0]}")
            print(f"Date assigned: \t\t{task_line[3]}")
            print(f"Due date: \t\t\t{task_line[4]}")
            print(f"Task complete?: \t{task_line[5]}")
            print(f"Task description: \n\t{task_line[2]}\n")


# This function is called when users type ‘vm’ to view all
# the tasks that have been assigned to them.
# It will take a username as a parameter
def view_mine(user_name):
    # Open the 'tasks.txt' file
    with open("tasks.txt", "r") as input_file:
        # Assign all the file content to 'tasks' variable and
        # create list from each line of string
        input_tasks = input_file.read().split("\n")

        # This 'place_holder' variable will be a placeholder
        # to check if user has any tasked or not
        place_holder = 0

        # This variable will store and show task number for each task
        task_num = 0

        # The task_num_list will store task numbers belonging to
        # the current logged in user. This will prevent user from
        # editing tasks of other users
        task_num_list = []

        # Iterate through each line and display task details
        for user_task in input_tasks:
            list_details = user_task.split(", ")
            task_num += 1

            # User_name is the one that was used to login
            # Check if 'user_name' is found on each line and print
            # task details of the user
            if user_name in user_task:
                print(f"Task number: \t\t{task_num}")
                print(f"Task: \t\t\t\t{list_details[1]}")
                print(f"Assigned to: \t\t{list_details[0]}")
                print(f"Date assigned: \t\t{list_details[3]}")
                print(f"Due date: \t\t\t{list_details[4]}")
                print(f"Task complete?: \t{list_details[5]}")
                print(f"Task description: \n\t{list_details[2]}\n")

                # Append task_num into the task_num_list
                task_num_list.append(task_num)
                place_holder = 1

        # Check if place is 1 or 0
        # If is == to zero user has no task
        if place_holder == 0:
            print("You don't have any tasks assigned to you.")
        else:
            user_response = "y"
            print("Task Editing")
            while user_response == "y":
                # Request a user to enter a task number
                user_task_num = int(input("\nEnter a task number for a task to be "
                                          "edited or\n-1 to return to the main menu: "))

                # Check if user_task_num is equal to -1 and
                # break the while loop
                if user_task_num == -1:
                    break

                # Check if user_task_num is stored in a list of task
                # numbers belonging to a current logged in user.
                if user_task_num in task_num_list:
                    # Call the edit_task function and pass user_task_no
                    # as an argument until user enters 'n' to stop editing
                    edit_task(user_task_num)
                else:
                    print(f"\nTask number {user_task_num} not found "
                          f"in your task list.")

                # Ask user if they want to edit another task
                user_response = input("\nDo you want to edit another task? "
                                      "(Yes or No)\nEnter y or n: ").lower()


# This function will check if username exist in the user.txt file.
# It takes a new_username as a parameter
# If username exist print an error message and allow user to enter
# a different username
def check_username_exists(new_username):
    # Open user.txt file.
    # Read and assign file content to 'credentials' variable
    # Split each line of login details with a new line to list of details
    with open("user.txt") as file:
        credentials = file.read().split("\n")

        # Iterate through each line of credentials
        # Split each list element with a comma
        for credential in credentials:
            credential = credential.split(", ")

            # Check if a new username on index zero exist in the
            # 'user.txt' file.
            # If true print error message and return True
            if new_username == credential[0]:
                print("\nError!\nUsername already taken, "
                      "enter another username.")
                return True
        # If new username is not in the 'user.txt' file, return False
        return False


# This function will edit a specific task and takes a task number as parameter
# It will be called in 'view_mine' function
def edit_task(task_no):
    # Open and read 'tasks.txt' file
    with open("tasks.txt", "r") as file:
        # Read and split each task line with a new line to
        # create a list of tasks
        tasks_content = file.read().split("\n")

        # Take a task line for the specified index, split that line with ", "
        # assign a list of task details to the 'task_list' variable.
        task_list = tasks_content[task_no-1].split(", ")

        # Ask the user if they want mark or edit a task.
        # Request a user to enter 'm' for mark or 'e' for edit a task.
        user_response = input("\nDo you want to mark or edit the task?"
                              "\nEnter m for mark or e for edit: ").lower()

        # Check if user entered an 'm' to mark or 'e' to edit a task
        if user_response == "m":

            # Check if task is not marked as complete.
            # If true mark it as complete else print message that
            # task is complete and it can't be edited.
            if task_list[5] == "No":
                task_list[5] = "Yes"
                print(f"\nTask number {task_no} has been edited successful.")
            else:
                print(f"\nTask no. {task_no} is already completed and "
                      f"it cannot be edited.")
        elif user_response == "e":

            # Check if task is not marked as complete.
            # If true ask user if they want to edit Username or Due date
            if task_list[5] == "No":
                user_response2 = input("\nDo you want to edit a Username or "
                                       "Due date? \n"
                                       "Enter u for Username or "
                                       "d for Due date: ").lower()

                # If user enter 'u' edit username else if 'd' edit due date
                if user_response2 == "u":
                    new_username = input("\nEdit task Username."
                                         "\nEnter a new username: ")

                    # Edit username on index 0 with entered username
                    task_list[0] = new_username
                elif user_response2 == "d":

                    # Edit due date on index 4 with entered due date
                    new_due_date = input("\nEdit task Due date."
                                         "\nEnter task due date E.g (1 Nov 2021): ")

                    task_list[4] = new_due_date
                print(f"\nTask number {task_no} has been edited successful.")
            else:
                # Print message if task is already completed
                print(f"Task no. {task_no} is already completed and "
                      f"it cannot be edited.")

        # Use ", ".join() to create a single string separated by a comma
        # and assign back to tasks_content[task_no-1]
        tasks_content[task_no-1] = ", ".join(task_list)

    # Write the new content to 'tasks.txt' file
    with open("tasks.txt", "w") as output_file:
        # Iterate through each task line and write each into 'tasks.txt' file
        for my_task in tasks_content:
            output_file.writelines(f"{my_task}\n")


# This function will calculate statistics about the tasks.
# It will calculate total number of:
#   tasks
#   completed tasks
#   uncompleted tasks
#   overdue tasks
#   percentage of incomplete task
#   percentage of overdue task
def task_overview_stats():
    # Open 'tasks.txt' file
    with open('tasks.txt', 'r') as file:

        # 'task_list' variable stores tasks.txt file content
        # split() by a new line to create a list of content
        # strip() any empty lines at begin & end
        task_list = file.read().strip().split("\n")

        # This 'total_num_tasks' variable will store the number of tasks
        total_num_tasks = len(task_list)

        # This 'count_completed_tasks' variable will count completed tasks
        count_completed_tasks = 0

        # This 'count_uncompleted_tasks' variable will count uncompleted tasks
        count_uncompleted_task = 0

        # This 'count_overdue_task' variable will count overdue
        # and uncompleted tasks
        count_overdue_task = 0

        # Get system date/today's date
        system_date = datetime.date.today().strftime("%d %b %Y")

        # Iterate through a list of tasks.
        # spilt(", ") a string of task into list of individual
        # pieces of details
        for task_line in task_list:
            task_line = task_line.split(", ")

            # Check if there is 'Yes' in a list of 'task_line'
            # and increment 'count_completed_tasks' or 'count_uncompleted_task'
            if "Yes" in task_line:
                count_completed_tasks += 1
            else:
                count_uncompleted_task += 1

            # Check for 'No' in 'task_line' list to confirm
            # if task is not completed
            if "No" in task_line:

                # Convert due date and today's date to datetime object
                # for comparison.
                # This will convert dates to this 2021-11-13 format.
                # due date is found on index 4 from
                converted_today = datetime.datetime.strptime(system_date, "%d %b %Y")

                converted_due_date = datetime.datetime.strptime(task_line[4], "%d %b %Y")

                # Check if today's date is greater than or after the due date
                if converted_today > converted_due_date:
                    count_overdue_task += 1

    # Calculate the percentage of tasks that are incomplete.
    # divide number of incomplete tasks by total number of tasks
    # and multiply by 100
    percentage_tasks_incomplete = (count_uncompleted_task / total_num_tasks) * 100

    # Calculate the percentage of overdue tasks.
    # divide number of overdue tasks by total number of tasks
    # and multiply by 100
    percentage_overdue_tasks = (count_overdue_task / total_num_tasks) * 100

    # Write the results to 'task_overview.txt'
    with open("task_overview.txt", "w") as output_file:
        output_file.writelines(
            f"Total number of tasks: {total_num_tasks}\n"
            f"Total number of completed tasks: {count_completed_tasks}\n"
            f"Total number of uncompleted tasks: {count_uncompleted_task}\n"
            f"Total number of overdue tasks: {count_overdue_task}\n"
            f"Percentage for incomplete tasks: {round(percentage_tasks_incomplete)}%\n"
            f"Percentage for overdue tasks: {round(percentage_overdue_tasks)}%"
        )


# This function will calculate statistics about the task assigned to each user.
# It will calculate total number of:
#   Number of tasks
#   Total number of users
#   percentage overdue tasks
#   percentage of incomplete task
#   percentage of overdue task
def user_overview_stats():
    # Open the 'user.txt' file
    with open("user.txt", "r") as file:
        # Read the file, split each line with a new line and assign file
        # content to 'users_list' variable
        users_list = file.read().split("\n")

        # This variable stores the total number of users
        total_num_users = len(users_list)

        # This dictionary variable will store all the user overview data/stats
        data_dict = {}

    with open("tasks.txt", "r") as task_file:
        # Read the file, strip empty lines and split each line with
        # a new line and assign file content to 'tasks_list' variable
        tasks_list = task_file.read().strip().split("\n")

        # This variable stores the total number of tasks
        total_num_tasks = len(tasks_list)

        # Iterate through a list of users and get each user
        for each_user in users_list:

            # Split each user line with a comma and assign the
            # list of credentials to user_details
            user_details = each_user.split(", ")

            # This 'count_tasks_user' variable will increase by 1 to get
            # total number of tasks for each user
            count_tasks_user = 0

            # This 'count_completed_tasks' variable will increase by 1 to get
            # total number of completed tasks for each user
            count_completed_tasks = 0

            # This 'count_uncompleted_tasks' variable will increase by 1 to get
            # total number of uncompleted tasks for each user
            count_uncompleted_tasks = 0

            # This 'count_overdue_task' variable will count overdue
            # and uncompleted tasks
            count_overdue_tasks = 0

            # Get system date representing today's date
            system_date = datetime.date.today().strftime("%d %b %Y")

            # Iterate through 'tasks_lis' list and get each task/line
            for each_task in tasks_list:

                # Split each task line with a comma and assign the
                # list of task details to 'task_details' variable
                task_details = each_task.split(", ")

                # Check if username is in the task list then
                # increment 'count_tasks_user' by 1
                if user_details[0] in task_details:
                    count_tasks_user += 1

                    # Check if task is Yes/Completed then add 1
                    # to 'count_completed_tasks'
                    # else add 1 to 'count_uncompleted_tasks'
                    if "Yes" in task_details:
                        count_completed_tasks += 1
                    elif "No" in task_details:
                        count_uncompleted_tasks += 1

                        # Convert due date and today's date to datetime object
                        # for comparison.
                        # This will convert dates to this 2021-11-13 format.
                        # due date is found on index 4 from
                        converted_system_date = datetime.datetime.strptime(system_date, "%d %b %Y")

                        converted_due_date = datetime.datetime.strptime(task_details[4], "%d %b %Y")

                        # Check if today's date is greater than or
                        # after the due date
                        if converted_system_date > converted_due_date:
                            count_overdue_tasks += 1

            # Calculate percentage of tasks assigned to the user from the
            # total number of tasks.
            # Round off and store the value to the
            # 'percentage_total_tasks' variable.
            percentage_total_tasks = round(count_tasks_user / total_num_tasks * 100)

            # Calculate percentage of completed tasks assigned to the user.
            # Round off and store the value to the
            # 'percentage_completed_tasks' variable.
            percentage_completed_tasks = round(count_completed_tasks / count_tasks_user * 100)

            # Calculate percentage of uncompleted tasks assigned to the user.
            # Round off and store the value to the
            # 'percentage_uncompleted_tasks' variable.
            percentage_uncompleted_tasks = round(count_uncompleted_tasks / count_tasks_user * 100)

            # Calculate percentage of uncompleted and overdue tasks assigned
            # to the user.
            # Round off and store the value to the 'percentage_overdue_tasks'
            # variable.
            percentage_overdue_tasks = round(count_overdue_tasks / count_tasks_user * 100)

            # Add generated stats to the 'data_dic' variable
            # The 'data_dict' dictionary will be a nested dictionary
            # Each username is key and their values are dictionaries with key/value pairs
            # dictionary will be like this:
            #     {
            #       admin: {
            #            "Assigned to": "Admin",
            #            "Total number of task: 2
            #            }
            #      }
            data_dict[user_details[0]] = {
                "Assigned to": user_details[0],
                "Total number of task": count_tasks_user,
                "% for total number of tasks": f"{percentage_total_tasks}%",
                "% for completed tasks": f"{percentage_completed_tasks}%",
                "% for uncompleted tasks": f"{percentage_uncompleted_tasks}%",
                "% for overdue tasks": f"{percentage_overdue_tasks}%"
            }

    # Open 'user_overview.txt' file to write the information
    with open("user_overview.txt", "w") as output_file:

        # Write total number of users and task at the top
        output_file.writelines(
            f"Total number of users: {total_num_users}\n"
            f"Total number of tasks: {total_num_tasks}\n\n"
        )

        # Iterate through the nested dictionary
        # to get key, value pair.
        # The is the username.
        for key in data_dict:

            # Iterate through the dictionary e.g
            # 'admin': {Total number of task": 2} to get values
            for user_key in data_dict[key]:
                output_file.writelines(f"{user_key}: {data_dict[key][user_key]}\n")

            # Write an empty line between user information for readability
            output_file.write("\n")


# This function will read both 'task_overview.txt & user_overview.txt' files
# display their file contents as statistics
def display_statistics():
    
    # Call task_overview_stats & user_overview_stats function
    # to refresh task_overview.txt & user_overview.txt with
    # new information
    task_overview_stats()
    user_overview_stats()

    # Open and read 'task_overview.txt' file content
    with open("task_overview.txt", "r") as file:
        print("TASK OVERVIEW STATS")

        # Print file content
        print(file.read())

    # Open and read 'user_overview.txt' file content
    with open("user_overview.txt", "r") as file2:
        print("\nUSER OVERVIEW STATS")

        # Print file content
        print(file2.read())


# ----Login Section ----

# Open the 'user.txt' file
with open("user.txt", "r") as user_file:
    list_users = user_file.read().split("\n")

    # This variable is used to control the 'while loop' conditional statement
    flag = 0

    while flag == 0:
        # Request username and password from user
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for user in list_users:

            # create a list of credentials for each line [username, password]
            user_details_line = user.split(", ")

            # Check entered username and username at index 0.
            # If true check password.
            # Username and password are correct then stop and assign flag
            # the value of 1 to exit the 'while' loop
            if username == user_details_line[0]:
                if password == user_details_line[1]:
                    flag = 1
                    print("\nLogin successful.")
                    # Included the 'break' keyword so that if username and
                    # password are correct there's no need to check other
                    # credentials, just stop the for loop and move to other
                    # processes
                    break

        # Check if flag == 0 and display error message
        if flag == 0:
            print("\nError!\nYou have entered an incorrect username "
                  "or password.\n")

# ----MENU Section----
# After the user has logged in the user must choose which task/action they want
# to perform
menu_description = '''
Please select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
e - exit
'''

admin_menu = """
Please select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit
"""
# Request menu option from user
while True:
    # Check if 'username' is admin then display a different menu option
    if username == "admin":
        menu_option = input(admin_menu + "\n").lower()
    else:
        menu_option = input(menu_description).lower()

    # Check which menu option has been selected and perform it's designated
    # task
    if menu_option == "r":
        # Call the reg_user function and pass the username used for login
        # as an argument
        reg_user(username)

    elif menu_option == "a":
        # Call the add_task function
        add_task()

    elif menu_option == "va":
        # Call the view_all function
        view_all()

    elif menu_option == "vm":
        # Call view_mine function and pass the username used for login
        # as an argument
        view_mine(username)

    elif menu_option == "gr":
        # Call the 'task_overview_stats' & 'user_overview_stats' functions
        # to generate reports
        task_overview_stats()
        user_overview_stats()
        print("\nReports generated successful.")

    elif menu_option == "ds":
        # Reference to check if file exist:
        # https://stackoverflow.com/questions/82831
        # /how-do-i-check-whether-a-file-exists-without-exceptions

        # Check if 'task_overview.txt & user_overview.txt' files exist or not
        # if not call 'task_overview_stats & user_overview_stats' functions to
        # generate reports

        if not os.path.isfile("task_overview.txt"):
            if not os.path.isfile("user_overview.txt"):
                task_overview_stats()
                user_overview_stats()

        # Call this function to display stats
        display_statistics()
    elif menu_option == "e":
        break
