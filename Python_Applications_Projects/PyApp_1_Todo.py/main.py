todos = []                               # declaring todos as a list

while True:                             #using while loop
    user_action = input("Type add or show or edit or exit: ")     # giving user input
    user_action = user_action.strip()   # strip() is used for removing trailing spaces

    match user_action:                  #match - case
        case "add":
            todo = input("Enter a Todo:")
            todos.append(todo)     #used for add input values to the todos list and title is used for capital letters of every word
        case "show":
            for index, item in enumerate(todos):
                row = f"{index}-{item}"    #using f strings directly by adding and assigning it to the row
                print(row)      #showing the list of items and capitalising too
        case "edit":                  #editing a list item
            number = input("Enter the number of Todo to edit:")
            print(number)
            new_todo = input("Enter your Todo to edit:")    #replacing the required item into the list
            todos[int(number)] = new_todo #converting string with int
            print(new_todo.title())
        case "exit":                 #breaking the while loop under match case
            break

print("bye")                        # prints for while loop after exit

print("To do added successfully!")

print("Number of todos: ", len(todos))   #checks the length of the todos i.e. the no. of items in the list




