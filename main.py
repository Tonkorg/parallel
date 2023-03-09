#1000*1200 2 Потока
from datetime import datetime
from threading import Thread
import numpy
from random import randint

def main():
    len = 1000
    height = 1200
    len1 = 1200
    hight1 = 2000
    matrix1 = numpy.matrix([len],[height])
    matrix2 = numpy.matrix([len1], [hight1])
    count_threads = 2 #количество используемых потоков
    startTime = datetime.now() #начало отсчёта времени
    print(startTime)
    # for i in range(len):
    #     for j in range(height):
    #         matrix1[i][j] = randint(0, 100)
    #
    # print(matrix1)
    #
    #
    # for i in range(len1):
    #     for j in range(hight1):
    #         matrix2[i][j] = randint(0, 100)
    #
    #
    # matrix3 = numpy.dot(matrix1, matrix2)
    # print(f"Время выполнения:  {(datetime.now() - startTime)}")

    #thread = Thread(findFuctorial(1, 115000, numbers))
    # thread.start()
    # thread.join()
    # thread = Thread(findFuctorial(115000, 230000, numbers))
    # thread.start()
    # thread.join()
    # thread = Thread(findFuctorial(230000, 340000, numbers))
    # thread.start()
    # thread.join()
    # #подсчёт результата
    # for i in numbers:
    #   res*=i

    #вывод результата времени
#     print(f"Время: {(datetime.now() - startTime)}")
#     print(f"Количество потоков: {count_threads}")
#     #метод вычисляющий факториал
#
# def findFuctorial(start, end, res):
#     ans = 1; #вычисленное число факториала
#     i = start #число начала вычисления факториала
#     while(i <= end):
#         ans *= i;
#         i += 1
#         res.append(ans)

