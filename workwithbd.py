import sqlite3

class bd():
 def __init__(self,name):
     self.conn = sqlite3.connect(name)


 def add_user(self,login,password,name,family):
    c = self.conn.cursor()
    c.execute("SELECT login FROM users WHERE login='"+login+"';")
    log = c.fetchone()
    if(log is not None  or len(login)<=6 or len(password)<=6):
        c.close()
        return False
    else:
      c.execute("INSERT INTO users (login,password,name,family) VALUES (?,?,?,?)", ((login), (password), (name), (family)))
      self.conn.commit()
      c.close()
      return True


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
 def delete(self,name):
     c = self.conn.cursor()
     c.execute("DROP TABLE IF EXISTS " + name+";")
     self.conn.commit()
     c.close()
 def create(self,name):
     c = self.conn.cursor()
     c.execute(" CREATE TABLE "+name+" (login TEXT, password TEXT, name TEXT, family TEXT) " + ";")

