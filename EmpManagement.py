import pymysql
from jproperties import Properties
props=Properties()
with open("application.properties",'rb') as ap:
    props.load(ap)

class Emp:
    def __int__(self):
        self.eno

    def __init__(self,no,name,sal,addr):
        self.eno=no
        self.ename=name
        self.esal=sal
        self.eaddr=addr

    def createEmp(self):
        try:
            con = pymysql.connect(host=props.get('host').data, database=props.get('database').data,user=props.get('user').data, password=props.get('password').data)
            cursor = con.cursor()
            query = """INSERT INTO employees1 (eno, ename, esal, eaddr) 
                                        VALUES (%s,%s, %s, %s) """
            cursor.execute(query,(self.eno,self.ename,self.esal,self.eaddr))
            con.commit()
            print("Record inserted successfully")

        except pymysql.DatabaseError as e:
            if con:
                con.rollback()
                print("there is a problem in db:", e)
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close

    def getAllEMp(self):
        try:
            con = pymysql.connect(host='localhost', database='harikadb', user='dbaharika', password='harika1990')
            cursor = con.cursor()
            query = """select * from  employees1"""
            cursor.execute(query)
            myresult = cursor.fetchall()
            resultList=[]
            for x in myresult:
                resultList.append(x)
                print(x)
            return resultList


        except pymysql.DatabaseError as e:
                print("there is a problem in db:", e)
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close

    def getAEMp(self):
        try:
            con = pymysql.connect(host='localhost', database='harikadb', user='dbaharika', password='harika1990')
            cursor = con.cursor()
            query = """select * from  employees1 where eno=%s"""
            cursor.execute(query,self.eno)
            myresult = cursor.fetchall()
            resultList = []
            for x in myresult:
                resultList.append(x)
                print(x)
            return resultList


        except pymysql.DatabaseError as e:
                print("there is a problem in db:", e)
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close

    def getEmpName(self):
        try:
            con = pymysql.connect(host='localhost', database='harikadb', user='dbaharika', password='harika1990')
            cursor = con.cursor()
            query = """select * from  employees1 where ename=%s"""
            cursor.execute(query,self.ename)
            myresult = cursor.fetchall()
            resultList = []
            for x in myresult:
                resultList.append(x)
                print(x)
            return resultList


        except pymysql.DatabaseError as e:
                print("there is a problem in db:", e)
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close



myEmp = Emp(1,'RRR', 10000, 'Hyderabad')
myEmp.createEmp()
