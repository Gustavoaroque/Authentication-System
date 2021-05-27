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
    #Desplegar info

def enter_using_card():
    card_id_read = int(read_card())
    user_info = Database.get_one_user_by_card(card_id_read)
    print('Hello ', user_info[0])


def add_card_to_user():
    card_id_read = int(read_card())
    user_id = int(input('Enter the users ID\n'))
    initial_credit = float(input('Enter the initial credit\n'))
    Database.add_card(card_id_read,initial_credit,user_id)


if '__main__' == __name__:
    Database = DataBase()
    make_border('W E L C O M E   T O   T H E   R E G I S T R A T I O N   S Y S T E M')
    while True:
        print('='*120)
        print('1:Validate user \n2:Add User\n3:Add Card to a user')
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
            #c_id = int(read_card())
            #user_info = Search_usr(c_id)
            #message = 'Welcome ' + user_info[0]
            #make_border(message)
            #for i in range(10):
            #    print('.')
            #action = float(input('Put the amount of money you want to discount?'))
            #Update_credit(c_id,action)
        elif x == 2:
            make_border('Enter your ID:\n')
            id_enter = input(' ')
            user_selected = Database.get_one_user_by_id(id_enter)
            print(user_selected[4])
            if user_selected[4] == 'ADMIN':
                print('W E L C O M E   S I R')
                validation = input('Do you want to create a SuperUser?\ny : yes\nother option : no\n')
                if validation == 'y':
                    get_data('ADMIN')
                else:
                    get_data('USER')
            else:
                print('You are not ADMIN')
            
#            name_user = input('Enter the name of the new user:\n')
#            last_name_user = input('Last Name:\n')
#            credit_user = int(input('Credit:\n'))
#            c_id = int(read_card())
#            Insert_usr(name_user, last_name_user,c_id,credit_user)

        elif x == 3:
            add_card_to_user()
        else:
            print('ERROR')
