
# Создаем функцию для интроспекции объекта
def introspection_info(obj):
    """Проводит интроспекцию объекта и возвращает информацию о нем."""
    info = {
        'type': type(obj).__name__,  # Тип объекта
        'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')],  # Атрибуты объекта
        'methods': [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')],  # Методы объекта
        'module': getattr(obj, '__module__', 'Builtin'),  # Модуль объекта
    }
    
    # Добавим дополнительные свойства, если объект — это пользовательский класс
    if hasattr(obj, '__dict__'):
        info['custom_attributes'] = obj.__dict__
    
    return info

# Пример использования с встроенным типом
number_info = introspection_info(42)
print("Информация о числе:", number_info)

# Создаем пользовательский класс для примера
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, {self.name}!"

    def is_adult(self):
        return self.age >= 18

# Создаем объект пользовательского класса
my_object = MyClass(name="Alice", age=30)

# Применяем интроспекцию к пользовательскому объекту
custom_object_info = introspection_info(my_object)
print("Информация о пользовательском объекте:", custom_object_info)
