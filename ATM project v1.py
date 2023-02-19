import os 
os.system("cls")


class ATM:
    def __init__(self):
        self.db={

    "p1":{"account":{"card_number":"0000000000000000","cvv2":"1234","password":"1234","Exp":"00/00","esm":"shohra","shaba":"000","balance":"10000"} 
    
}
}

    def test(self):
        self.db["p1"]["account"]["password"]="1234"
        return self.db


a=ATM

print(a.test())