import sqlite3
conn = sqlite3.connect('dat.sqlite')
class bd():
 def add_user(self,login,password):
    c = conn.cursor()
    c.execute("SELECT name FROM users WHERE name='"+login+"';")
    log = c.fetchone()
    conn.commit()

    if(log is not None):
        c.close()
        conn.commit()

    else:

      c.execute("INSERT INTO users (name,password) VALUES (?,?)", (str(login), str(password)))
      conn.commit()
      c.close()


 def prin_database(self):
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    row=c.fetchone()
    while row is not None:
        print(row)
        row=c.fetchone()
    c.close()
 def clear(self):
    c = conn.cursor()
    c.execute("    DELETE FROM users;")
    conn.commit()


    c.close()
#(add_user('admin','123'))
#(add_user('sasha','sos12'))

# Завершение соединения
