from RF_ID import read_card
import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
from pirc522 import RFID
import time
from insert import Insert_usr, Search_usr, Update_credit

def make_border(message):
    print('='*120)
    message_usr = message.center(116," ")
    message_usr = '||'+ message_usr +'||'
    print(message_usr)
    print('='*120)



if '__main__' == __name__:
    make_border('W E L C O M E   T O   T H E   R E G I S T R A T I O N   S Y S T E M')
    while True:
        print('1: To Validate card')
        print('2: To Add User')
        x = int(input('What would you like to do?     '))
        if x == 1:
            print('Put the card in the sensor')
            c_id = int(read_card())
            user_info = Search_usr(c_id)
            message = 'Welcome ' + user_info[0]
            make_border(message)
            for i in range(10):
                print('.')
            action = int(input('Put the amount of money you want to discount?'))
            Update_credit(c_id,action)
        else:
            name_user = input('Enter the name of the new user:  ')
            last_name_user = input('Last Name:    ')
            credit_user = int(input('Credit:     '))
            c_id = int(read_card())
            Insert_usr(name_user, last_name_user,c_id,credit_user)


