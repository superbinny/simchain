#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys

sys.path.append('..')

# 使用 https://zhuanlan.zhihu.com/p/52074021 给的例子进行随机数的测试

step = 0
def print_step(msg):
    global step
    step += 1
    print(f'Step {step}:{msg}')

# 来自工具 F:\Document\OneDrive\Program\latex\DOC\blockchain\Scripts\Fix区块链模拟器simchain.py

print_step('导入Network、Peer对象')
from simchain import Network,Peer
print_step('创建区块链虚拟网络，初始节点数量为1，创世币为10000分')
net = Network(nop = 1,von = 10000)
print_step('访问网络中的节点数量')
print(net.nop)
# 1
print_step('访问网络中的节点，列表类型，每个节点会随机生成一个坐标，类似IP地址')
print(net.peers)
# [peer(54, 40)]
print_step('将0号节点命名为张三')
zhangsan = net.peers[0]
print_step('张三的IP地址，在Simchain中无具体用处')
print(zhangsan.coords)
# (54, 40)
print_step('访问张三的私钥')
print(zhangsan.sk)
# b'\xaa\xfb\xec\r\xc6\x19%\xb8\x9e\x0cN\x99s\xa1\xb7\xf8\x8c]`\xd7"\xd13{\xefr\x89\xb52\xde\xdbQ'
print_step('访问张三的公钥')
print(zhangsan.pk)
# b'8\xc96\xb6\x0c\x15.|(\xbec\xb8N\xce\xea\xd7\xed\x9d\x06\x0b\x94\xae\xb5_\xc4\xc2G\xae\x0e(}\xe3\x90D\xb6\n\xd9\xfe%U\x0fT f\xcb\xbe7\xb9\xb2c\xda\xd1a\t\x03}\x84*\x98\xb1}0\xd3\x03'
print_step('访问张三的地址')
print(zhangsan.addr)
# '13JyTbD3oR9Bgasa45uXsbgbdDmS67i89K'

print_step('查看张三的余额，为10000分')
print(zhangsan.get_balance())
# 10000
print_step('访问创世区块')
print(zhangsan.blockchain[0])
# Block(hash:9f53d80df4ed3e2cdbd1e6510be2f1c55c765838eeef55f04559926cc5697265)
print_step('访问创世区块中的交易，数量为1')
print(zhangsan.blockchain[0].txs)
# [Tx(id:d18a391ae803454405b7e0185ef40fef14b34848a8248885633c2b34a2a3bad2)]
print_step('访问创世区块中交易的输出，1个输出单元')
print(zhangsan.blockchain[0].txs[0].tx_out)
# [Vout(to_addr:13JyTbD3oR9Bgasa45uXsbgbdDmS67i89K,value:10000)]
print_step('获取张三的UTXO，数量也为1')
print(zhangsan.get_utxo())
# [UTXO(vout:Vout(to_addr:13JyTbD3oR9Bgasa45uXsbgbdDmS67i89K,value:10000),
# pointer:Pointer(tx_id:d18a391ae803454405b7e0185ef40fef14b34848a8248885633c2b34a2a3bad2,n:0))]

print_step('添加一个节点到网络中')
net.add_peer()
print_step('将第二个节点命名为李四')
lisi = net.peers[1]
print_step('访问李四的私钥')
print(lisi.sk)
# b'9\xe1\xe8\xa52P\x1a<HZ\xe3\x05\x13\x05\x99\xcc\x97CP\x9f\x0e\x82\x01\xb49\xe2\xa4k<\xe5\x1c\x8f'
print_step('访问李四的公钥')
print(lisi.pk)
# b"\xd9\x92\xbe\xa9\xd7\x832D\xffl*\xadz\\:\x8clT@\xb0H\x9f\xd8!\xc6\xe1\x13G+\n\xf2\xf8\x05\xfeo\xbe\xa9\xf8\xf1\xc6\xdd\x0e\x9d\x13\x02'\xea\x86\xb7U\xaf\xec\\\xe8 \x08\xd6\x88S\xdb\x90\xf3\xad\xd1"
print_step('访问李四的地址')
print(lisi.addr)
# '14k7yTRabxn67RxV6FJzSArBuMQxB5nERX'
print_step('张三的区块链与李四的区块链相同')
print(zhangsan.blockchain == lisi.blockchain)
# True
print_step('张三的UTXO集与李四的UTXO集相同')
print(zhangsan.utxo_set == lisi.utxo_set)
# True
print(lisi.get_balance())
# 0

