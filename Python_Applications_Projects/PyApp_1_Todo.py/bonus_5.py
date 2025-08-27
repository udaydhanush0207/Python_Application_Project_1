waiting_list = ["Uday","Dhanush","K V S "]  #to get that mutable nature, we must assign a list to a variable if not list itself wont work with sort()
waiting_list.sort(reverse=True)      #lists are mutable with methods so no need of wait_list = wait_list.sort(), instead we can write directly like this

for i,j in enumerate(waiting_list):
    row = f"{i + 1}.{j.title()}"
    print(row)
