from Crypto.Util.number import *
import gmpy2


n = 980691789310217045137229890561810025319775231
c = 784511081438109880513098919250132930587979131

phi = int(n,16) - int(x,16) + 1
d = gmpy2.invert(65537,phi)
m = pow(int(c,16),d,int(n,16))
print(long_to_bytes(m))