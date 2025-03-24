#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys

sys.path.append('..')

# 使用 https://zhuanlan.zhihu.com/p/52074021 给的例子进行随机数的测试
# 导入Network、Peer对象
from simchain import Network,Peer

print('创建区块链虚拟网络，初始节点数量为1，创世币为 10000 分')
net = Network(nop = 1, von = 10000)
print('访问网络中的节点数量')
print(net.nop)
print('访问网络中的节点，列表类型，每个节点会随机生成一个坐标，类似IP地址')
print(net.peers)
print('将0号节点命名为张三')
zhangsan = net.peers[0]
print('张三的IP地址，在Simchain中无具体用处')
print(zhangsan.coords)
print('访问张三的私钥')
print(zhangsan.sk)
# b'\xaa\xfb\xec\r\xc6\x19%\xb8\x9e\x0cN\x99s\xa1\xb7\xf8\x8c]`\xd7"\xd13{\xefr\x89\xb52\xde\xdbQ' 
print('访问张三的公钥')
print(zhangsan.pk)
# b'8\xc96\xb6\x0c\x15.|(\xbec\xb8N\xce\xea\xd7\xed\x9d\x06\x0b\x94\xae\xb5_\xc4\xc2G\xae\x0e(}\xe3\x90D\xb6\n\xd9\xfe%U\x0fT f\xcb\xbe7\xb9\xb2c\xda\xd1a\t\x03}\x84*\x98\xb1}0\xd3\x03' 
print('访问张三的地址')
print(zhangsan.addr)
# '13JyTbD3oR9Bgasa45uXsbgbdDmS67i89K'
print('查看张三的余额，为10000分')
print(zhangsan.get_balance())
print('访问创世区块')
print(zhangsan.blockchain[0])
# Block(hash:9f53d80df4ed3e2cdbd1e6510be2f1c55c765838eeef55f04559926cc5697265)
print('访问创世区块中的交易，数量为1')
print(zhangsan.blockchain[0].txs)
# [Tx(id:d18a391ae803454405b7e0185ef40fef14b34848a8248885633c2b34a2a3bad2)]
print('访问创世区块中交易的输出，1个输出单元')
print(zhangsan.blockchain[0].txs[0].tx_out)
# [Vout(to_addr:13JyTbD3oR9Bgasa45uXsbgbdDmS67i89K,value:10000)]
print('获取张三的UTXO，数量也为1')
print(zhangsan.get_utxo())