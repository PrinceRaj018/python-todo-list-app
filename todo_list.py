tasks = []
while True:
    print("=" * 40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    print("=" * 40)
    choice = int(input("enter your choice: "))
   
   
    if choice == 1:
        print("\nADD YOUR TASK")
        task = input("enter your tasks: ")
        tasks.append(task)
        print("Task Added!")
       
    elif choice == 2:
        print("\nVIEW YOUR TASKS")
        print("Your Tasks", tasks)
       
    elif choice == 3:
        print("\nREMOVE TASK")
        task = input("enter your tasks: ")
        tasks.remove(task)
        print("Task Remove!")
       
    elif choice == 4:
        break
    else:
        print("Invalide Choice!")
