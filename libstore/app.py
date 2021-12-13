from packages.store import Store
from packages.exceptions.appExceptions import BadNameException, WrongOperationException

try:
    store_name = input('Enter store name: ')
    if store_name:
        book_store = Store(store_name)
        while True:
            print()
            print('Select operations:',
                  '1 - Create new book',
                  '2 - Delete existed book',
                  '3 - Save data to json',
                  '4 - Exit',
                  sep='\n', end='\n\n')
            user_select = input('Please, enter operation code: ')
            if user_select == '1':
                book_store.add_book()
            elif user_select == '2':
                book_store.remove_book()
            elif user_select == '3':
                book_store.save_json()
            elif user_select == '4':
                print('See you next time')
                break
            else:
                raise WrongOperationException('Wrong operation code')
    else:
        raise BadNameException('Bad name')
except WrongOperationException as WOE:
    print(WOE.args[0])
except BadNameException as BNE:
    print(BNE.args[0])
except:
    print('Totally madness going on')
