from abc import ABC, abstractmethod
from datetime import  datetime

class Product(ABC):

    @abstractmethod
    def add1(self, shop):
        pass

    @abstractmethod
    def add2(self, shop):
        pass

    @abstractmethod
    def notify1(self):
        pass

    @abstractmethod
    def notify2(self):
        pass

class ConcreteProduct(Product):

    def __init__(self, price, price1):
        self._pr_price = price
        self._pr_price1 = price1


    shops = []
    shops1 =[]

    def add1(self, shop):
        self.shops.append(shop)

    def add2(self, shop):
        self.shops1.append(shop)

    def notify1(self):
        now = datetime.today()
        today = now.strftime("%d.%m.%Y")
        print(f'Date: {today}')
        for shop in self.shops:
            shop.update(self)
        print('---------------------------------------')

    def notify2(self):
        now = datetime.today()
        today = now.strftime("%d.%m.%Y")
        print(f'Date: {today}')
        for shop in self.shops1:
            shop.update1(self)
        print('---------------------------------------')

    @property
    def pr_price(self):
        return self._pr_price

    @property
    def pr_price1(self):
        return self._pr_price1

    @pr_price.setter
    def pr_price(self, price):
        self._pr_price = price
        self.notify1()

    @pr_price1.setter
    def pr_price1(self, price1):
        self._pr_price1 = price1
        self.notify2()




class ShopObserver(ABC):

    @abstractmethod
    def update(self, product):
        pass

    @abstractmethod
    def update1(self, product):
        pass


class Shops(ShopObserver):

    def __init__(self, shop_name: str):
        self._shop_name = shop_name

    def update(self, product: ConcreteProduct):
        print("Price of cheese up to ", pr.pr_price, 'uah in ', self._shop_name)

    def update1(self, product: ConcreteProduct):
        print("Price of cheese up to ", pr.pr_price1, 'uah in ', self._shop_name)

pr = ConcreteProduct(10,15)

pr.add1(Shops('ATB'))
pr.add1(Shops('Tavria V'))

pr.add2(Shops('Silpo'))
pr.add2(Shops('Gippo'))


pr.pr_price = 22
pr.pr_price1 = 23.50