print_step('参数为李四的地址和金额')
zhangsan.create_transaction(lisi.addr,100)
print_step('获取当前交易')
tx = zhangsan.current_tx
print_step('访问当前交易的输出')
print(tx.tx_out)
# [Vout(to_addr:14k7yTRabxn67RxV6FJzSArBuMQxB5nERX,value:100), Vout(to_addr:13JyTbD3oR9Bgasa45uXsbgbdDmS67i89K,value:9890)]
print_step('张三余额')
print(zhangsan.get_balance())
# 10000
print_step('李四的余额')
print(lisi.get_balance())
# 0
print_step('张三将交易广播到网络中')
zhangsan.broadcast_transaction()
print_step('张三余额，10分的交易费')
print(zhangsan.get_balance())
# 9890
print_step('李四的余额')
print(lisi.get_balance())
# 100


print_step('获取张三未确认的UTXO')
print(zhangsan.get_unconfirmed_utxo())
# [UTXO(vout:Vout(to_addr:13JyTbD3oR9Bgasa45uXsbgbdDmS67i89K,value:9890),
# pointer:Pointer(tx_id:3b182b06b3c7c89f67f19a8a8ca009267b2f83db9f73a6fc1aa16cdb4a4994a1,n:1))]
print_step('获取李四未确认的UTXO')
print(lisi.get_unconfirmed_utxo())
# [UTXO(vout:Vout(to_addr:14k7yTRabxn67RxV6FJzSArBuMQxB5nERX,value:100),
# pointer:Pointer(tx_id:3b182b06b3c7c89f67f19a8a8ca009267b2f83db9f73a6fc1aa16cdb4a4994a1,n:0))]
print(zhangsan.get_height() == lisi.get_height() == 1)
# True
print_step('张三的交易池中有一条交易')
print(zhangsan.mem_pool)
# {'3b182b06b3c7c89f67f19a8a8ca009267b2f83db9f73a6fc1aa16cdb4a4994a1': Tx(id:3b182b06b3c7c89f67f19a8a8ca009267b2f83db9f73a6fc1aa16cdb4a4994a1)}
print_step('李四的交易池与张三的相同')
print(lisi.mem_pool == zhangsan.mem_pool)
# True


print_step('网络中的节点达成共识')
print(net.consensus())
# 2018-06-21 17:23:37,711 - 2 peers are mining
# 2018-06-21 17:23:42,368 - peer(54, 40)(pid=0) is winner,4.594226121902466 secs used
# 2018-06-21 17:23:42,478 - Block(
# hash:00002b876ad6abfe15f688cf63497573f50cd451fbdcd8a837173453370da7c9) received by 1 peers
print_step('张三获得奖励固定500分，交易费10分')
print(zhangsan.get_balance())
# 10400
print(zhangsan.get_height() == lisi.get_height() == 2)
# True
print(zhangsan.get_unconfirmed_utxo() == lisi.get_unconfirmed_utxo() ==[])
# True
print_step('第一条交易为创币交易')
print(zhangsan.blockchain[1].txs[0].is_coinbase)
# True
print_step('奖励500分，交易费10分')
print(zhangsan.blockchain[1].txs[0].tx_out[0].value)
# 510

print_step('从Simchain中导入Network')
from simchain import Network
print_step('创建一个网络，初始节点12个')
net = Network()
print_step('0号节点命名位张三')
zhangsan = net.peers[0]
print_step('6号节点命名为李四')
lisi = net.peers[6]

