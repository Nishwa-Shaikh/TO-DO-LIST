Add_task=[]
Remove_task=[]
Completed_task=[]

def display_menu():
    print('What you want to do?\n1.Add a task\t2.Remove a task\t3.See completed tasks\t4.Exit ')
    return int(input('Enter your choice number: '))


while True:
    try :
        print()
        user_choice=display_menu()
        if user_choice==1:
            while True:
                print()
                add_task=input('Enter your task,if you want to exit, type "exit": ').capitalize()
                if add_task in Add_task:
                    None
                else:
                    Add_task.append(add_task)
                if add_task=='Exit':
                    Add_task.remove('Exit')
                    print(Add_task)
                    break
        elif user_choice==2:
            while True:
                print()
                print(f'Remaining tasks: {Add_task}')
                remove_task=input('Enter task that you want to remove, if you want to exit, type "exit": ').capitalize()
                if remove_task=='Exit':
                    print(f'Remove tasks: {Remove_task}')
                    print(f'Remaining tasks: {Add_task}')
                    break
                elif remove_task in Add_task:
                    Remove_task.append(remove_task)
                    Add_task.remove(remove_task)
                else:
                    print('No such task exists')
        elif user_choice==3:
            while True:
                print()
                print(f'Remaining tasks: {Add_task}')
                completed_task=input('Enter tasks that you have completed, if you want to exit, type "exit": ').capitalize()
                if completed_task in Add_task:
                    Completed_task.append(completed_task)
                    Add_task.remove(completed_task)
                else:
                    print('No such task exist in list')
                
                if completed_task=='Exit':
                    print(f'Completed tasks: {Completed_task}')
                    print(f'Remaining tasks: {Add_task}')
                    break
        elif user_choice==4:
            print()
            print('Thankyou for using our application')
            break

        else:
            print()
            print('Enter correct value!')

    except:
        print()
        print('You should type an integer!')