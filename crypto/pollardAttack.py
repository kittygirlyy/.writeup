from Crypto.Util.number import *
import gmpy2
n = '6c22f986f42070bffcb20cde5f2b177d7e7e0aa27da9d8bff6878ca2e20decc536415464f3421b566c99b3a847563356274742960fec72f23159598a485cc1c4b14fbb06663e9216a2155dcb467eabd376af03046e1388100f30dd45110bc1a0d83cd61e601056bf4c2f7c218bb9f7092d55404ad5d1972816d0c99b1afb3891848a8149a10c1712f5aa5063b89f916258b6c7aab25199bdda4dd3bbb41861b6abe22fad20533768e9669ec724536b8edf136334817f0eb1ed7521de10fba7e57adf6a186ea507f8c4beff0bb257ba5ffca31099d1b0585adca615cc55db717e8cd368a4ddfde79c84fb4daaec9fa98af61af9351640f971098f5739101f9901'
c = '5f1b83489ccf5b6e7c61deeb9a153caea3a8db74ef7c408b69e7e31c65ed8cf0507be40eccf6e1d0aaacefb01e9c10b4051faa6186a04c517ed92f8b394ea024a1cdf500d4ffa8f00377cf63d14ad301b9112b63fa136e7c4bbef050154da3206d26f9d85987d73cf22d2648cd18c8641de25bbb01f84105b8df327616eb8f68d3ef1d5b5271b411564cd1ff04ee975a19a2cfeb87f1cbed0cf131501d966ec8bb6dcd3f43939e987d52c25b36326f02cfa542fc393c87e49b682faf8262621d89714271e22adb189530574140a68aa518d6133115a573f534ab577dadd04fcffb742cb186d7c75f640e0f21fcb9273745a0d4f60916c117717b0bab3ebd1fd'

def Pollard(n):
    a = 2
    while True:
        for i in range(2,80000):
            a = pow(a,i,n)
        for j in range(80000,104729+1):
            a = pow(a,j,n)
            if j % 15 == 0:
                d = GCD(a-1,n)
                if(1 < d < n):
                    return(d)
        a += 1
p = Pollard(int(n,16))
q = int(n,16)//p
d = gmpy2.invert(65537,(p-1)*(q-1))
m = pow(int(c,16),d,int(n,16))
print(long_to_bytes(m))