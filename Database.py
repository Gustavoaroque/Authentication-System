import mariadb
import sys




def Search_usr(card):
    conn = mariadb.connect(
        user="gustavoaroque",
        password="Gustavoarr0309",
        host="localhost",
        port=3306,
        database="test_py" )

    cur = conn.cursor()
    cur.execute("SELECT name FROM user_2 WHERE card_id = ?",(card,))
    for name in cur:
        return name

    conn.close()

def Update_credit(card_id, credit):
    conn = mariadb.connect(
        user="gustavoaroque",
        password="Gustavoarr0309",
        host="localhost",
        port=3306,
        database="test_py" )
    cur = conn.cursor()
    try:
        cur.execute("UPDATE user_2 SET credit=? WHERE card_id= ? ",(credit,card_id))
    except mariadb.Error as e:
        print(f"Error: {e}")

    conn.commit()
    print("DONE")
    conn.close()





def Insert_usr( name_usr, last_name,card_id_usr, credit):
    conn = mariadb.connect(
        user="gustavoaroque",
        password="Gustavoarr0309",
        host="localhost",
        port=3306,
        database="test_py" )
    cur = conn.cursor()
    try: 
        cur.execute("INSERT INTO user_2 (name,card_id) VALUES (?,?)",(name_usr,card_id_usr))
    except mariadb.Error as e: 
        print(f"Error: {e}")

    conn.commit() 
    print(f"Last Inserted ID: {cur.lastrowid}")
    conn.close()

if "__main__" == __name__:

    Update_credit(1,999)
