todos = []                               # declaring todos as a list

while True:                             #using while loop
    user_action = input("Type add or show or edit or complete or exit: ")     # giving user input
    user_action = user_action.strip()   # strip() is used for removing trailing spaces

    match user_action:                  #match - case
        case "add":
            todo = input("Enter a Todo:")
            todos.append(todo)     #used for add input values to the todos list and title is used for capital letters of every word
        case "show":
            for index, item in enumerate(todos):
                row = f"{index - 1}-{item}"    #using f strings directly by adding and assigning it to the row
                print("Length of the row is :", len(row))   #adding length as well
                print(row.title())      #showing the list of items and capitalising too
        case "edit":                  #editing a list item
            number = int(input("Enter the number of Todo to edit:"))
            number = number - 1
            new_todo = input("Enter your Todo to edit:")    #replacing the required item into the list
            todos[int(number)] = new_todo #converting string with int
            print(new_todo.title())
        case "complete":                         #here when the assigned work is done, it should be deleted
            number = int(input("Enter the number of todo to complete:"))
            number = number - 1
            todos.pop(int(number))              # pop() used for removing list indexing
            print(todos)
        case "exit":                 #breaking the while loop under match case
            break

print("bye")                        # prints for while loop after exit

print("To do added successfully!")

print("Number of todos: ", len(todos))   #checks the length of the todos i.e. the no. of items in the list




