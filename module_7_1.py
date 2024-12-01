# Домашнее задание по теме "Режимы открытия файлов"
from pprint import pprint
from xml.sax.handler import property_interning_dict

def prod(file_name):
    str_prod = []
    file = open(file_name, 'r')
    for line in file:
        str_prod.append(line.strip())
        # В этом примере для каждой строки в файле вызывается метод strip(),
        # который удаляет символ новой строки в конце строки. В результате
        # переменная line будет содержать список строк из файла,
        # но уже без символа новой строки.
        # Метод .strip() удаляет пробельные символы как в начале, так и в конце строки, включая символы новой строки (\n).
    return str_prod


class Product:

    def __init__(self, name, weight, category):
        self.name = name            # название продукта (строка)
        self.weight = weight        # общий вес товара (дробное число)
        self.category = category    # категория товара (строка)

    def __str__(self):
        return f'{self.name} {self.weight} {self.category}' # <название>, <вес>, <категория>


class Shop:
    __file_name = 'products.txt'
    # Если файла нет, то я его создам
    file = open(__file_name, 'a+')
    file.close()


    def get_products(self):
        # В условии задания написано - "возвращает единую строку со всеми товарами из файла"
        c = ', '.join(prod(self.__file_name))
        return c

    def add(self, *products):
        str_prod = prod(self.__file_name)

        for product in products:
            if str_prod.count(str(product)):
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(str(product) + '\n')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())