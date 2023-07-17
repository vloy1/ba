from web3 import Web3
import json
import requests
import time
import random
from web3.middleware import geth_poa_middleware

start = time.time()

arb = {
    'name':'Arbitrum',
    'RPC':'https://arb1.arbitrum.io/rpc',}

avax = {
    'name':'Avax',
    'RPC':'https://avalanche-c-chain.publicnode.com/',}

bsc = {
    'name':'Bep20',
    'RPC':'https://bsc-dataseed1.defibit.io/',}

poligon = {
    'name':'poligon',
    'RPC':'https://polygon-rpc.com',}

def res_balance(set,adres):
    w3 = Web3(Web3.HTTPProvider(set['RPC'])) 
    eth_balance = w3.eth.get_balance(adres)
    print(eth_balance)
    if eth_balance <= 0:
        return 0
    else:
        return 1


def wallett():
    try:
        private = open('wal.txt','r').read().splitlines()
        wallet = private[00]
        return wallet
    except:
        print('Кошельки кончились')

def wallett_del():
    ish = open('wal.txt','r').readlines()
    del ish[00]
    with open("wal.txt", "w") as file:
        file.writelines(ish)

def write(text,set):
    name_set = set['name']
    with open(f'{name_set}.txt', 'a') as f:
        f.write(f'{text}\n')

def main():
    while True:
        try:
            ak = wallett()
            r = res_balance(arb,ak)
            if r == 0:
                write(ak,arb)
            r1 = res_balance(avax,ak)
            if r1 == 0:
                write(ak,avax)
            r2 = res_balance(bsc,ak)
            if r2 == 0:
                write(ak,bsc)
            r3 = res_balance(poligon,ak)
            if r3 == 0:
                write(ak,poligon)
            wallett_del()
        except:
            break

main()

end = time.time() - start
print(end)