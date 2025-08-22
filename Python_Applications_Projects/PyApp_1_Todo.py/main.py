todos = []                               # declaring todos as a list

while True:                             #using while loop
    user_action = input("Type add or show or exit: ")     # giving user input
    user_action = user_action.strip()   # strip() is used for removing trailing spaces

    match user_action:                  #match - case
        case "add":
            todo = input("Enter a todo:")
            todos.append(todo.title())     #used for add input values to the todos list and title is used for capital letters of every word
        case "show":
            for item in todos:       #using for loop
                print(item)
        case "exit":                 #breaking the while loop under match case
            break

print("bye")                        # prints for while loop after exit

print("To do added successfully!")

print("Number of todos:", len(todos))   #checks the length of the todos i.e. the no. of items in the list




