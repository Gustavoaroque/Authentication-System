import mariadb
import sys


class DataBase:
    def __init__(self):
        self.conn = mariadb.connect(
            user="gustavoaroque",
            password="Gustavoarr0309",
            host="localhost",
            port=3306,
            database="test_py" )
        self.cur = self.conn.cursor()
        print("CONEXION ESTABLECIDA")
        
    def get_all_users(self):
        
        try:    
            self.cur.execute("SELECT * FROM Users")
            users = self.cur.fetchall()
            for user in users:
                print('ID: '+str(user[0])+'\n'+'Name: '+ user[1])
                
        except Exception as e:
            raise
        
    def get_one_user_by_id(self,id):
        try:    
            self.cur.execute("SELECT * FROM Users WHERE user_id = {}".format(id))
            user = self.cur.fetchone()
            #print('ID: '+str(user[0])+'\n'+'Name: '+ user[1])
            return user
        except Exception as e:
            raise
        
    def get_one_user_by_card(self,card_id):
        try:
            self.cur.execute("SELECT Users.user_name, Cards.card_id, Users.user_id FROM Cards JOIN Users ON Cards.user_id=Users.user_id WHERE Cards.card_id= {}".format(card_id))
            user = self.cur.fetchone()
            return user
        except Exception as e:
            raise
            
    def get_user_id(self,name,last_name,email):
        try:    
            self.cur.execute("SELECT user_id FROM Users WHERE user_name = ? AND user_lastname=? AND user_email=?",(name,last_name,email))
            user = self.cur.fetchone()
            print('ID: '+str(user))
            return user
        except Exception as e:
            raise
        
    def update_user_name(self,id,name):
        try:
            self.cur.execute("UPDATE Users set user_name=? WHERE user_id = ?",(name,id))
            print('Actualizado correctamente')
        except Exception as e:
            raise
        
    def add_user(self,name,lastname,email,privilege):
        try:
            self.cur.execute("INSERT INTO Users (user_name,user_lastname,user_email,user_privilege) VALUES (?,?,?,?)",(name,lastname,email,privilege))
            print('Created')
        except Exception as e:
            raise
        self.conn.commit() 
        print(f"Last Inserted ID: {self.cur.lastrowid}")
        
        
        
    def add_card(self, card_id, credit, user_id):
        try:
            self.cur.execute("INSERT INTO Cards (card_id, credit, user_id) VALUES (?,?,?)",(card_id, credit, user_id))
            #print('Creado Correctamente')
        except Exception as e:
            raise
        self.conn.commit() 
        print(f"Last Inserted ID: {self.cur.lastrowid}")
        
data = DataBase()
#data.get_all_users()
#print('-'*25)
#data.update_user_name(1,"Marcelo")
#print('-'*25)
#data.get_one_user(1)
#print('-'*25)
