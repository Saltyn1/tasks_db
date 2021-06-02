"""
1)Создайте класс и объявите в нём 3 метода: публичный, защищённый и приватный. Затем создайте экземпляр данного класса и вызовите по очереди каждый из методов.
"""
class Website:
      
    def to_open(self):
        return 'www.google.com'

    def _get_email (self):
        return "Limited access"

    def __get_email(self):
        return "Error"

website = Website()
print(website.to_open())
print(website._get_email())
print(website.__get_email())


"""
2)Определите класс A, в нём объявите метод method1, который печатает строку "Hello World". Затем создайте класс B, который будет наследоваться от класса A. Создайте экземпляр от класса B, и через него вызовите метод method1.
"""
class A:
  def method1(self):
    print('Hello World')

class B(A):
  pass
b = B()
b.method1()




"""
3)Объявите класс Car, в котором будет приватный атрибут экземпляра speed. Затем определите метод set_speed, который будет устанавливать значение скорости и метод show_speed, с помощью которого Вы будете получать значение скорости.
"""
class Car:
    
    __speed = 50

    def set_speed(self, value):
        self.__speed = value

    def show_speed(self):
        return self.__speed
    
       
car = Car()
print(car.show_speed())

"""
4)Перепишите класс Car из предыдущего задания.
Перепишите метод set_speed() с использование декоратора @speed.setter, а метод show_speed() с использованием декоратора @property, для того чтобы можно было работать с данным классом следующим образом:

car = Car()
car.speed = 120
print(car.speed)


"""
class Car:
    
    __speed = 50

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

        
car = Car()
car.speed = 120
print(car.speed)