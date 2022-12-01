from eth_account import Account
import secrets
import time
import pyetherbalance 


def generate_key_pair():
    private_key = secrets.token_hex(32)
    acc = Account.privateKeyToAccount(private_key)
    return (acc.address, private_key)


def search_addresses():
    infura_url = 'https://mainnet.infura.io/v3/e508404adf4241ef83e5fc8bc05e9b8a'
    ethbalance = pyetherbalance.PyEtherBalance(infura_url)

    counter = 0
    start = time.perf_counter()

    while True:
        a = generate_key_pair()
        balance_eth = ethbalance.get_eth_balance(a[0])
        addr_per_s = counter / (time.perf_counter() - start)

        print(f'Address: {a[0]}')
        print(f'Private key: 0x{a[1]}')
        print(f'Balance in ETH: {balance_eth["balance"]}')
        print(f'({addr_per_s} addr/s)')

        if balance_eth['balance'] > 0:
            print('--- An address with a non-zero balance has been found ---')
            break

        print()
        counter += 1


def found_prefix(prefix, case_sensitive=True):
    counter = 0
    start = time.perf_counter()


    if case_sensitive is True:
        while True:
            a = generate_key_pair()
            addr_per_s = counter / (time.perf_counter() - start)

            if prefix == a[0][2:len(prefix)+2]:
                print(f'Address: {a[0]}')
                print(f'Private key: 0x{a[1]}')
                print(f'({int(addr_per_s)} addr/s)')
                print()

            counter += 1

    elif case_sensitive is False:
        while True:
            a = generate_key_pair()
            addr_per_s = counter / (time.perf_counter() - start)

            if prefix.casefold() == (a[0][2:len(prefix)+2]).casefold():
                print(f'Address: {a[0]}')
                print(f'Private key: 0x{a[1]}')
                print(f'({int(addr_per_s)} addr/s)')
                print()

            counter += 1




#found_prefix('EEE', True)
#free_eth()






import datetime as dt
from multiprocessing import Process, current_process
import sys

def f(name):
    print('{}: hello {} from {}'.format(
        dt.datetime.now(), name, current_process().name))
    sys.stdout.flush()




counter = 0
def found_prefix_multiprocessing(prefix, start, case_sensitive=True):
    global counter


    for i in range(2000):
        if case_sensitive is True:
            a = generate_key_pair()
            addr_per_s = counter / (time.perf_counter() - start)

            if prefix == a[0][2:len(prefix)+2]:
                print(f'Address: {a[0]}')
                print(f'Private key: 0x{a[1]}')
                print(f'({int(addr_per_s)} addr/s)')
                print()

            counter += 1

        elif case_sensitive is False:
    
            a = generate_key_pair()
            addr_per_s = counter / (time.perf_counter() - start)

            if prefix.casefold() == (a[0][2:len(prefix)+2]).casefold():
                print(f'Address: {a[0]}')
                print(f'Private key: 0x{a[1]}')
                print(f'({int(addr_per_s)} addr/s)')
                print()

            counter += 1
        print('z funkcji counter: ', counter)


if __name__ == '__main__':
    start = time.perf_counter()

    worker_count = 2
    worker_pool = []
    for _ in range(worker_count):
        p = Process(target=found_prefix_multiprocessing, args=('a', start, False))
        p.start()
        worker_pool.append(p)
    for p in worker_pool:
        p.join()  # Wait for all of the workers to finish.

    print('counter: ', counter)
    print('Finished')