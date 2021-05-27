import time
import itertools

class TrafficLight:
    __color = [["red", 7, 31], ["yellow", 2, 33], ["green", 7, 32], ["yellow", 2, 33]]

    def running(self):
        for item in itertools.cycle(self.__color):
            print(f"\r\033[{item[2]}m\033[1m{item[0]}\033[0m", end='' )
            time.sleep(item[1])


svetofor = TrafficLight()
svetofor.running()

#долго тупил как сделать ввод с начала строки и не выводить все подряд, пришлось подсмотреть фишку со сдвигом каретки, Не ругайтесь))
