import os 
import random
import sys                                                           #ketabkhane sys baraye khroj az commend line
os.system("cls")                                                     #ketabkhane rendom baraye shomare card va ccv2 random
print("""                                                                                               
     _____       _ _       _       ___ ________  ___
    | ___ \     | | |     | |     / _ |_   _|  \/  |
    | |_/ / __ _| | |_   _| | __ / /_\ \| | | .  . |
    | ___ \/ _` | | | | | | |/ / |  _  || | | |\/| |
    | |_/ | (_| | | | |_| |   <  | | | || | | |  | |
    \____/ \__,_|_|_|\__,_|_|\_\ \_| |_/\_/ \_|  |_/
                                                
|-------------be ATM BALLUK khoshamadid----------------------|             

Creator : Navid Arteshi
Telegram : t.me/navid_cap
Instagram : instagram.com/navid_cap 

""")

class ATM:                                                         #yek class ba mohtavaye database va i (shomarande ozviyat Bank)
    
    def __init__(self):
        self.db={

    "p0":{"account":{"card_number":"0014831123441500","cvv2":"1234","password":"1234","exp":"02/04","fname":"navid","lname":"areteshi","balance":"100000"}}, 
    "p1":{"account":{"card_number":"0014831123441501","cvv2":"5678","password":"5678","exp":"05/11","fname":"noshin","lname":"mohamadzade","balance":"100000"}} 
    

}       
       


    def str_maker_card(self,u_card):                       #in function baraye str kardan listi ke ketabkhane random be ma mide ta dar database estefade shavad
        self.card_number_str=""
        for i in range(0,len(u_card)):
            m="".join(str(u_card[i]))
            self.card_number_str += str(m)
        return self.card_number_str

    def str_maker_cvv2(self,u_cvv2):                       #in function baraye str kardan listi ke ketabkhane random be ma mide (cvv2) ta dar data bace estefade beshe
        self.cvv2_str=""
        for i in range(0,len(u_cvv2)):
            w="".join(str(u_cvv2[i]))
            self.cvv2_str +=str(w) 
        return self.cvv2_str
    
    def ozviyat(self):                                 #function ozviyat ke dar dakhel try except neveshte shode ta har gone erorr code dobare be func show() bargarda va code stop nashavd
        try:
            print("------Be Safheye Ozviyat Bank BALLUK Khosh Amadid------------|")
            p_number="p"+str(len(self.db))                                        #az i class dae inja estefade mikonim baraye shomaresh tedad moshtari haye bank
            card_number=[0,0,1,4]+(random.choices(range(0,10),k=12))          #card number bank balluk ba 0014 shoro shode v 12 ragam be sorat random entekhab mishavad
            cvv2=(random.choices(range(0,10),k=4))                              #cvv2 bank 4 ragami be sorat random entekhab mishavd
            exp="0"+str(random.randint(2,9))+"/"+str(random.randint(1,12))        #exp card be sorat random entekhab mishavad da baze 1402 ta 1409 
            while True:                                               #halge baraye ozviyat
                fname=input("nam khod ra vared konid\n---> ")              #nam va nam khanevadegi gerefte mishe
                lname=input("nam khanevadegi khod ra vared konid\n---> ")
                if lname and fname != "":                                  #shart ma ine ke karbar natavanad field hara khali rad konad
                    break
                else:
                    print("!!! lotfan etalat ro dagig vared konid vared konid !!!")
            while True:                                                             #halge bareye daryaft pass az karbar
                password=int(input("password entekhabi khodra vared konid\n---> "))
                if (len(str(password))) == 4:                                           #shart in ast ke az karbar fagat pass 4 ragami daryaft shavad va gar bekhahad ba "enter" field ra khali begozarad be func show() bar migardad
                    break
                else:
                    print("!!! ramz bayad 4 ragami bashad !!!")
            balance=int(input("mojodi cart khodeton ro vared konid\n---> "))            #bank ma kheyli bahale mojodi ro khodet mid agar chizi geyre int vared field shavad be func show() barmigardim
            self.str_maker_card(card_number)                                             #dar inja list hayi az adad tasadofi sakhte shode card va cvv2 ro be func haye str maker cvv2 v card number midahim be onvan megdar!
            self.str_maker_cvv2(cvv2)
            print(f"ozviyat shoma anjam shod\nshomare card = {self.card_number_str}\ncvv2={self.cvv2_str}\npasswor={password}\nexp={exp}\ncard banki benam {fname} {lname}\nmojodi card = {balance}")  #dar inja etelaat Banki karbar ozv shode ro be karbar neshan midahim 
            self.db[p_number]={"account":{"card_number":self.card_number_str,"cvv2":self.cvv2_str,"password":str(password),"exp":exp,"fname":fname,"lname":lname,"balance":str(balance)}}     #dar db ba etelat gerfete shode az karbar db ro upgrade mikonim   
            print(self.db)
            self.show()    #ozviyat tamamshod barmigardim be safheye aval atm yani func show()
        except:                                   
            print("az ATM BALLUK kharej shodid dar vared kardan atelaat khod degtat konid !!! ♥")
            self.show()
    
    def show(self):
        print("|------be khadamat bedon kart khosh amadid-------------------|")
        ozv=input("\n***agar ozv balluk bank nistin kalmeye 'OZV' ro vared konid***\n\n|----------agar ozv hastin enter bezanid---------------------|\n\n☺-----baraye kharej shodan az ATM 'EXIT' ra type konid------☺\n\n--->")
        match ozv.upper():
            case "OZV":
                self.ozviyat()
            case "EXIT":
                self.exit()
            case _:
                x = False
                while True:
                    darkhast_card_number=input("shomare kart ra vared konid:\n---> ")                
                    for i in range(len(self.db)) :
                        if darkhast_card_number != "" :
                            if len(darkhast_card_number)==16:
                                if darkhast_card_number == self.db["p"+str(i)]["account"]["card_number"]:
                                    self.karbar=self.db["p"+str(i)]
                                    x =True
                                    break
                        else:
                            print("!!! field shomare card ro khali nagozarid !!!")
                            self.show()

                    if (x == True):
                        break
                    else:
                        print("!!! shomare card ehstebah hast !!!")
                y=False
                while True:
                    darkhast_password=input("password khod ra vared konid:\n---> ")
                    for i in range(len(self.db)) :         
                        if darkhast_password != "":
                            if len(darkhast_password)==4:
                                if darkhast_password == self.db["p"+str(i)]["account"]["password"] and darkhast_card_number == self.db["p"+str(i)]["account"]["card_number"] :
                                    y=True
                                    break
                        else:
                            print("!!! field password ro khali nagozarid !!!")
                            self.show()
                    if (y == True):
                        print("|------lotfan khadamat mored niyaz khodra entekhab konid-----|")
                        self.meno_khadamat()
                        break
    
                    else:
                        print("!!! password ehstebah hast !!!")

    def meno_khadamat(self):
        try:
            print(f"""#----------{self.karbar["account"]["fname"]} {self.karbar["account"]["lname"]}------------#""")
            print("1.tagir etelaat")
            print("2.etela az mojodi")
            print("3.card be card")
            print("4.mosbage ba atm")
            print("5.bazgasht be sfhaye vorod")
            print("6.exit")
            while True:
                shomare_khadamat=int(input("|------shomare khadamat mord nazar vared konid---------------|\n---> "))
                if len(str(shomare_khadamat)) == 1 :
                    if 0 < shomare_khadamat < 7:
                        break
                    else:
                        print("lotfan yeki az adad haye khadamat ra entekhab konid")
                else:
                    print("lotfan yeki az adad haye khadamat ra entekhab konid")
            if shomare_khadamat == 1:
                self.tagir_etelaat()
            if shomare_khadamat == 2:
                print("dar hal beroz resani")
            if shomare_khadamat == 3:
                print("dar hal beroz resani")
            if shomare_khadamat == 4:
                print("dar hal beroz resani")
            if shomare_khadamat == 5:
                self.show()
        except:
            print("!!!! dar entekhab shomare amaliyat degat konid !!!!")
            self.meno_khadamat()
    
        if shomare_khadamat == 6:
            self.exit()

    def tagir_etelaat(self):
        
        print(f"""----------- {self.karbar["account"]["fname"]} {self.karbar["account"]["lname"]}--------|""")
        print("1.tagir password")
        print("2.montazer update haye badi bashin :)")
        while True:
            khadamat_tagir=int(input("----shomare khadamat mored nazar khod ra vared konid----------|\n---> "))
            if len(str(khadamat_tagir)) == 1 :
                if 0 < khadamat_tagir < 2:
                    break
                    
                else:
                     print("az meno adad khadamat khod ra entekhab konid ")
            else:
                print("az meno adad khadamat khod ra entekhab konid ")
        if khadamat_tagir == 1:
            while True:
                old_pass=int(input("remaz gabli khodra vared konid\n---> "))
                if len(str(old_pass))==4:
                    if str(old_pass) == self.karbar["account"]["password"]:
                        break
                    else:
                        print("ramz ehstebah hast")
                else:
                    print("ramz eshtebah hast")
            while True:
                new_pass=input("ramz jadid ra vared konid\n---> ")
                if new_pass != "" :
                    if len(str(new_pass))==4:
                        new_pass2=input("ramz jadid khod ra dobare vared konid\n---> ")
                        if new_pass == new_pass2:
                            if new_pass != str(old_pass):
                                self.karbar["account"]["password"]=new_pass2
                                print("!-|____remz shoma tagir yaft____|-!")
                                break
                            else:
                                print("$-----shoma nemitavanid az ramz gabli be onvan ramz jadid estefade konid-----$")
                        else:
                            print("!!!!!! ramz shoma baham tatabog nadarad !!!!!!")
                    else:
                        print("ramz 4 ragami bayad bashad")
                else:
                     print("ramz 4 ragami bayad bashad")

        self.meno_khadamat()

    def exit(self):
        print("  ^^    az in ke BAANK BALLUK ro targih dadid mamnonim   ( ͡⚆ ͜ʖ ͡⚆)  ")
        os._exit(0)



c_atm=ATM()
c_atm.show()