import sqlite3

class bd():
 def __init__(self,name):
     self.conn = sqlite3.connect(name)


 def add_user(self,login,password):
    c = self.conn.cursor()
    c.execute("SELECT name FROM users WHERE name='"+login+"';")
    log = c.fetchone()
    if(log is not None):
        c.close()
    else:
      c.execute("INSERT INTO users (name,password) VALUES (?,?)", ((login), (password)))
      self.conn.commit()
      c.close()


 def prin_database(self):
    c = self.conn.cursor()
    c.execute("SELECT * FROM users")
    row=c.fetchone()
    while row is not None:
        print(row)
        row=c.fetchone()
    c.close()

     
 def clear(self):
    c = self.conn.cursor()
    c.execute("    DELETE FROM users;")
    self.conn.commit()
    c.close()

