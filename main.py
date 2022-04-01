# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print('Hello')
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(1)


t1 = Hello()
t2 = Hi()
t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()
print('bye')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
