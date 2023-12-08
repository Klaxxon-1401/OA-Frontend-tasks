N='Name'
M="Mail"
U='Username'
P='Password'
v=[
            Jake={'Name':'Jake','Mail':'Jake@gmail.com','Username':'Jake1','Password':'Jake@123'}
            Dave={N:'Dave',M:'Dave@gmail.com',U:'Dave1',P:'Dave@123'}
            Fred={N:'Fred',M:'Fred@gmail.com',U:'Fred1',P:'Fred@123'}
            Rachel={N:'Rachel',M:'RAchel@gmail.com',U:'Rach1',P:'Rach@123'}
        ]
import pymongo
client = pymongo.MongoClient('mongodb+srv://DevanDuraiPragash:Devan1401@cluster0.weyhdl2.mongodb.net/?retryWrites=true&w=majority')
DB1=client['LoginDatabase']
col1=DB1['Attempt 1']
col1.insert_many(v)



usr=input('Enter Username:')

b=list(dict1.keys())
c=list(dict1.values())

def First(*dict1):
    dict1={'Jake':'Jake@123','Joey':'Joey@123','Rachel':'Rach@123','Chandler':'Chan@123'}
    b=list(dict1.keys()) 
    c=list(dict1.values())
    Second()

def First2(dict1):
    usr=input('Enter Username: ')
    First(dict1)


def Signup():
    dict1={'Jake':'Jake@123','Joey':'Joey@123','Rachel':'Rach@123','Chandler':'Chan@123'}
    usr2=input('Enter Your Name: ')
    pwd1=input('Enter Your Password: ')
    pwd2=input('ReEnter Your Password: ')
    if(pwd1 ==  pwd2):
        dict1.update({usr2 : pwd1})
    else:
        while(pwd1!=pwd2):
            print('Password do not match ')
            pwd1=input('Enter Your Password')
            pwd2=input('ReEnter Your Password')
    return (dict1)
        
def passwordreset():
    n1=input('Enter New Password: ')
    n2=input('RenEnter New Password: ')
    while(n1!=n2):
        print('Passwords do not match \nReEnter Password')
        n1=input('Enter New Password: ')
        n2=input('ReEnter New Password: ')
    dict1.update({usr : n1})
    b=list(dict1.keys())
    c=list(dict1.values())
    x=b.index(usr)
    y=c[x]
    return y
        
def passwordVerify(psd):
    x=b.index(usr)
    y=c[x]

    while(psd != y):
        for i in range(0,1):
            psd=input('Enter Password:')
            if(psd == y):
                continue
            print('Invalid Password')
            n=input('Would you like to reset your password? ')
            if(n=='Yes'):
                y=passwordreset()

    if(psd == y):
        print('*Loading Homepage*')

def Second():            
    if(usr in b):
        psd=input('Enter Password:')
        passwordVerify(psd)
        
    else:
        print('User does not exist in database')
        s=input('Would you like to Sign Up?')
        if(s=='Yes'):
            lol=Signup()
            print('SignUp completed \nUser Added to Database\n')
            print(lol)
            First2(lol)
        else:
            print('Program complete')

##First()



for i in col1.find():
    print(i['Name'])
