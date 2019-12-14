class Bank:
    Bank_name="ICICI"
    ROI=14
    MBL="mumbai"

    def __init__(self,Name,Age,Phno,Email,Bal=0):
        self.Name=Name
        self.Age=Age
        self.Phno=Phno
        self.Email=Email
        self.Bal=Bal

    def deposit(self,amt=0):
        if amt==0:
            amount=self.get_amount()
        self.Bal+=amt
        self.success()

    def withdraw(self,amt=0):
        if amt==0:
            amt=self.get_amount()
        if amt>self.Bal:
            self.failure()
            print("Insufficient funds")
            return
        self.Bal=self.sub(self.Bal,amt)
        self.success()

    def display(self):
        print(self.Name,self.Age,self.Phno,self.Email,self.Bal)

    def modify(self,Name=" ",Age=0,Phno=0,Email=" "):
        if Name!=" ":
            self.Name=Name
        if Age!=0:
            self.Age=Age
        if Phno!=0:
            self.Phno=Phno
        if Email!=" ":
            self.Email=Email
            self.success()
    @classmethod
    def change_Bname(cls,new=" "):
        if new==" ":
            cls.Bank_name=new
            cls.success()
    @classmethod
    def modify_ROI(cls,new=0):
        if new==0:
            new=cls.get_ROI()
        cls.ROI=new
        cls.success()

    @staticmethod
    def get_ROI():
        new=float(input("Enter the new ROI"))
        return new

    @staticmethod
    def sub(a,b):
        return a-b

    @staticmethod
    def failure():
        print("Transaction failure")

    @staticmethod
    def success():
        print("Transaction successfully")

    @staticmethod
    def get_amount():
        amount=int(input("Enter the amount"))
        return amount


class Bank2(Bank):
    def __init__(self, Name,Age,Phno,Email,pan,aadhar,Bal=0):
        super(Bank2,self).__init__(Name,Age,Phno,Email,Bal=0)
        self.pan = pan
        self.aadhar = aadhar

    def add_aadhar_pan(self, pan, aadhar):
        self.pan = pan
        self.aadhar = aadhar

    def display(self):
        print(self.Name,self.Age,self.Phno,self.Email,self.Bal,self.aadhar, self.pan)

Reeta=Bank("Reeta",25,9847800173,"reeta@geeta.com",20000)
# Bank.modify_ROI()
# Reeta.display()
# Reeta.withdraw()
# Bank.display(Reeta)
# Bank.withdraw(Reeta,1000)
Bank2.add_aadhar_pan(Reeta,"jdhgkjsd",234)
print(Reeta.aadhar)
print(Reeta.pan)
Ram = Bank2("Ram", 29, 456, "kjsdhk", 6549,"kjdfhsl")
Ram.display()
