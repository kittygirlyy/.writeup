from Crypto.Util.number import *

P = 1014758245272560775463
Q = 966428993190202075493737
E = 68399
C = 784511081438109880513098919250132930587979131
n = P * Q

phi = (P-1)*(Q-1)
d = inverse(E,phi)
m = pow(C,d,n)
print(long_to_bytes(m))