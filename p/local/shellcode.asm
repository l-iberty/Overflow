
[section .text]
ALIGN	32
global	_start
global	_exit

_start:
	mov	ecx, O_RDWR
	mov	ebx, FileName
	mov	eax, NR_open		; open
	int	0x80
	;cmp	eax, ERROR_CODE
	;je	_exit

	mov	edx, rBUFSIZE
	mov	ecx, rBuf
	mov	ebx, eax		; fd
	mov	eax, NR_read		; read
	int	0x80
	cmp	eax, ERROR_CODE
	je	_exit
	
	push	eax			; num of bytes read
	push	rBuf			; bytes read from fd
	call	DispStr
	add	esp, 8

	;mov	edx, wBUFSIZE
	;mov	ecx, wBuf
	;mov	ebx, [fd]		; fd
	;mov	eax, NR_write		; write
	;int	0x80
	;cmp	eax, ERROR_CODE
	;je	_exit

	;mov	ebx, [fd]		; `
	;mov	eax, NR_close		; | close(fd)
	;int	0x80			; /

	;push	szLen
	;push	szBuf
	;call	DispStr
	;add	esp, 8
	
_exit:
	;mov	ebx, 0
	;mov	eax, NR_exit
	;int	0x80
	
	jmp	$


;------------------------------------------------------------
;  void DispStr(char* p_buf, int len);
;------------------------------------------------------------
DispStr:
	push	ebp
	mov	ebp, esp
	mov	ecx, [ebp + 8]	; p_buf
	mov	edx, [ebp + 12]	; len
	mov	ebx, STDOUT
	mov	eax, NR_write
	int	0x80
	leave
	ret


;[section .data]
NR_exit		equ	1
NR_read		equ	3
NR_write	equ	4
NR_open		equ	5
NR_close	equ	6


O_RDONLY	equ	0
O_WRONLY	equ	1
O_RDWR		equ	2

O_CREAT		equ	64

ERROR_CODE	equ	(-1)
STDOUT		equ	1


;szBuf		db	"Done!",0Ah
;szLen		equ	$ - szBuf

rBuf		times 32 db 0
rBUFSIZE	equ	$ - rBuf

;wBuf		db	"All Data to be written",0Ah
;wBUFSIZE	equ	$ - wBuf

FileName	db	"file",0