print_step('访问钥匙对的数量，目前数量为1对，nok = number of keys')
print(zhangsan.wallet.nok)
# 1
print_step('访问张三第一对密钥私钥的字节串编码')
print(zhangsan.wallet.keys[0].sk.to_bytes())
# b"R\x06~\xeaf2\xc3\xc8t\xb8\xa5\x9d!'\xf3D8_\x1e\x04\xc0\xfb\xe1\xe3\x0e\x90\xc0\xe5+S>"
print_step('访问张三第一对钥匙公钥的字节串编码')
print(zhangsan.wallet.keys[0].pk.to_bytes())
# b"\x8bq\xb3J\xbeS\x9e\xad\xee\xea\xceb\x16\rk?\x90\x1b\x03\xa2K\xf6\xb3\xfa\xfd\xf6\xa4~\n1\xa4\x7f\x85GL-'\x92u\rM)\xe0e\x01~PK&G\xce\xe8Kw0sh\xe7oY\xea\x91g\xb4"
print_step('访问张三第一对密钥对应的地址')
print(zhangsan.wallet.addrs[0])
# '1AkBHz6DfMstFWqaF7s3xa9VUXnQpBtUqQ'

print(lisi.wallet.keys[0].sk.to_bytes())
# b'.6Z27,;o\xb7\x97\xd3\x1c?+\x94\x9bA#!=\xee\xbaF\x16\xc7\xec}\xa6\xa75\xd2\x07'
print(lisi.wallet.keys[0].pk.to_bytes())
# b"\xddS\xa6}\x7f\xef\x80\x8b\x06\xb23\xeb}I\xe2\xbe\xd3GR\x87'DsX\xda\xa3\xce7\\\xfc\x9a\x0c\x15\x08e\xb4\x06\x19#!V\xcc\xd3\x02/de\x7fS\xe4\xca` \xbf-\xe6\xcd$X\xbe]]v\x1e"
print(lisi.wallet.addrs[0])
# '1LzciVftLW1BnDBBNbioGq6NxXweHr8UkY'

print_step('生成新的钥匙、地址对')
zhangsan.wallet.generate_keys()
print(zhangsan.wallet.nok)
# 2
print_step('张三第二对密钥私钥的字节串编码')
print(zhangsan.wallet.keys[1].sk.to_bytes())
# b'\xd5\xe7V`w\xe6\xe0\x98=\x7f\xbc\xdd_\xe7h,\x0f\x00z~\x07\\\xf9\xd9\x1e\x1cf\xc1E\x19\x997'
print_step('张三第二对密钥公钥的字节串编码')
print(zhangsan.wallet.keys[1].pk.to_bytes())
# b'\xc5\xa3\x04\x8d\xd8\xb7\xa1\x9d\xd0\x85\xbe\xd4\xbf9\xaf\xac\xf2\x94(\xfeY\xdf\xaa]\xfdD\r\x19\xec\xf2\xb1f\xcf\xcd\x84\xf7+\xad\xa0?b\xb4\x00\xd5\xed\x932-\xb8\x1d6\xbdA\n7\xff\x9a\x1f=1\xdch\xafA'
print_step('张三第二对密钥对应的地址')
print(zhangsan.wallet.addrs[1])
# '13QbeqbFWXX5GxNQuZxd6heUp9H34LFDMW'

print_step('指向李四的地址')
print(zhangsan.create_transaction(lisi.wallet.addrs[0],1000))
# 2018-06-05 14:20:39,386 - peer(83, 55)(pid=0) created a transaction
# True
print_step('张三广播交易')
print(zhangsan.broadcast_transaction())
# 2018-06-05 14:20:59,388 - peer(83, 55)(pid=0) sent a transaction to network
# 2018-06-05 14:21:00,516 - peer(83, 55)(pid=0)'s transaction verified by 9 peers

print_step('访问节点创建的最新交易')
tx = zhangsan.txs[-1]
print(tx)
# Tx(id:1a15c7645ddb67f4f129b43cc622c0dd8c7b7b82048c78ea3dcfcc511cceb4b3)
print_step('访问交易输入列表，只有一个输入单元')
print(tx.tx_in)
# [Vin(to_spend:Pointer(tx_id:48edf9a0c1064b8f57c83e15027a397aa6a8a2819fdce635f12f1f7683fbef53,n:0), signature:b'\xd3\xaa\x9e&mPmr\x97*\xe0<\xb1G$S\xc4\xf1\xf3\xc8\x11\x07\xee\x7f\tR\xea\xac4&\xa7~\xb8\xce\xf9\xe1t\xabL5{\xe0-\x93\xe4{\x9a\xfa^<\x85G8\xef1\x10L\x9dQX2\x0c\xa1', pubkey:b"\x8bq\xb3J\xbeS\x9e\xad\xee\xea\xceb\x16\rk?\x90\x1b\x03\xa2K\xf6\xb3\xfa\xfd\xf6\xa4~\n1\xa4\x7f\x85GL-'\x92u\rM)\xe0e\x01~PK&G\xce\xe8Kw0sh\xe7oY\xea\x91g\xb4")]

