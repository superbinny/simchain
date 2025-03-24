#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

class myrandom():
    def __init__(self):
        # super().__init__()  # 初始化父类
        self.count = 0
        self.seed = 'Binny'
        self.current = 1
        self.a = 5
        self.full_string = bytes([i for i in range(256)])
        self.c = 23
        
    def lcg(self):
        # 线性同余发生器（LCG）
        # 线性同余发生器是最常见的伪随机数生成器之一。它的生成过程可以用以下公式表示：
        # Xn+1 = (a * Xn + c) mod m
        # 其中，Xn 是当前值，Xn+1 是下一个生成的值，a、c、m 是常数。
        # 该公式通过对当前值进行一系列乘法、加法和取模运算，生成下一个数值。LCG的特点是简单且高效，
        # 但在某些情况下可能会产生可预测的周期性模式。
        return (self.a * self.current + self.c) % self.range

    def randint(self, start, end):
        """生成一个指定范围内的随机整数（包括边界）"""
        # 每次调用都不一样
        self.count += 1
        self.range =  end - start + 1
        self.current = self.lcg()
        # print(f'\tDebug:randint={self.current}')
        return self.current

    def uniform(self, start, end):
        self.count += 1
        # 每次调用都不一样
        """生成一个指定范围内的随机浮点数（包括边界）"""
        self.range =  end - start + 1
        self.current = self.lcg()
        self.uniform = random.uniform(start, end)
        return self.uniform
    
    def urandom(self, length):
        ret_str = []
        for i in range(length):
            index = self.randint(0, length - 1)
            ret_str.append(self.full_string[index])
        return bytes(ret_str)
    
class MySystemRandom():
    def __init__(self):
        # super().__init__()  # 初始化父类
        self.random = myrandom()
        
    def randrange(self, start, end):
        return self.random.randint(start, end)