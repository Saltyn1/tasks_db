"""Создайте класс Auto в нем реализуйте метод ride который выводит сообщение Riding on a ground, создайте класс Boat реализуйте метод swim, который выводит floating on water.
Создайте класс Amphibian который наследуется от класса Auto и Boat. Создайте от него объект и вызовите все методы.
# """
class Auto:
  def ride(self):
    print('Riding on a ground')

class Boat:
  def swim(self):
    print('floating on water')

class Amphibian(Auto, Boat):
  pass

auto = Amphibian()
boat = Amphibian()
boat.swim()
auto.ride()

"""Создайте класс RadioMixin в нем реализуйте метод для проигрывания музыки play_music который принимает в себя название песни. Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина"""

class RadioMixin:
   
    def play_music(self):
        input('Enter the song name: ')
    
class Auto(RadioMixin):
  pass

class Boat(RadioMixin):
  pass

class Amphibian(RadioMixin):
  pass

auto = Auto()
boat = Boat()
amphibian = Amphibian()

auto.play_music()
boat.play_music()
amphibian.play_music()


"""Будильник
Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, с методами для включения и выключения будильника.
Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
нему метод для установки будильника, при вызове которого должен включатся будильник."""

from datetime import datetime

class Clock:
  
  def alarm(self):
    print (datetime.now())
    

class Alarm:
  
  def alarm_on(self):
    print('Alarm on')

  def alarm_off(self):
    print('Alarm off')
  
class AlarmClock(Clock, Alarm):
  pass
    

a = AlarmClock()
a.alarm()
a.alarm_on()


"""Разработчики
Напишите класс Coder с атрибутами experience, count_code_time = 0 и абстрактными методами
get_info и coding.
Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder. Класс Backend должен принимать дополнительно параметр languages_backend, а Frontend — languages_frontend соответственно.
Переопределите в обоих классах методы get_info и coding (так, чтобы он принимал количество часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time). 
Так же бывают FullStack разработчики и
поэтому создайте данный класс и чтобы у него были атрибуты и методы предыдущих классов. Создайте несколько экземпляров от классов Backend, Frontend, FullStack и вызовите их методы."""

class Coder:
   count_code_time = 0

   def coding(self):
      pass

class Backend(Coder):
    def __init__(self, languages_backend):
        self.language = languages_backend
    
    def get_info(self):
        print(f'Coding hours - {self.count_code_time}')
    
    def coding(self, count_hour):
        self.count_code_time += count_hour

class Frontend(Coder):

    def __init__(self, languages_frontend):
        self.language = languages_frontend

    def get_info(self):
        print(f'Coding hours - {self.count_code_time}')
        
    def coding(self, count_hour):
        self.count_code_time += count_hour
    
class FullStack(Frontend, Backend):
      pass
  

frontend = FullStack(0)
backend = FullStack(0)
fullstack = FullStack(0)

frontend.coding(15)
frontend.get_info()
backend.coding(10)
backend.coding(15)
backend.get_info()
fullstack.coding(20)
fullstack.coding(20)
fullstack.get_info()