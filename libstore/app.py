from packages.store import Store

store_name = input('Enter store name: ')
if store_name:
    book_store = Store(store_name)
    while True:
        print()
        print('Select operations:', '1 - Create new book',
              '2 - Delete existed book', 'Any simbol - Exit', sep='\n', end='\n\n')
        user_select = input('Please, enter operation code: ')
        if user_select == '1':
            book_store.add_book()
        elif user_select == '2':
            book_store.remove_book()
        else:
            print('See you next time!')
            break
else:
    print('Sorry but you entered bad store name!')
