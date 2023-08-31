import mysql.connector
from tabulate import tabulate
con=mysql.connector.connect(host="localhost",user="root",password="siva",database="marks")
def inserting(Sno, Name, Age, M1, M2, M3, M4, M5):
    res = con.cursor()
    sql = "insert into rooted (Sno,Name,Age,M1,M2,M3,M4,M5) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    users = (Sno, Name, Age, M1, M2, M3, M4, M5)
    res.execute(sql, users)
    con.commit()
    print("That was inserted..please check.")
def updating(Name, Age, M1, M2, M3, M4, M5,Sno):
    res = con.cursor()
    sql = "update marks.rooted set Name=%s, Age=%s, M1=%s, M2=%s, M3=%s, M4=%s,M5=%s where Sno=%s"
    users = (Name, Age, M1, M2, M3, M4, M5,Sno)
    res.execute(sql, users)
    con.commit()
    print("That was updated..please check.")
def deleting(Sno):
    res = con.cursor()
    sql = "delete from marks.rooted where Sno=%s"
    users = (Sno,)
    res.execute(sql, users)
    con.commit()
    print("That was deleted..please check.")
def selecting():
    res = con.cursor()
    sql = "SELECT Sno,Name, Age, M1, M2, M3, M4, M5 from rooted"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result, headers=["Sno","Name", "Age", "M1", "M2", "M3", "M4", "M5"]))

while True:
    print("""Enter your choice:
    1.Insert
    2.Update
    3.Delete
    4.Show 
    5.Quit
    """)
    ch=int(input("Enter Your choice:"))
    if ch==1:
        Sno=input("ENter the series:")
        Name = input("Enter the Name:")
        Age = int(input("Enter the age:"))
        M1 = int(input("Enter the 1 subject mark:"))
        M2 = int(input("Enter the 2 subject mark:"))
        M3 = int(input("Enter the 3 subject mark:"))
        M4 = int(input("Enter the 4 subject mark:"))
        M5=int(input("Enter the 5 subject mark:"))
        inserting(Sno, Name, Age, M1, M2, M3, M4, M5)
    elif ch==2:
        Sno = int(input("Ener the Id it will be Change:"))
        Name = input("Enter the Name:")
        Age = int(input("Enter the age:"))
        M1 = int(input("Enter the 1 subject mark:"))
        M2 = int(input("Enter the 2 subject mark:"))
        M3 = int(input("Enter the 3 subject mark:"))
        M4 = int(input("Enter the 4 subject mark:"))
        M5 = int(input("Enter the 5 subject mark:"))
        updating(Name, Age, M1, M2, M3, M4, M5,Sno)
    elif ch==3:
        Sno = int(input("Ener the Id it will be Deleted:"))
        deleting(Sno)
    elif ch==4:
        selecting()
    elif ch==5:
        quit()
    else:
        print("Invalid:")


print("ok")

