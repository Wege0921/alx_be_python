# daily_reminder.py proj num 4 

# Prompt user for input


task = input("Enter your task: ").strip().lower()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the task based on priority and time sensitivity
print("Reminder:", end=" ")
match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"'{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a high priority task. Consider completing it promptly.")
    case 'medium':
        if time_bound == 'yes':
            print(f"'{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a medium priority task. Plan to complete it soon.")
    case 'low':
        if time_bound == 'yes':
            print(f"'{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level entered. Please choose high, medium, or low.")

