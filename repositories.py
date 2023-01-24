from Bank_Users.models import User
from typing import List, Optional

users: List[User] = []
class UserRepository:
    def createUser(self, name: str, surname: str, password: str) -> None:
        users.append(User(name, surname, password))
        print("Added to the Database")
    def getUser(self, name: str,surname: str, password: str) -> Optional[User]:
        for i in range(len(users)):
            if users[i].name == name and users[i].surname == surname and users[i].password == password:
                return users[i]
        print(f'There is no such User')
        return None

    def checkUser(self, name: str, surname: str) -> Optional[User]:
        for i in range(len(users)):
            if users[i].name == name and users[i].surname == surname:
                return users[i]

        print(f'There is no User with the fullname {name} {surname}')
        return None

    def sendBankAccount(self, name: str, surname: str, sender: User, money: int) -> None:
        getter = self.checkUser(name, surname)
        if getter != None and sender.subtractBankAccount(money):
            if getter.curs != sender.curs:
                money = getter.getCurs(sender.curs, money)
            getter.addBankAccount(money)
            print("Successfully Send !!!")

