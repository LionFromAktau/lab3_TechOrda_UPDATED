import random
from Account import Account
class User:
    name: str
    surname: str
    password: str
    pocket: int
    curs: int
    _curses = ['USD', 'RUB', 'KZT', 'EUR']
    def __init__(self, name:str, surname:str, password:str):
        self.name = name
        self.surname = surname
        self.password = password
        self.curs = 0
        self.pocket = 0
        print('\nWellcome to our bank\n')
        print(self)

    def __repr__(self) -> str:
        return f'Owner: {self.name} {self.surname}.\nMoney in pocket: {self.getPocket()}.'

    def getPocket(self) -> int:
        return "You have " + "{:.2f}".format(self.pocket) + " in " + self._curses[self.curs]

    def addBankAccount(self, money: int) -> None:
        self.pocket += money
        print(f'Dear {self.name} {self.surname}, {money} {self._curses[self.curs]} was added to your Bank Account')

    def subtractBankAccount(self, money:int) -> bool:
        if(money > self.pocket):
            print('Not enough money !!!')
            return False
        self.pocket -= money
        print(f'Dear {self.name} {self.surname}, {money} {self._curses[self.curs]} was taken from your Bank Account')
        return True

    def setCurs(self, curs: int) -> None:
        self.__convert(curs)

    def convert(self) -> None:
        choose = -1
        while (choose != 0):
            print('0. Exit')
            print('1. To USD')
            print('2. To RUB')
            print('3. To KZT')
            print('4. To EUR')
            choose = int(input('Your choice: '))
            if choose > 4:
                print('Please write an appropriate number!!!')
            else:
                self.__convert(choose - 1)
                print(self.getPocket())
                break

    def __convert(self, newCurs: int) -> None:
        money = Account.USD.value
        for j in Account:
            if self._curses[self.curs] == j.name:
                money = j.value
                break
        print(f'\nFrom {self._curses[self.curs]} to {self._curses[newCurs]}')
        self.curs = newCurs
        print(f'\nNew curs money {money[newCurs]}')
        self.pocket *= money[newCurs]

    def getCurs(self, newCurs: int, moneyS: int) -> int:
        money = Account.USD.value
        for j in Account:
            if self._curses[newCurs] == j.name:
                money = j.value
                break
        return moneyS * money[self.curs]