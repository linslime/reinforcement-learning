#用于第一题第一问求解
import math
import matplotlib.pyplot as plt
import csv

#步长，初始值，及终止值
step = 0.00000001
start = 0
end = 0.1

g = 10
R = 0.00001

def f1(x,u1,u2):
    return u2

def f2(x,u1,u2):
    return -1 * math.cos(u1) * g / R



#龙格库塔
def RK4(u1,u2,x):
    for i in range(len(x) - 1):
        k11 = f1(x[i], u1[i], u2[i])
        k21 = f2(x[i], u1[i], u2[i])

        k12 = f1(x[i] + step / 2, u1[i] + step * k11 / 2, u2[i] + step * k21 / 2)
        k22 = f2(x[i] + step / 2, u1[i] + step * k11 / 2, u2[i] + step * k21 / 2)

        k13 = f1(x[i] + step / 2, u1[i] + step * k12 / 2, u2[i] + step * k22 / 2)
        k23 = f2(x[i] + step / 2, u1[i] + step * k12 / 2, u2[i] + step * k22 / 2)

        k14 = f1(x[i] + step, u1[i] + step * k13, u2[i] + step * k23)
        k24 = f2(x[i] + step, u1[i] + step * k13, u2[i] + step * k23)

        u1[i + 1] = u1[i] + step / 6 * (k11 + 2 * k12 + 2 * k13 + k14)
        u2[i + 1] = u2[i] + step / 6 * (k21 + 2 * k22 + 2 * k23 + k24)

    return [u1,u2]

#主函数
if __name__ == "__main__":

    x = []
    temp = start
    while temp <= end:
        x.append(temp)
        temp += step

    u1 = [0 for i in range(len(x))]
    u2 = [0 for i in range(len(x))]
    u2[0] = math.pow(1 * g / R,0.5)

    ans = RK4(u1,u2,x)


    # with open("D:\Desktop\\T1.1.csv", "w", newline="") as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerows(list(map(list, zip(*ans))))

    # t = [1.570796*math.sin(2*math.pi * i / 4.69048) for i in x]

    #作图
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(x, u1, color="red" ,linewidth=1.0, linestyle="-")  # 将散点连在一起
    # plt.plot(x, t, color="blue", linewidth=1.0, linestyle="-")  # 将散点连在一起
    plt.xlabel('时间/s')
    plt.ylabel('角位移')
    plt.show()

    #作图
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(x, u2, color="red" ,linewidth=1.0, linestyle="-")  # 将散点连在一起
    plt.xlabel('时间/s')
    plt.ylabel('角速度')
    plt.show()















