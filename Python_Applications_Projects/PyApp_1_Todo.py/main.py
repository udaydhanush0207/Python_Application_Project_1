
user_prompt = "Enter your todo item: "

todos = []

while True:
    todo = input(user_prompt)
    print(todo.capitalize())
    todos.append(todo)
    print(todos)


print("To do added successfully!")

print("Number of todos:", len(todo))




