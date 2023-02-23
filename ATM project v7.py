import os 
import random                                                         #ketabkhane os baraye khroj az commend line
os.system("cls")                                                     #ketabkhane rendom baraye shomare card va ccv2 random
print("""                                                                                               
     _____       _ _       _       ___ ________  ___
    | ___ \     | | |     | |     / _ |_   _|  \/  |
    | |_/ / __ _| | |_   _| | __ / /_\ \| | | .  . |
    | ___ \/ _` | | | | | | |/ / |  _  || | | |\/| |
    | |_/ | (_| | | | |_| |   <  | | | || | | |  | |
    \____/ \__,_|_|_|\__,_|_|\_\ \_| |_/\_/ \_|  |_/
                                                
|----------------Be ATM BALLUK Khoshamadid-------------------|             

Creator : Navid Arteshi
Telegram : t.me/navid_cap
Instagram : instagram.com/navid_cap 
atm language : persian (finglish)

""")

class ATM:                                                         #yek class ba mohtavaye database 
    
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
    
    def ozviyat(self):                                 #function ozviyat vase safheye ozviyat hasteshe ke dar dakhel try except neveshte shode ta har gone erorr code dobare be func show() bargarda va code stop nashavd
        try:
            print("------Be Safheye Ozviyat Bank BALLUK Khosh Amadid------------|")
            p_number="p"+str(len(self.db))                                        #az len db inja estefade mikonim baraye shomaresh tedad moshtari haye bank
            card_number=[0,0,1,4]+(random.choices(range(0,10),k=12))          #card number bank balluk ba 0014 shoro shode v 12 ragam be sorat random entekhab mishavad
            for i in range(len(self.db)):
                if self.str_maker_card(card_number) != self.db["p"+str(i)]["account"]["card_number"]:  #dar inja az tekrari shodan shomare kart ha jelogiri mishavad
                    pass
                else:
                    print("moshkeli pish amade dobare emtahan konid")
                    self.ozviyat()
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
                password=int(input("password entekhabi khodra vared konid\nyek adad '4' ragami dar nazar begiri\n---> "))
                if (len(str(password))) == 4:                                           #shart in ast ke az karbar fagat pass 4 ragami daryaft shavad va gar bekhahad ba "enter" field ra khali begozarad be func show() bar migardad
                    break
                else:
                    print("!!! ramz bayad 4 ragami bashad !!!")
            balance=int(input("mojodi cart khodeton ro vared konid\n---> "))            #bank ma kheyli bahale mojodi ro khodet mid agar chizi geyre int vared field shavad be func show() barmigardim
            self.str_maker_card(card_number)                                             #dar inja list hayi az adad tasadofi sakhte shode card va cvv2 ro be func haye str maker cvv2 v card number midahim be onvan megdar!
            self.str_maker_cvv2(cvv2)
            print(f"ozviyat shoma anjam shod\ncard banki benam {fname} {lname}\nshomare card = {self.card_number_str}\ncvv2={self.cvv2_str}\npasswor={password}\nexp={exp}\nmojodi card = {balance}")  #dar inja etelaat Banki karbar ozv shode ro be karbar neshan midahim 
            self.db[p_number]={"account":{"card_number":self.card_number_str,"cvv2":self.cvv2_str,"password":str(password),"exp":exp,"fname":fname,"lname":lname,"balance":str(balance)}}     #dar db ba etelat gerfete shode az karbar db ro upgrade mikonim   
            self.show()    #ozviyat tamamshod barmigardim be safheye aval atm yani func show()
        except:                                   
            print("type:restart_ozviyat :az ATM BALLUK kharej shodid dar vared kardan atelaat khod degtat konid !!! ♥")  #agar erorr shod (masalan karbar be jaye adad harf dad be atm) in jomlaro pront kone va be safheye aval bargarde
            self.show()
    
    def show(self):         #function show meno asli bank ro tashkil mide ke tabe function haye ozviyat , exit va meno khadamat dakheleshan 
        try:
            """be himaliya khosh omadin"""
            print("|-----------be khadamat bedon kart khosh amadid--------------|")
            print("|-------baraye edame az gozine haye zir entekhab konid-------|")
            print("1.vorod be bank")
            print("2.ozviyat")
            print("3.rahnoma ATM (HELP)")
            print("4.EXIT")
            while True:
                self.ozv=int(input("|------ baraye edame gozine mored nazar ra vared koini-------|\n---> "))
                if len(str(self.ozv)) == 1:
                    if 0 < self.ozv < 5:
                        break
                    else:
                        print("az beyn gozine ha entekhab konid")
                else:
                    print("az beyn gozine ha entekhab konid")
        except:
            print("ba vared kardan adad '3' az rahnomayi atm (HELP) jahat behtar va rahat tar estefade kardan komak begirid")
            print("type: restart_show lotfan az gozine ha entekhab konid :).")
            self.show()
        match self.ozv:            #dar inja az karbar baraye entekhab meno ozviyat ya baraye vorod be bank darkhat midim 
            case 2:               #agar ozv vared kard be safhe ozviyat montagel mishe
                self.ozviyat()
            case 3:   
                self.help()            #agar ozv vared kard be safhe ozviyat montagel mishe
            case 4:               #agar exit vared kard az barname kharej mishe
                self.exit()
            case 1:                     #agar hich kodam ra vared nakard va enter ya hatchi geyre in balahayi zad be ehsterak sanj vared mishavad
                x = False                #yek motager be nam x ba megdar False darim
                while True:
                    darkhast_card_number=input("shomare kart ra vared konid:\n---> ")                #inja yek halge darim baraye daryaf shomarekart
                    for i in range(len(self.db)) :                                                   #va ba shart ha az khali gozashtan field ha va kam ya ziyad vared kardan shomare kart jelogiri mishavad
                        if darkhast_card_number != "" :                                              #ba estefade az for (halge) tamam db barresi mishavad ke aya in shomare kart vojod darad ya na
                            if len(darkhast_card_number)==16:                                         
                                if darkhast_card_number == self.db["p"+str(i)]["account"]["card_number"]:
                                    self.karbar=self.db["p"+str(i)]
                                    x =True                                                          #agar vojod dasht az db fname va lname moshtari zakhire mishvad va halge for payan miyabad va megdar x ra be TRUE update mikonad
                                    break
                        else:
                            print("!!! field shomare card ro khali nagozarid !!!")                   #agar shart khali nabidan field raayat nashavd be meno aval yani func show() ejra mishavad
                            self.show()

                    if (x == True):                     #chon dar halge for shomare card ra az db peyda kard va shart bargarar shod megdar x be true update shod dar inja az in motagayer be onvan BREAK estafede mikonim baraye payan halge
                        break
                    else:                               #agar megdar x tagir nakard yani shart haye halge for bargara nabod ba pegam shpmare card ehstebah hast movajeh  mishavim va halge edame darad
                        print("!!! shomare card eshtebah hast !!!")
                y=False                                 #yek motager be nam y ba megdar False darim
                while True:                             # dar in hakge ham dagigan ba halge bala yaftan shomare kart yeki hast
                    darkhast_password=input("password khod ra vared konid:\n---> ")
                    for i in range(len(self.db)) :         
                        if darkhast_password != "":
                            if len(darkhast_password)==4:            #ba in tafavot dar dakhel for alave bar password ba shomare kart niz tadabog (tatabog) midahand
                                if darkhast_password == self.db["p"+str(i)]["account"]["password"] and darkhast_card_number == self.db["p"+str(i)]["account"]["card_number"] :
                                    y=True
                                    break
                        else:
                            print("!!! field password ro khali nagozarid !!!")
                            self.show()
                    if (y == True):                                #agar for payan yaft va shart ha bargar bod megdar y be true update shode va halge while ham break mishavad ve be meno khadamat yani func meno_khadamt ejra mishavad
                        print("|------lotfan khadamat mored niyaz khodra entekhab konid-----|")
                        self.meno_khadamat()
                        break
    
                    else:                                          #agar dar for shart ha bargarar nasho va ba peygam password eshtebah ast chap mikonim va halge while edame darad
                        print("!!! password ehstebah hast !!!")

    def meno_khadamat(self):    #function meno_khadamt safheye khadamt hast ke function haye mokhtalefi dakhelesh ejra mishavand
        try:           #func dar dakhel try except neveshte shode ta dar movageh erorr dobare func meno_khadamt ejra shavad
            print(f"""#--------------------------{self.karbar["account"]["fname"]} {self.karbar["account"]["lname"]}---------------------#""")     #nam va nam khanevage saheb kart ra dar balaye meno chap mikonad
            print("1.tagir etelaat")                          #meno va rahnoma meno_khadamt chap mishavad
            print("2.mojodi")
            print("3.card be card")
            print("4.mosbage ba atm")
            print("5.bazgasht be sfhaye vorod")
            print("6.exit")
            while True:                                     #dar yek halge shomare khadamati ke moshatri mikhahad ra daryatft mikonim
                shomare_khadamat=int(input("|------shomare khadamat mord nazar vared konid---------------|\n---> "))  #shomare khadamt ra az karbar daryeft mikonim 
                if len(str(shomare_khadamat)) == 1 :                                          #shart haye 1 ragami va dar bazeye 0 - 7 bodabesh ra barresi mikonim 
                    if 0 < shomare_khadamat < 7:
                        break                                                                 #dar sorat bargar bodan shart ha halge while break mishavad
                    else:
                        print("lotfan yeki az adad haye khadamat ra entekhab konid")          #agar shart ha bargarar nabashad be karbar payam ELSE chap va halge edame peyda mikonad
                else:
                    print("lotfan yeki az adad haye khadamat ra entekhab konid")
            if shomare_khadamat == 1:                                                         #pas az anke etminam hasel kardim adad daryafti az karbar be dard ma mikhorad tebge on adadad func hayi ejra mishadvad
                self.tagir_etelaat()
            if shomare_khadamat == 2:
                self.mojodi()
            if shomare_khadamat == 3:
                self.card_be_card()
            if shomare_khadamat == 4:
                self.mosabge()
            if shomare_khadamat == 5:
                self.show()
        except:
            print("type:restart_menokhadamat : !!!! dar entekhab shomare amaliyat degat konid !!!!")                    
            self.meno_khadamat()
    
        if shomare_khadamat == 6:                                                            # chon func exit dar try expet be moshkel bar mikharaad kharej az an neveshte shode             
            self.exit()

    def tagir_etelaat(self):   #functio tagir etelaat menno tagir etelat ra miyavarad
        
        print(f"""----------- {self.karbar["account"]["fname"]} {self.karbar["account"]["lname"]}--------|""")    #ebtadaye meno fname va lname moshtari chap mishavad
        print("1.tagir password")
        print("2.meno khadamat")
        print("3.exit")                                                            #meno khadamat haye gabel erye chap mishavad
        try:
            while True:
                khadamat_tagir=int(input("----shomare khadamat mored nazar khod ra vared konid----------|\n---> "))    #ba estefade az halge while adad daryafti az karbar barresi mishavad
                if len(str(khadamat_tagir)) == 1 :
                    if 0 < khadamat_tagir < 3:
                        break
                        
                    else:
                        print("az meno adad khadamat khod ra entekhab konid ")
                else:
                    print("az meno adad khadamat khod ra entekhab konid ")
            if khadamat_tagir == 2:
                self.meno_khadamat()
            if khadamat_tagir == 3:
                self.exit()
            if khadamat_tagir == 1:                                                        #adad daryefti az khadamat_tagir tebge meno ejra mishavad
                while True:
                    old_pass=int(input("remaz gabli khodra vared konid\n---> "))
                    if len(str(old_pass))==4:
                        if str(old_pass) == self.karbar["account"]["password"]:            #self.karbar dar inja haman key db hast ke karbar ba an vared system shode
                            break                                                           #old pass karbar ham gerefte mishavd ta dar tagir ramz az ramz gabli khod estefade nakonad
                        else:
                            print("ramz ehstebah hast")
                    else:
                        print("ramz eshtebah hast")
                while True:
                    new_pass=input("ramz jadid ra vared konid\n---> ")                      #new pass ra az karbar daryeft karde ba barresi shart ha db ra update mikonad
                    if new_pass != "" :
                        if len(str(new_pass))==4:
                            new_pass2=input("ramz jadid khod ra dobare vared konid\n---> ")
                            if new_pass == new_pass2:                                       #jahat etmminan 2 bar new pass ra az karbar gerefte va barresi mikonim ke aya yeki hastan ya na
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
                                                                  #bad etmama amaliyat tagir ramz va break shodan halge pegam ramz tagir yaf chap mishavad be meno khadamat baz migardim 
        except:
            print("type:restart_tagir_etelaat :!!!!!!!!!! lotfan dar vared kardan adad degat konid !!!!!!!!!!")
            self.tagir_etelaat()

    def exit(self):  #function exit har vagt ejra shavad barname stop va tamam mishavad
        print("  ^^    az in ke BAANK BALLUK ro targih dadid mamnonim   ( ͡⚆ ͜ʖ ͡⚆)  ")
        os._exit(0)        #az ketbkhane os estefade shode

    def mojodi(self):        #function mojodi mojodi ra az db estekhraj va namayesh midahad
        """dont look at me -_-"""
        print(f"""|------------------- {self.karbar["account"]["fname"]} {self.karbar["account"]["lname"]}------------------------- --|""")
        mojodi=self.karbar["account"]["balance"]
        print(f"""
        
                        ╭┻━-━━┻╮
                         ┃╭╮╭╮ ┃
                        ╭┫▕▎▕▎┣╮
                        ╰┓┳╰╯┳┏╯ mojodi shoma
                        ╭┛╰━━╯┗━━━╮
                        ┃┃    ┏━╭╰╯╮
                        ┃┃    ┃┏┻━━┻┓
                        ╰┫ ╭╮ ┃┃ {mojodi}  $$$$
                         ┃ ┃┃ ┃╰━━━━╯
                        ╭┛ ┃┃ ┗-╮
        """)
        print("1.bazgasht be meno khadamat")
        print("2.exit")
        try:
            while True:                            #dar inja bad chap mojodi karbar ra baraye edame amaliyat rahnomayi mikonim 
                gozine=int(input("gozine mored nazar khodra entekhab konid\n---> "))
                if len(str(gozine)) ==1 :
                    if 0 < int(gozine) < 3:
                        break                                             
                    else:
                        print("lotafan az adad gozine haye meno entekhab konid")
                else:
                    print("lotafan az adad gozine haye meno entekhab konid")
            match gozine:
                case 1:                             #bad bargarari shart ha be safheye haye marbote yani func haye marbote ro ejra mikonim 
                    self.meno_khadamat()
                case 2:
                    self.exit()
        except:
            print("type:restart_mojodi :!!!!!!!!!! lotfan dar vared kardan adad degat konid !!!!!!!!!!")
            self.mojodi()

    def card_be_card(self):   #function card be card dar entegal mablag estefade mishavad
        print("*-------------be safheye card be card bank balluk khosh amadid-----------*")
        print("1.meno khadamat")
        print("2.start Money transfer")
        print("3.mojodi")
        print("4.exit")
        try:
            while True:                            #dar inja bad chap meno card be card karbar ra baraye edame amaliyat rahnomayi mikonim 
                gozine_card_be_card=int(input("gozine mored nazar khodra entekhab konid\n---> ")) 
                if len(str(gozine_card_be_card)) ==1 :
                    if 0 < int(gozine_card_be_card) < 5:
                        break                                             
                    else:
                        print("lotafan az adad gozine haye meno entekhab konid")
                else:
                    print("lotafan az adad gozine haye meno entekhab konid")
            match gozine_card_be_card:
                case 1:                             #bad bargarari shart ha be safheye haye marbote yani func haye marbote ro ejra mikonim 
                    self.meno_khadamat()
                case 3:
                    self.mojodi()
                case 4:
                    self.exit()
                case 2:
                    x = False                #tozihat in code dar func show dade shode
                    while True:
                        magsad_card_be_card_number=input("shomare card magsad ra vared konid:\n---> ")               
                        for i in range(len(self.db)) :                                                  
                            if magsad_card_be_card_number != "" :                                             
                                if len(magsad_card_be_card_number)==16:                                         
                                    if magsad_card_be_card_number == self.db["p"+str(i)]["account"]["card_number"]:
                                        magsad_karbar=self.db["p"+str(i)]
                                        x =True                                                          
                                        break
                            else:
                                print("!!! field shomare card ro khali nagozarid !!!")
                                self.card_be_card()                   

                        if (x == True):                     
                            break
                        else:                               
                            print("!!! shomare card ehstebah hast !!!")
                    while True:
                        mablag_entegali=input("*------$ mablagi entagli ra vared konid $\n---> $ ")
                        if mablag_entegali != "":
                            if int(mablag_entegali) <= int(self.karbar["account"]["balance"]):
                                print(f"""$$$ mablag entegali {mablag_entegali}\n\n shomare card magsad {magsad_card_be_card_number}\n\nsaheb shomare card {magsad_karbar["account"]["fname"]} {magsad_karbar["account"]["lname"]} """)
                                while True:
                                    print()
                                    print("1.bale edame midaham")
                                    print("2.lagv amaliyat")
                                    soal_etebar_sanji=input("\n|-----aya mikhahid amaliyat ra kamle konid ? ")
                                    #az match baraye edame ya lagv amaliyat estefade kardim 
                                    if soal_etebar_sanji != "":
                                        if len(soal_etebar_sanji) == 1:
                                            if 0 < int(soal_etebar_sanji) < 3:
                                                break
                                            else:
                                                print("!!! az beyn gozine ha entekhab konid !!!")
                                        else:
                                            print("!!! az adad tak ragami estefade konid !!!")
                                    else:
                                        print("!!! field ra khali nagozarid !!!")
                                match soal_etebar_sanji :
                                    case "1":
                                        amaliyt=(int(self.karbar["account"]["balance"])-int(mablag_entegali))
                                        self.karbar["account"]["balance"]=str(amaliyt)
                                        #chon dar db str balance save shode str be db ezafe mikonim 
                                        #self.karbar ra az func show dar etebar sanji shomare car bardashtim
                                        amaliyt_2=(int(magsad_karbar["account"]["balance"])+int(mablag_entegali))
                                        magsad_karbar["account"]["balance"]=str(amaliyt_2)
                                        print("$$$ entegal mofagiyat amiz bod $$$")
                                        self.card_be_card()
                                        break
                                    case "2":
                                        print("!!! amaliya lagve shod !!!")
                                        self.card_be_card()
                            else:
                                print("$$$ mablag entegali az mojodi shoma bishtar ast $$$")
                                self.card_be_card()
                        else:
                            print("^^^ lotfan ragam mored nazar ra vared konid ^^^^")
        except:
            print("type:restart_card_be_card :!!!!!!!!!! lotfan dar vared kardan adad degat konid va fagat adad vared konid !!!!!!!!!!")
            self.card_be_card()

    def mosabge(self):      #function mosabage yek mosabege koshak ba adad hast baraye sargarmi tarrahi shode
        """faliyat 6 ostad"""
        try:
            emtiyaz_user=0
            emtiyaz_pc=0
            i=1
            # i baraye halge hsat ke mosabage 5 bar tekrar shavad i = 1 hast dar halge i+=1 mishavad
            pc_adad=""
            user_adad=""
            #dar akhar tamam adad entekhabi dar in motagey ha jam mishavad
            print("1.shoro mosabage :)")
            print("2.meno khadamat")
            print("3.exit")
            while True:                                     #dar yek halge shomare khadamati ke moshatri mikhahad ra daryatft mikonim
                shomare_khadamat_mosabege=int(input("|------shomare khadamat mord nazar vared konid---------------|\n---> "))  #shomare khadamt ra az karbar daryeft mikonim 
                if len(str(shomare_khadamat_mosabege)) == 1 :                                          #shart haye 1 ragami va dar bazeye 0 - 4 bodabesh ra barresi mikonim 
                    if 0 < shomare_khadamat_mosabege < 4:
                        break                                                                 #dar sorat bargar bodan shart ha halge while break mishavad
                    else:
                        print("lotfan yeki az adad haye khadamat ra entekhab konid")          #agar shart ha bargarar nabashad be karbar payam ELSE chap va halge edame peyda mikonad
                else:
                    print("lotfan yeki az adad haye khadamat ra entekhab konid")
            match shomare_khadamat_mosabege:
                case 2:
                    self.meno_khadamat()
                case 3:
                    self.exit()
                case 1:
                    print("|----------be mosabege ba ATM (pc) khosh amadid-----------|")
                    print("|----------mosabage 5 marhale khahad dasht----------------|")
                    print("|-yek adad shoma az 0-20 etnetekhab mikonid va yek adad ATM-|")
                    print("|----adad har ki bozorg tar bashad '1' emtiyaz migirad----|")
                    print("|-agar adad ha mosavi bashad har do taraf '1' emtiyaz daryaft mikonad-|")
                    print("|----------barande dar akhar malom mishavad---------------|")
                    print("|-va dar akhar har marhale va payan mosabege adad haye entekhabi ra khahid did-|")
                    print("|------------jahat sargarmi hastesh enjoy it--------------|\n")
                    while (i <= 5) :
                        while True:
                            #in halge baraye entekhab adad 0-20 tarahi shode ta mosabge baraye har dalili stop nashavad
                            #va khod in halge 5 bar tekrar mishavad
                            adad_pc=random.randint(0,20)
                            adad_karbar =int(input("yek adad beyn 0 ta 20: ")) 
                            pc_adad+=(str(adad_pc)+",")
                            user_adad+=(str(adad_karbar)+",")
                            if (20 >= adad_karbar >= 0) :
                                break
                            else:
                                print("adad beyn 0 - 20 entekhab konid")
                        print(f"adad pc = {adad_pc}")
                        if adad_pc < adad_karbar :
                            print(f""" {self.karbar["account"]["fname"]} {self.karbar["account"]["lname"]} ( ͡⚆ ͜ʖ ͡⚆)╭∩╮ - - - - - - - - - - - - - - - -- - - - - -- -  ATM  """)
                            emtiyaz_user += 1
                        elif adad_pc == adad_karbar :
                            print(f""" {self.karbar["account"]["fname"]} {self.karbar["account"]["lname"]} ( ͡⚆ ͜ʖ ͡⚆)╭∩╮ - - - - - - - - - - - -  - - - - -╭∩╮( ͡⚆ ͜ʖ ͡⚆) ATM  """)
                            emtiyaz_user += 1
                            emtiyaz_pc += 1
                        else :
                            print(f""" {self.karbar["account"]["fname"]} {self.karbar["account"]["lname"]}  - - - - - - - - - -- - - - --  - - - - - - - -╭∩╮( ͡⚆ ͜ʖ ͡⚆) ATM  """)
                            emtiyaz_pc += 1
                        i+=1

                    if emtiyaz_pc > emtiyaz_user :
                        print("*******pc barande hast*********")
                    elif emtiyaz_pc < emtiyaz_user:
                        print("*******user barande hast*******")
                    else:
                        print("++++++++mosavi shodid++++++++++")

                    print(f"user={user_adad} , pc={pc_adad}")

                    print(f"""emtiyaz pc = {emtiyaz_pc} emtiyaz user = {emtiyaz_user}""")
                    
                    self.mosabge()
        except:
            print("type:restart_mosabage lotfan az adad khaste shode entekhab konid")
            self.mosabge()

    def help(self):          #function for HELP
        print(" :) ba salam be ATM BALLUK khosh omadin. ")
        print()
        print(" :) kar kardan ba in ATM kheyli rahat hast. ")
        print()
        print(" :) be rahnomyi haye aval har safhe degat konid. ")
        print()
        print(" :) az gozine va adad khaste shode estefade va vared konid. ")
        print()
        print(" :) kafist ta jayi ke khaste shode az horof alafbe a-z estefade nakonid.")
        print()
        print(" :) field hara aslan khali nagozarid por konid hata be eshtebah :)))")
        print()
        print(" :) fagat dar mavaredi ke az shoma khaste shode masalan dar safhye ozviyat nam va nam khanevadegi. ")
        print()
        print(" :) az horof alafba fagat baraye kharej shodan az tedadi marahel mahdod mesl:\n\n :) vasat amaliyat tagir password az horof alafba baraye restart kardan amaliyat va bazgasht be meno estefade konid")
        print()
        print(" :) albate har nazar, entegad, pishnahad dashtid rah haye ertebat ba man dar aval atm chap shode\n\n :) mitavanid dar miyan begozarid.")
        print()
        print(" :) nokte akhar az zendegi lezat bebarin")
        print()
        self.show()
Balluk_atm=ATM()
Balluk_atm.show()