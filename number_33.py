class MyList:

    def __init__(self, name):
        self.name = name
        self.type = []
        pass

    def return_sum(self):
        """
        Возвращает сумму всех элементов сохраненного листа.
        Пользоваться sum нельзя!
        """
        summa = 0
        for i in range(len(self.name)):
            summa = summa + self.name[i]
        return summa
        pass

    def make_reverse(self):
        """
        Разворачивает сохраненный лист.
        """
        return list(reversed(self.name))
        pass

    def make_slice(self, start, stop):
        """
        Делает слайсинг сохраненного листа.
        """
        return self.name[start:stop]
        pass


a = MyList([1, 2, 3, 4])
assert a.return_sum() == 10
assert a.make_reverse() == [4, 3, 2, 1]
assert a.make_slice(0, 2) == [1, 2]

b = MyList([5, 6, 6, 5])
assert b.return_sum() == 22
assert b.make_reverse() == [5, 6, 6, 5]
assert b.make_slice(1, 2) == [6]