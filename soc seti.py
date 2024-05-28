class User:
    def __init__(self, name, mail, age, phonenumber):
        self.name=name
        self.mail=mail
        self.age=age
        self.phonenumber=phonenumber
    def changeusername(self,change):
        self.name=change
        print('new name')
    def changenumber(self,number):
        self.phonenumber=number
    def changemail(self, newmail):
        self.mail=newmail

