'''from flask import *

from MyLearnings.EmpManagement import Emp

app=Flask(__name__)

@app.route('/create',methods=["GET","POST"]) # GET: http://localhost:80/create?id=value1&name=Valu2....
def home():
    args = request.args # reads all query params
    request.data
    eid = args.get('id') # id is should be in query param
    ename = args.get('name') # name is should be in query param
    esal = args.get('sal')
    eaddr = args.get('addr')
    myEmp = Emp(eid, ename, esal, eaddr)
    myEmp.createEmp()
    return 'Welcom HARIKA flask...'

@app.route('/getAllEmp',methods=['GET'])
def getAllEmp():
    myEmp =  Emp(1, 'RRRRR', 20000, 'Hyderabad')
    return  myEmp.getAllEMp()

@app.route('/getEmp',methods=['GET'])
def getEmp():
    args=request.args
    eid = args.get('id')
    myEmp=Emp(eid,'',0,'')
    myresult = myEmp.getAEMp()
    return myresult
@app.route('/getEmpbyName',methods=['GET'])
def getEmpName():
    args=request.args
    ename=args.get('name')
    myEmp = Emp(0, ename, 0, '')
    myresult = myEmp.getEmpName()
    return myresult


if __name__=='__main__':
    app.secret_key='aabbcc'
    app.run(host='0.0.0.0',port=80)'''

from flask import *

app=Flask(__name__)

@app.route('/home',methods=['GET'])
def first():
    return 'Welcom to my flask....HARIKA'


@app.route('/index',methods=['GET'])
def index():
    return 'Welcom to Indexing....HARIKA'

@app.route('/login',methods=['POST'])
def logging():
    #username
    #password
    username=request.form['username']
    password=request.form['password']
    print(username)
    print(password)
    return 'Welcom to login...HARIKA'

@app.route('/login',methods=['GET'])
def login_get():
    #username
    #password
    username=request.args['username']
    password=request.args['password']
    print(username)
    print(password)
    return 'Welcom to login...HARIKA'

@app.route('/loginjson',methods=['POST'])
def login_json():
    request_data=request.get_json()
    print(request_data)
    username=request_data['username']
    password=request_data['password']
    print(username)
    print(password)
    return 'Welcom to login...HARIKA'




if __name__=='__main__':
    app.secret_key='zxcvb'
    app.run(host='0.0.0.0',port=80)

