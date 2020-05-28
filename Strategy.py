import abc

class AbstractStrategy(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def listdefining(self):
        pass

class FirstStrategy(AbstractStrategy):
    def listdefining(self):
        print ("It is father list:")

class SecondStrategy(AbstractStrategy):
    def listdefining(self):
        print('It is mother list: ')

class ThirdStrategy(AbstractStrategy):
    def listdefining(self):
        print('It is your custom list:')

class LightStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def list(self):
        pass


class FList(LightStrategyAbstract):
    def flist(self):
        print ("Meat, Cheese, Snacks, Beer")

first_strategy = FirstStrategy()
second_strategy = SecondStrategy()
third_strategy = ThirdStrategy()
FL = FList()


class List(object):
    def __init__(self, first_strategy, light_strategy):
        self._first_strategy = first_strategy
        self._light_strategy = light_strategy

    def listdefining(self):
        self._first_strategy.listdefining()

    def flist(self):
        self._light_strategy.flist()


class MyCustomList(List):
    def __init__(self):
        super(MyCustomList, self).__init__(third_strategy, None)

    def mlist(self):
        input("Select products: ")

class MotherList(List):
    def __init__(self):
        super(MotherList, self).__init__(second_strategy, None)

    def mlist(self):
        print ("Apples, Juice, Fish")

class FatherList(List):
    def __init__(self):
        super(FatherList, self).__init__(first_strategy, FL)


fl = FatherList()
fl.listdefining()
fl.flist()
print('---------')

ml = MotherList()
ml.listdefining()
ml.mlist()
print('---------')

cl = MyCustomList()
cl.listdefining()
cl.mlist()
