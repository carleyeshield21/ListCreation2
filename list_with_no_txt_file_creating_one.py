# the list for the text file will be created inside the case by first opening the file with readable option to check
# contents of the file
while True:
    user_action = input("Type 'a' to add item to list\n's' to view your list\n'e' to edit your list\n'x' to "
                        "exit and view your list\n'r' to remove item from the list\n").strip().lower()
    try:
        with open('file.txt','r') as text_file:
            match user_action:
                case 'a':
                    item = input('Type an entry\n') + '\n'
                    text_file = open('file.txt','r')
                    listahan = text_file.readlines()
                    listahan.append(item.capitalize())
                    text_file = open('file.txt','w')
                    text_file.writelines(listahan)
                case 'x':
                    text_file = open('file.txt','r')
                    listahan = text_file.readlines()
                    for i in listahan:
                        print(i.strip())
                    exit()
                case 's':
                    text_file = open('file.txt','r')
                    listahan = text_file.readlines()
                    for entry in listahan:
                        print(f'{listahan.index(entry) + 1}. {entry.strip()}')
                    print('==============')
                case 'r':
                    text_file = open('file.txt','r')
                    listahan = text_file.readlines()
                    num_item = int(input('Type the number of the item you want to remove\n'))
                    if num_item <= len(listahan):
                        text_file = open('file.txt','r')
                        listahan.remove(listahan[num_item - 1])
                        text_file = open('file.txt','w')
                        text_file.writelines(listahan)
                        print(listahan)
                    else:
                        print('The item you chose does not exist\nPlease try again.\n')
                        user_action = input("Type 'a' to add item to list\n's' to view your list\n'e' to edit your list\n'x' to "
                                            "exit and view your list\n'r' to remove item from the list\n").strip().lower()
                case 'e':
                    try:
                        text_file = open('file.txt','r')
                        listahan = text_file.readlines()
                        print(listahan)
                        for entry in listahan:
                            print(f'{listahan.index(entry) + 1}. {entry.strip()}')
                        to_edit = int(input('Type the number of the item you want to change\n'))
                        print(to_edit)
                        print(type(to_edit))
                        if to_edit <= len(listahan):
                            edited_item = input('Type the new entry\n') + '\n'
                            text_file = open('file.txt','r')
                            listahan[to_edit - 1] = edited_item.capitalize()
                            text_file = open('file.txt','w')
                            text_file.writelines(listahan)
                        else:
                            print('The item you chose does not exist\nPlease try again.\n')
                            user_action = input("Type 'a' to add item to list\n's' to view your list\n'e' to edit your list\n'x' to "
                                                "exit and view your list\n'r' to remove item from the list\n").strip().lower()
                    except IndexError:
                        print('The item you chose does not exist\nPlease try again.\n')
                        user_action = input("Type 'a' to add item to list\n's' to view your list\n'e' to edit your list\n'x' to "
                                            "exit and view your list\n'r' to remove item from the list\n").strip().lower()
    except FileNotFoundError:
        user_choice = input('A file does not exist yet. Do you want to create one? Type "y" to create a text file. Or any key to exit\n')
        if user_choice == 'y':
            print('A new text file has been created')
            with open('file.txt','w') as text_file:
                print('The text file has been saved')
        else:
            exit()
