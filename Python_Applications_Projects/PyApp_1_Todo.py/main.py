user_prompt = "Enter your todo item: "

todos = []

while True:
    todo = input(user_prompt)
    todos.append(todo)
    print(todo.title())
    print(todos)

print("To do added successfully!")

print("Number of todos:", len(todo))




