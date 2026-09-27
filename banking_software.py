import csv          #all banking details will be stored in csv file
import os           #to check whether file exist or not
import random       #for generating unique userIDs
import bcrypt       #to hash a pin 
from getpass import getpass
class bankAccount():
    def __init__(self,name,userID,pin,balance):
        self.name=name
        self.pin=pin
        self.balance=int(balance)
        self.userID=userID
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            user['balance']=str(t.balance)
            save_accounts(accounts)
            print("Amount",amount,"successfully deposited")                
        else:
            print("Invalid request")
        return    
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            user['balance']=str(t.balance)
            save_accounts(accounts)
            print("Amount",amount,"successfully withdrawn")           
        else:
            print("Invalid request")
            return
        
    def deduct(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            user['balance']=str(t.balance)
            save_accounts(accounts)
            transfer_to_differentacc(amount)
            print("Amount",amount,"deducted from your account")           
        else:
            print("Invalid request")
        return
     
    def transfer(self,amount):
        if amount>0:
            self.balance+=amount
            trf['balance']=str(t.balance)
            save_accounts(accounts)
            print("Amount",amount,"successfully deposited")                
        else:
            print("Invalid request") 
        return         
    def balance_check(self):
        print("Your current balance is",self.balance)
        return
    

def transfer_to_differentacc(transfer):
    global trf
    trf=None
    acc=input('Enter the userID of the account you want to transfer: ')               
    accounts=load_accounts()
    try:
        for row in accounts:
            if row['userID']==acc :
                    trf=row               
                    break                              
        if trf:
            t=bankAccount(trf['name'],trf['userID'],trf['pin'],trf['balance'])
            t.transfer(transfer)  
    except Exception as e:
        print(e)


def load_accounts():
    with open('bank_details.csv','r',newline='') as file:
        return list(csv.DictReader(file))     #list contains dictionary as single element of a single user   
def save_accounts(accounts):   
    with open('bank_details.csv','w',newline='') as file:
        writer=csv.DictWriter(file,['name','userID','pin','balance'])        
        writer.writeheader()
        writer.writerows(accounts)
    
                        
def username(name):
    while True:
        low=name.lower()
        b=low.split()
        c=''
        for i in b:
            c+=i
            d=str(random.randint(1,999))
            c+=d
        c=list(c)
        c.append('@sbi.com')
        z=''.join(c)
        print('UserID suggesiton: ',end='')
        print(z)
        print('However you can create your own personalised ID')
        print('')
        user_ID=input('Enter your personalised userID: \n PRESS 2 to Exit' )
        accounts=load_accounts()
        for acc in accounts:
            if acc['userID']==user_ID:
                print('UserID already exists please try a different UserID')
                print('')
                break
            elif user_ID==2:
                break
        else:    
            return user_ID
            
                   
if not os.path.exists('bank_details.csv'):
    with open('/Python/Banking project/bank_details.csv','w',newline='') as file:
        writer=csv.DictWriter(file,['name','userID','pin','balance'])
        writer.writeheader()
z=0
while z==0:
    print('1:Create New Account')
    print('2:Login')
    print('3:Exit')
    try:
        ch=int(input('Enter your choice:'))
        if ch==1:
            new_name=input('Enter your name:')                  
            accounts=load_accounts()
            user_ID=username(new_name)
            # for acc in accounts:
            #     if acc['userID']==user_ID:
            #         print('UserID already exists please try a differnt UserID')
            #         break
            # for acc in accounts:
            #     if acc['name']==new_name:
            #         print('The user already exists')
            #         break
            #else:
            pin=input('Enter your pin:').encode()            # encode to convert to bytes
            hashed_pin=bcrypt.hashpw(pin,bcrypt.gensalt())   # takes string as input                 
            accounts.append({'name':new_name,'userID':user_ID,'pin':hashed_pin.decode(),'balance':'0'}) #decode to convert to string
            save_accounts(accounts)       
            print('New account has been created')
            print('')         
        elif ch==2:
            name=input('Enter your name or UserID:')
            print('!!!Your pin will be completely hidden for security reasons!!!')
            pin=getpass('Enter your pin:').encode()  #takes string as input           
            accounts=load_accounts()
            user=None
            for row in accounts:
                stored_hash=row['pin'].encode()
                if row['name']==name and bcrypt.checkpw(pin,stored_hash):
                    # if Id==name and bcrypt.checkpw(pin,stored_hash):
                        user=row  #access all data of a user
                        break

                elif row['userID']==name and bcrypt.checkpw(pin,stored_hash):
                        user=row
                        break
                # if (row['name']==name or row['userID']==name) and bcrypt.checkpw(pin,stored_hash):
                #     user=row 
                #     break           
            if user:
                t=bankAccount(user['name'],user['userID'],user['pin'],user['balance'])
                while True:               
                    print("  ")
                    print("1:Deposit")
                    print("2:Withdraw") 
                    print("3:Check Balance")
                    print("4:Transfer to other account")
                    print("5:Exit to main menu")
                    print("  ")
                    try:
                        a=int(input("Enter your choice:"))
                        print('')
                        if a==1:        
                            d=int(input("Enter the amount you want to deposit:"))        
                            t.deposit(d)  
                        elif a==2:
                            d=int(input("Enter the amount you want to withdraw:"))       
                            t.withdraw(d)  
                        elif a==3:       
                            t.balance_check()      
                        elif a==4:
                            d=int(input('Enter the amount you want to transfer'))
                            t.deduct(d)
                             
                        elif a==5:
                            break    
                    except:
                        print('')
                        print('Wrong input!!!')                               
            else:
                print('Invalid Login')
        elif ch==3:
            break   
    except Exception as e:
        print('')
        print('Wrong input!!!',e)   
