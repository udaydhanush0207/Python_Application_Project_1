todos = []

while True:  #using while loop
    user_action = input("Type add or show or exit: ")  # giving user input
    user_action = user_action.strip()  # strip() is used for removing trailing spaces

    match user_action:  #match - case
        case "add":
            todo = input("Enter a todo:")
            todos.append(
                todo.title())                                  #used for add input values to the todos list and title is used for capital letters of every word
        case "show" | "display":                                 #using a bitwise  OR operator
            for item in todos:                                     #using for loop
                print(item.title())                                 #making every word capital
        case "exit":                                               #breaking the while loop under match case
            break
        case whatever:                                              #using a whatever
            print("Unknown command")

print("bye")
