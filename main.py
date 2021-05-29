from RF_ID import read_card
import RPi.GPIO as GPIO 
from pirc522 import RFID
import time
from Database_manager import DataBase

def make_border(message):
    print('='*120)
    message_usr = message.center(116," ")
    message_usr = '||'+ message_usr +'||'
    print(message_usr)
    print('='*120)

def get_data(priv):
    
    name = input("New Users name: \n")
    last_name = input("New Users lastname: \n")
    email = input("New Users email: \n")
    Database.add_user(name,last_name,email,priv)
    print('User Created')

def enter_using_id():
    id_user = int(input('Enter yout ID:\n'))
    user_info = Database.get_one_user_by_id(id_user)
    print('Hello ', user_info[1])


def enter_using_card():
    card_id_read = int(read_card())
    user_info = Database.get_one_user_by_card(card_id_read)
    print('Hello ', user_info[0])
    type_op = input('A: Add money to the account \nD: Discount money\n')
    type_op = type_op.capitalize()
    if type_op == 'A':
        money = float(input('The money you want to add:\n'))
        money_t = float(user_info[3])
        money_t = money_t + money
        Database.add_transaction(card_id_read,money)
        Database.update_card_credit(card_id_read,money_t)
    elif type_op == 'D':
        money = float(input('The money you want to discount:\n'))
        money_t = float(user_info[3])
        money_t = money_t - money
        if money_t < 0:
            print('Rejected')
        else:
            Database.add_transaction(card_id_read,money)
            Database.update_card_credit(card_id_read,money_t)
    else:
        print('Error')


def add_card_to_user():
    card_id_read = int(read_card())
    user_id = int(input('Enter the users ID\n'))
    initial_credit = float(input('Enter the initial credit\n'))
    Database.add_card(card_id_read,initial_credit,user_id)


def show_all_info():
    make_border('Enter your ID:\n')
    id_enter = input(' ')
    user_selected = Database.get_one_user_by_id(id_enter)
    if user_selected[4] == 'ADMIN':
        info_show = int(input('Select the info you want to display:\n1:All Users\n2:All Cards\n3:All Transactions\n'))
        if info_show == 1:
            Database.get_all_users()
        elif info_show == 2:
            Database.get_all_cards()
        elif info_show == 3:
            Database.get_all_transactions()
        else:
            print('Wrong selection')
    else:
        print('ERROR')
    
    


if '__main__' == __name__:
    Database = DataBase()
    make_border('W E L C O M E   T O   T H E   R E G I S T R A T I O N   S Y S T E M')
    while True:
        print('='*120)
        print('1:Validate user \n2:Add User\n3:Add Card to a user\n4:Show all info')
        x = int(input('What would you like to do?\n'))
        if x == 1:
            print('Validate using:\n1)Card\n2)ID')
            option = int(input(''))
            if  option == 1:
                enter_using_card()
                
            elif option == 2:
                enter_using_id()
            else:
                print('ERROR')

        elif x == 2:
            make_border('Enter your ID:\n')
            id_enter = input(' ')
            user_selected = Database.get_one_user_by_id(id_enter)
            print(user_selected[4])
            if user_selected[4] == 'ADMIN':
                print('W E L C O M E   A D M I N')
                validation = input('Do you want to create a SuperUser?\ny : yes\nother option : no\n').capitalize()
                if validation == 'y':
                    get_data('ADMIN')
                else:
                    get_data('USER')
            else:
                print('You are not ADMIN')
                
        elif x == 3:
            add_card_to_user()
        elif x == 4:
            show_all_info()

        else:
            print('ERROR')
