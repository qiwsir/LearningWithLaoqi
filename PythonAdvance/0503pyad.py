#coding:utf-8

"""
问题：
在地球上，重力加速度跟物体所在的维度和高度有关，它的值不是固定不变的。
编写一个嵌套函数，实现G=mg，计算物体的重力。
要求：
    （1）首先确定不同的重力加速度；
    （2）然后传入参数质量的值，得到该位置物体的重力
"""

def weight(g):
    def calc_mg(m):
        return m * g
    return calc_mg

if __name__ == "__main__":
    g0 = 9.8    #通常计算使用的值
    G0 = weight(g0)
    w0 = G0(10)
    print("g=9.8, m = 10kg, G = {0}".format(w0))
    print("-"*30)
    g1 = 9.78046    #赤道海平面上的重力加速度
    G1 = weight(g1)
    w1 = G1(10)
    print("g1 = 9.78046, m = 10kg, G = {0}".format(w1))
