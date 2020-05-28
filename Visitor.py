from __future__ import generators
import random


class Buyer(object):
    def accept(self, visitor):
        visitor.visit(self)
    def buy(self, buyer):
        print(self, 'will be buy by', buyer)
    def not_buy(self, nbuyer):
        print(self, 'will not be buy by', nbuyer, 'Because he do not need this product')
    def __str__(self):
        return self.__class__.__name__

class Cheese(Buyer): pass
class Meat(Buyer): pass
class Snacks(Buyer): pass

class Visitor:
    def __str__(self):
        return self.__class__.__name__

class People(Visitor): pass
class PBuyer(People): pass
class PNBuyer(People): pass


class Alex(PBuyer):
    def visit(self, product):
        product.buy(self)


class Yuri(PNBuyer):
    def visit(self, product):
        product.not_buy(self)

def productGenerator(n):
    pr = Buyer.__subclasses__()
    for i in range(n):
        yield random.choice(pr)()


alex = Alex()
y = Yuri()
for product in productGenerator(2):
    product.accept(alex)
    product.accept(y)