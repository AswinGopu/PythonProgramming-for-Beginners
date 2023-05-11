#!python 

import sqlite3 as s


con = s.connect('db/Items.db')
cur = con.cursor()
while True:
    print("1. Create Table")
    print("2. Insert Table Values")
    print("3. Select Table")
    print("4. Update Table")
    print("5. Delete Table")
    print("4. Exit")
    n = int(input("Choose your option : "))
    if n == "1": 
        sql="select * from items"
        cur.execute(sql)
        res= cur.fetchall()
        if len(res)>0:
            sql="""create table `items`(`id` PRIMARY_KEY, `items`TEXT(40),`PRICE`REAL)"""
            cur.execute(sql)
            cur.close()
            con.close()
            print("table item added")
        else:
            print("table is already created..!")
    elif n=="2":
        m=int(input("enter the limit : "))
        for i in range(0,m):
            item = input("enter the item : ")
            price = int(input("enter the price in digit : "))
            sql = "select ifnull(max(id),0)+ 1 from items"
            cur.execute(sql)
            id = cur.fetchall()[0][0]
            sql = "inset into items values('%s','%s','%s')"%(id,item,price)
            cur.execute(sql)
            con.commit()
            print("1 row created....")
        print("table data inserted")    
    elif n=="3":
        sql = "select * from items"
        cur.execute(sql)
        res = cur.fetchall()
        print("| ID | \t ITEM | PRICE")
        print("_"*50)
    elif n=="4":
        sql="select * from items"
        cur.execute(sql)
        res = cur.fetchall()
        print("| ID | \t ITEM | PRICE")
        print("_"*50)
        for i in res:
            print("| %5s | %10s | %5s |"%(i[0],i[1],i[2]))
        print("_"*50)    
        up = int(input("enter your update table id : "))
        item = input("update item : ")
        price = input("update price : ")
        sql = "update item set item = '%s',price = %s wher id = '%s'"%(item,price,up)
        cur.execute(sql)
        con.commit()
        sql="select * from items"
        cur.execute(sql)
        res=cur.fetchall()
        print("| ID | \t ITEM | PRICE")
        print("_"*50)
        for i in res:
            print("| %5s | %10s | %5s |"%(i[0],i[1],i[2]))
        print("_"*50)
    elif n=="5":
        sql="select * from items"
        cur.execute(sql)
        res = cur.fetchall()
        print("| ID | \t ITEM | PRICE")
        print("_"*50)
        for i in res:
            print("| %5s | %10s | %5s |"%(i[0],i[1],i[2]))
        print("_"*50)    
        up = int(input("enter your delete table id : "))
        sql = "delete from items where id = '%s'"%up
        cur.execute(sql)
        con.commit()
        print("1 row deleted...!")
    elif n=="6":
         print("programe exit...")
       

        



         




    
       