import mysql.connector as sqltor
sqlcon = sqltor.connect(host='localhost',user='root',password='tiger')
cursor = sqlcon.cursor()
cursor.execute("create database if not exists tradebot;")
cursor.execute("use tradebot;")

class Account:
    def __init__(self,user,balance):
        self.user = user
        self.balance = balance
        cursor.execute("create table if not exists Account (user varchar(200) primary key, balance float);")
        try:
            cursor.execute("insert into Account values('"+str(self.user)+"',"+str(self.balance)+");")
        except:
            print("User already exists")
        finally:
            sqlcon.commit()
    
    def gain(amount):
        if -amount <= self.balance:
            self.balance = self.balance + amount
            cursor.execute("update table Account set balance="+str(self.balance)+";")
            sqlcon.commit()
        else:
            print("Not enough balance")
    def pay(amount):
        gain(-amount)
    def recieve(amount):
        gain(amount)

parthacc = Account("Parth Gupte",10000)
print(parthacc.balance)
sqlcon.close()

        
