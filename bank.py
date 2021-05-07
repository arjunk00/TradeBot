import mysql.connector as sqltor
from nsetools import Nse
nse = Nse()
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

class DematAccount(Account):
    def __init__(self, user, balance):
        super().__init__(user, balance)
        cursor.execute("create table if not exists DematAccount (user varchar(200) foreign key references Account(user), stockowned char(50) primary key, buyingprice float, qty int;")
    def networth():
        cursor.execute("select stockowned, qty from DematAccount where user='"+str(self.user)+"';")
        data = cursor.fetchall()
        worth = 0
        for i in data:
            curprice = nse.get_quote(i[0])['lastPrice']
            worth += i[1]*curprice
        return worth
    def buystock(stock_code,quantity):
        curprice = nse.get_quote(stock_code)['lastPrice']
        self.pay(curprice*quantity)
        operation = ""
        cursor.execute(operation)

        


parthacc = Account("Parth Gupte",10000)
print(parthacc.balance)
sqlcon.close()

        