print_step('张三创建交易使用的UTXO所在的交易编号')
print(zhangsan.blockchain[0].txs[0].id)
# '48edf9a0c1064b8f57c83e15027a397aa6a8a2819fdce635f12f1f7683fbef53'
print_step('获取交易的第1个输出单元')
vout = zhangsan.blockchain[0].txs[0].tx_out[0]
print(vout)
# Vout(to_addr:1AkBHz6DfMstFWqaF7s3xa9VUXnQpBtUqQ,value:100000)
print_step('该地址属于张三')
print(vout.to_addr in zhangsan.wallet.addrs)
# True
print_step('指向张三的第一个地址')
print(zhangsan.wallet.addrs)
# ['1AkBHz6DfMstFWqaF7s3xa9VUXnQpBtUqQ', '13QbeqbFWXX5GxNQuZxd6heUp9H34L']

print_step('李四验证交易通过')
print(lisi.verify_transaction(tx))
# True

print_step('从simchain中导入输入单元Vin')
from simchain import Vin
print_step('获取交易的输入')
vin = tx.tx_in[0]
print_step('创建新的输入，放入新的签名')
vin1 = Vin(vin.to_spend,b'1'*64,vin.pubkey)
print_step('替换输入单元')
tx.tx_in[0] = vin1
print_step('李四验证交易不通过')
print(lisi.verify_transaction(tx))
# 2018-07-11 11:56:26,527 - singature does not math for
# Tx(id:8c2d40f2e3713dd783ff6f9883c5140c747bdb700495606accf88c309911e28b)
# False

pk_str = lisi.pk
print_step('创建新的输入单元')
vin2 = Vin(vin.to_spend,vin.signature, pk_str)
print_step('替换输入单元')
tx.tx_in[0] = vin2
print_step('李四验证交易仍不通过')
print(lisi.verify_transaction(tx))
# 2018-07-11 12:06:05,156 - singature does not math for
# Tx(id:4e86fb38c5488ed9f03a69a11029fc0b76587f0058573ec22bec048d6359930e)
# False

sk = zhangsan.wallet.keys[1].sk
pk = zhangsan.wallet.keys[1].pk
print_step('选择一条签名明文')
message = b'I love block chain'
print_step('用私钥进行签名')
signature = sk.sign(message)
print_step('用公钥签证签名')
print(pk.verify(signature,message))
# True
print_step('用张三的第一对密钥公钥验证签名')
pk1 = zhangsan.wallet.keys[0].pk
print(pk1.verify(signature,message))
# False

from simchain import Pointer
print_step('创建一个新的定位指针')
pointer = Pointer(vin.to_spend.tx_id,1)
print_step('新指针指向的输出单元')
new_out = zhangsan.blockchain[0].txs[0].tx_out[1]
print(new_out)
# Vout(to_addr:14YGxM1cR2ES8WnKemvNmEwd1q7jdF5SR1,value:100000)
print_step('输出单元指向的地址')
print(new_out.to_addr)
# '14YGxM1cR2ES8WnKemvNmEwd1q7jdF5SR1'
print_step('该地址不属于张三')
print(new_out.to_addr in zhangsan.wallet.addrs)
# False
print_step('创建一个新的输入单元')
vin3 = Vin(pointer,vin.signature,vin.pubkey)
print_step('替换输入单元')
tx.tx_in[0] = vin3
print_step('李四验证交易不通过')
print(lisi.verify_transaction(tx))
# 2018-07-11 12:44:09,041 - singature does not math for
# Tx(id:feb72cbc616688ca03912929afc1310154c97b1eba0b5ebca0c15d34beec3056)
# False

