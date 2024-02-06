#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 09:19:52 2023

@author: kameela
"""

import datetime


# PROBLEM DESCRIPTION
# This program below essentially creates a to-do list. 
# Adding, viewing, and marking items as completed is a breeze using this to-do list code. 
# A timestamp that shows the addition date of each task entry is included. 
# My to-do list is accessible and easily retrieved with time-stamped accuracy 
# thanks to the program's task saving to text file.


# Function to add a task to the list with a timestamp
def add(tasks, new_task):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Append the new task along with its timestamp to the tasks list
    tasks.append({"task": new_task, "time": time})
    print(f"Task '{new_task}' added successfully.")

# Function to mark a task as completed and remove it from the list
def complete(tasks, tasknumber):
    # Check if the tasknumber is within a valid range
    if 0 <= tasknumber < len(tasks):
        # Pop the task at the specified tasknumber from the list
        completed = tasks.pop(tasknumber)
        print(f"Task '{completed['task']}' marked as completed.")
    else:
        print("Invalid task number!!!.")

# Function to view the tasks in the list
def view(tasks):
    # Check if there are no tasks in the list
    if not tasks:
        print("No tasks saved.")
    else:
        # Print the current tasks along with their timestamps
        print("Current Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['task']} ({task['time']})")

# Function to save tasks to a file
def save(tasks, to_dolistfile):
    # Open the specified file in write mode
    with open(to_dolistfile, 'w') as file:
        # Write each task along with its timestamp to the file
        for task in tasks:
            file.write(f"{task['time']} - {task['task']}\n")
    print(f"Tasks have been saved to {to_dolistfile}.")

# Function to load tasks from a file
def load(to_dolistfile):
    tasks = []
    try:
        # Attempt to open the specified file in read mode
        with open(to_dolistfile, 'r') as file:
            # Read each line from the file
            for line in file:
                # this removes the white spaces from a line
                line = line.strip()
                # Split the line into timestamp and task 
                time, task = line.split(" - ", 1)
                # Append the task along with its timestamp to the tasks list
                tasks.append({"task": task.rstrip(")"), "time": time})
    except FileNotFoundError:
        # Ignore if the file is not found
        pass 
    # Return the list of tasks
    return tasks

# Function to display a welcome message
def welcome():
    # Print a welcome message with available options
    print("\nWelcome to Kameela's To-Do List\nWhat would you like to do today?:\n1. Add a Task\n2. Complete a Task\n3. View your Tasks\n4. Save Tasks and Exit")

# Main function to manage the to-do list
def todo_list():
    # Specify the output file for saving tasks
    to_dolistfile = "cps109_a1_output.txt"
    # Load existing tasks from the output file
    tasks = load(to_dolistfile)
    # This block of code basically user inputs the tasks to enter the task they want, update the task, etc.
    while True:
        welcome()
        option = input("Enter option 1 to 4: ")
        
        if option == '1':
            new_task = input("Enter the new task: ")
            add(tasks, new_task)
        elif option == '2':
            view(tasks)
            if tasks:
                tasknumber = int(input("Enter completed task number: ")) - 1
                complete(tasks, tasknumber)
        elif option == '3':
            view(tasks)
        elif option == '4':
            print("Thank you for using to-do list:) Exiting. GoodBye!")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 4.")
        
        # Save the updated tasks to the output file after each operation
        save(tasks, to_dolistfile)

if __name__ == "__main__":
    # Execute the to-do list application
    todo_list()

