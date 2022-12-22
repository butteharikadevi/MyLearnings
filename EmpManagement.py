import pymysql
class Emp:
    def __init__(self,no,name,sal,addr):
        self.eno=no
        self.ename=name
        self.esal=sal
        self.eaddr=addr

    def createEmp(self):
        try:
            con = pymysql.connect(host='localhost', database='harikadb', user='dbaharika', password='harika1990')
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

myEmp = Emp(1,'RRR', 10000, 'Hyderabad')
myEmp.createEmp()
