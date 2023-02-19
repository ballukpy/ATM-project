import os 
import random
os.system("cls")
print("""                                                                                               
 _____       _ _       _       ___ ________  ___
| ___ \     | | |     | |     / _ |_   _|  \/  |
| |_/ / __ _| | |_   _| | __ / /_\ \| | | .  . |
| ___ \/ _` | | | | | | |/ / |  _  || | | |\/| |
| |_/ | (_| | | | |_| |   <  | | | || | | |  | |
\____/ \__,_|_|_|\__,_|_|\_\ \_| |_/\_/ \_|  |_/
                                                
-------------be ATM BALLUK khoshamadid-------------------

Creator : Navid Arteshi
Telegram : t.me/navid_cap
Instagram : instagram.com/navid_cap 

""")

class ATM:
    
    def __init__(self):
        self.db={

    "p1":{"account":{"card_number":"0014831123441500","cvv2":"1234","password":"1234","exp":"02/04","fname":"navid","lname":"areteshi","balance":"100000"}}, 
    "p2":{"account":{"card_number":"0014831123441501","cvv2":"5678","password":"5678","exp":"05/11","fname":"noshin","lname":"mohamadzade","balance":"100000"}} 
    

}       
        self.i=3


    def str_maker_card(u_card):
        global card_number_str
        card_number_str=""
        for i in range(0,len(u_card)):
            m="".join(str(u_card[i]))
            card_number_str += str(m)
        return card_number_str

    def str_maker_cvv2(u_cvv2):
        global cvv2_str
        cvv2_str=""
        for i in range(0,len(u_cvv2)):
            w="".join(str(u_cvv2[i]))
            cvv2_str +=str(w) 
        return cvv2_str
         
    def ozviyat(self):
        try:
            print("------be safheye ozviyat bank BALLuk khosh amadid------")
            p_number="p"+str(self.i)
            card_number=[0,0,1,4]+(random.choices(range(0,10),k=12))
            cvv2=(random.choices(range(0,10),k=4))
            exp="0"+str(random.randint(2,9))+"/"+str(random.randint(1,12))
            while True:
                fname=input("nam khod ra vared konid\n---> ")
                lname=input("nam khanevadegi khod ra vared konid\n---> ")
                if lname and fname != "":
                    break
                else:
                    print("!!! lotfan etalat ro dagig vared konid vared konid !!!")
            while True:    
                password=int(input("password entekhabi khodra vared konid\n---> "))
                if (len(str(password))) == 4:
                    break
                else:
                    print("!!! ramz bayad 4 ragami bashad !!!")
            balance=int(input("mojodi cart khodeton ro vared konid\n---> "))
            ATM.str_maker_card(card_number)
            ATM.str_maker_cvv2(cvv2)
            print(f"ozviyat shoma anjam shod\nshomare card = {card_number_str}\ncvv2={cvv2_str}\npasswor={password}\nexp={exp}\ncard banki benam {fname} {lname}\nmojodi card = {balance}")
            self.db[p_number]={"account":{"card_number":card_number_str,"cvv2":cvv2_str,"password":str(password),"exp":exp,"fname":fname,"lname":lname,"balance":str(balance)}}       
            c_atm.show()
        except:
           print("az ATM BALLUK kharej shodid dar vared kardan be atelaat khod degtat konid !!! ♥")
    def show(self):
        print("------be khadamat bedon kart khosh amadid------")
        
        ozv=input("agar ozv balluk bank nistin kalmeye 'OZV' ro vared konid\n------agar ozv hastin enter bezanid------\n")
        if ozv == "OZV" :
            global c_atm
            c_atm=ATM()
            c_atm.ozviyat()
        else:
            x = False
            while True:
                darkhast_card_number=input("shomare kart ra vared konid:\n---> ")                
                for i in range(1,len(self.db)+1) :
                    if darkhast_card_number != "" :
                        if len(darkhast_card_number)==16:
                            if darkhast_card_number in self.db["p"+str(i)]["account"]["card_number"]:
                                x =True
                                break
                if (x == True):
                    break
                else:
                    print("!!! shomare card ehstebah hast !!!")
            y=False
            while True:
                darkhast_password=input("password khod ra vared konid:\n---> ")
                for i in range(1,len(self.db)+1) :         
                    if darkhast_password != "":
                        if len(darkhast_password)==4:
                            if darkhast_password in self.db["p"+str(i)]["account"]["password"]:
                                y=True
                                break
                if (y == True):
                    print("|------lotfan khadamat mored niyaz khodra entekhab konid------|")
                    break
 
                else:
                    print("!!! password ehstebah hast !!!")

c_atm=ATM()
c_atm.show()
