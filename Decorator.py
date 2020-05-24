import six
from abc import ABCMeta


@six.add_metaclass(ABCMeta)
class AbstractList(object):

    def get_products(self):
        return  str()

class MyList(AbstractList):

    def get_products(self):
        return str('My products list: Pepsi, Chocolate')



@six.add_metaclass(ABCMeta)
class Abstract_List_Decorator(AbstractList):

    def __init__(self, decorated_list):
        self.decorated_list = decorated_list


    def get_products(self):
        return self.decorated_list.get_products()


class Mothers_List(Abstract_List_Decorator):

    def __init__(self, decorated_list):
        Abstract_List_Decorator.__init__(self, decorated_list)


    def get_products(self):
        return self.decorated_list.get_products() + ', Meat, Milk, Cheese'

class Father_List(Abstract_List_Decorator):

    def __init__(self, decorated_list):
        Abstract_List_Decorator.__init__(self, decorated_list)

    def get_products(self):
        return self.decorated_list.get_products() + 'Potatoes, Carrot, Snacks'



l0 = AbstractList()
l = MyList()
l1 = Mothers_List(l)
l2 = Father_List(l0)
print('Mother will buy products for me, because I am so lazy :))')
print('Mother List: ' + l1.get_products())
print('-------------------')
print('But father do not want to buy products for me :(')
print('Father List: ' + l2.get_products())