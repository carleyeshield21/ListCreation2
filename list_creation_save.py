listahan = []
while True:
    user_action = input("Type 'a' to add item to list\n's' to view your list\n'e' to edit your list\n'x' to "
                        "exit and view your list\n'r' to remove item from the list\n").strip().lower()
    match user_action:
        case 'a':
            item = input('Type and entry\n') + '\n'
            listahan.append(item.capitalize())
            text_file = open('file.txt','w')
            text_file.writelines(listahan)
        case 'x':
            print('The items on you list are:')
            for i in listahan:
                print(i.strip())
            exit()
        case 's':
            for entry in listahan:
                print(f'{listahan.index(entry) + 1}. {entry.strip()}')
            print('==============')
        case 'r':
            num_item = int(input('Type the number of the item you want to remove\n'))
            if num_item <= len(listahan):
                listahan.remove(listahan[num_item - 1])
                print(listahan)
            else:
                print('The item you chose does not exist\nPlease try again.\n')
                user_action = input("Type 'a' to add item to list\n's' to view your list\n'e' to edit your list\n'x' to "
                                    "exit and view your list\n'r' to remove item from the list\n").strip().lower()
        case 'e':
            try:
                for entry in listahan:
                    print(f'{listahan.index(entry)+1}. {entry.strip()}')
                to_edit = int(input('Type the number of the item you want to change\n'))
                if to_edit <= len(listahan):
                        edited_item = input('Type the new item\n')
                        listahan[to_edit - 1] = edited_item.capitalize()
                else:
                    print('The item you chose does not exist\nPlease try again.\n')
                    user_action = input("Type 'a' to add item to list\n's' to view your list\n'e' to edit your list\n'x' to "
                                        "exit and view your list\n'r' to remove item from the list\n").strip().lower()
            except IndexError:
                print('The item you chose does not exist\nPlease try again.\n')
                user_action = input("Type 'a' to add item to list\n's' to view your list\n'e' to edit your list\n'x' to "
                                    "exit and view your list\n'r' to remove item from the list\n").strip().lower()