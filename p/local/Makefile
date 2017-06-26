.PHONY: clean bin

shellcode: shellcode.o
	ld -melf_i386 -Ttext 0x804a060 -s $< -o $@

shellcode.o: shellcode.asm
	nasm -f elf $< -o $@

clean:
	rm -f *.o
	echo unix > file

bin:
	nasm shellcode.asm -o shellcode.bin

