
user_prompt = "Enter your todo item: "

todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)

todos = [todo1, todo2, todo3, "Hello World!"]   

print(todos)

print(type(user_prompt))
      
print(type(todos))

print("Todo added successfully!")

print("Number of todos:", len(todos))
