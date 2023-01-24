import sys

from Bank_Users.models import User
from Bank_Users.repositories import UserRepository
from Bank_Users.services import ServiceUser

us = UserRepository()
userService = ServiceUser(us)
def userInterface(user: User):
    while True:
        print("0. Exit")
        print('1. Add Money')
        print('2. Get Money')
        print('3. Send Money')
        print('4. Convert Money')
        print('5. Get Info')
        choose = int(input("Your action: "))
        if choose == 0:
            break
        elif choose == 1:
            user.addBankAccount(int(input("Write the amount: ")))
        elif choose == 2:
            user.subtractBankAccount(int(input("Write the amount: ")))
        elif choose == 3:
            print('Fill the data related to the person that you want to send')
            name = input("Name: ")
            surname = input("Surname: ")
            amount = int(input("Amount: "))
            userService.sendBankAccount(name, surname, user, amount)
        elif choose == 4:
            user.convert()
        elif choose == 5:
            print(user)


def init():
    while True:
        print('0. Exit')
        print('1. Create an Account')
        print('2. Sign in')

        choose = int(input('Your Action: '))
        if choose == 0:
            sys.exit(0)
        elif choose == 1 or choose == 2:
            name = input("Write name: ")
            surname = input("Write surname: ")
            password = input("Write password: ")
            user = None
            if choose == 1:
                userService.createUser(name, surname, password)
            else:
                user = userService.getUser(name, surname, password)
            if user != None:
                userInterface(user)





if __name__ == '__main__':
    init()