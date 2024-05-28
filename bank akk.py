class BankAccaunt:
    def __init__(self,name, amount=0):
        self.name=name
        self.amount=amount
    def deposit(self,amount):
        self.amount+=amount
        print('den"gi uspeshno dobavleni')
    def cash(self,amount):
        if self.balance>= amount:
            self.balance-= amount
            print('dengi snyati')
        else:
            print('nedostatochno')
    def mybalance(self):
        print(f'deneg na balance:{self.balance}')
user1=BankAccaunt('botir')
while True:
    menu=input('sto vi hotite sdelat:\n'
                '1-posmotret balance \n'
                '2-poplnit schet \n'
                '3-snyat dengi\n'
                'deystvie:')
    if menu=='1':
        user1.mybalance()
    elif menu == '2':
        amount=float(input('vvedite summu:'))
        user1.deposit(amount)
    elif menu == '3':
        amount=float(input('vvedite summu dlya snyatiya'))
        user1.cash(amount)
    else:
        print('nepravilnoe deystvie')

