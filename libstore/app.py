from packages.requestHelper import RequestHelper
from packages.store import Store
from packages.exceptions.appExceptions import BadNameException, WrongOperationException
try:
    store_name = input('Enter store name: ')
    if store_name:
        book_store = Store(store_name)
        request_helper = RequestHelper(book_store)
        while True:
            print()
            print('Select operations:',
                  '1 - Create new book',
                  '2 - Update existed book',
                  '3 - Delete existed book',
                  '4 - Save data to json',
                  '5 - Get request',
                  '6 - Post request',
                  '7 - Put request',
                  '8 - Delete request',
                  '9 - Exit',
                  sep='\n', end='\n\n')
            user_select = input('Please, enter operation code: ')
            if user_select == '1':
                book_store.add_book()
            if user_select == '2':
                book_store.update_book()
            elif user_select == '3':
                book_store.remove_book()
            elif user_select == '4':
                book_store.save_json()
            elif user_select == '5':
                print(request_helper.get())
            elif user_select == '6':
                request_helper.post()
            elif user_select == '7':
                request_helper.put()
            elif user_select == '8':
                request_helper.delete()
            elif user_select == '9':
                print('See you next time')
                break
            else:
                if not user_select:
                    raise WrongOperationException('Wrong operation code')
    else:
        raise BadNameException('Bad name')
except WrongOperationException as WOE:
    print(WOE.args[0])
except BadNameException as BNE:
    print(BNE.args[0])
except:
    print('Totally madness going on')
