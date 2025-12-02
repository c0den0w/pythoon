import inquirer

def select_a_choice():
    options = [
        "Create New File",
        "Edit Existing File",
        "Run Diagnostics",
        "Exit Program"
    ]

    questions = [
      inquirer.List(
            'action',                     # The key for the answer in the results dictionary
            message="What action should be performed?",
            choices=options,              # The list of options to display
            default="Create New File"     # Optional: Pre-selects an option
        )
    ]

    answers = inquirer.prompt(questions)

    if answers is None:
        print("\nSelection cancelled.")
        return None

    selected_action = answers['action']
    
    print(f"\n✅ You selected: **{selected_action}**")
    return selected_action

choice = select_a_choice()

if choice == "Exit Program":
    print("Goodbye!")
# name = input("what is your name? ")
# print("Hellow " + name)