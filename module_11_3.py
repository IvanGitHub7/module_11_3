import requests
import inspect

from pprint import pprint
class My_class():
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        
    def function_object(int_1, int_2, int_3):
            if int_1 == 0 and int_2 ** int_3 == 0 or int_2 == int_3 == 0:
                return 'Нельзя возводить ноль в нулевую степень'
            else:
                return int_1 ** int_2 ** int_3
            
object = My_class('Я объект класса My_class')


def introspection_info(obj):
    #Тип объекта:
    type_object = type(obj).__name__
    #Атрибуты объекта:
    attr_object = list(vars(obj).keys())
    #Методы объекта:
    methods_object = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]
    #Специальные метода объекта:
    special_methods_object = [s_method for s_method in dir(obj) if s_method.startswith('__')]
    #Модуль объекта:
    module_object = object.__module__
    #Упаковываем полученные значения в словарь:
    return {'type':type_object, 'attributes':attr_object, 'methods':methods_object, 'special methods':special_methods_object, 'module':module_object}

print(introspection_info(object))