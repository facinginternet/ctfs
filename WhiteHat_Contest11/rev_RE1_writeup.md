# RE1

Category: Reverse Engineering   
Points: 100

## Question

```
http://material.wargame.whitehat.vn/contests/11/re1_d3309936b177b41dada3796c4c3acadf.zip
```

## Answer

```re1_d3309936b177b41dada3796c4c3acadf.zip``` の中には，```RE100``` というファイルが入っている．

```zsh
% file RE100
RE100: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), dynamically linked (uses shared libs), for GNU/Linux 2.6.32, from 'x)', not stripped
```

ファイル形式は**ELF 64-bit**．   
ubuntuで実行してみる．

```
$ ./RE100
Input key : hogehoge
Wrong !!!

Input key : flag please
Wrong !!!
```

正しいキーを入力すればいいらしい．   
Hopper Disassemblerで静的解析する．

```
00000000004a1a38  db  "{daf29f59034938ae4efd53fc275d81053ed5be8c}", 0 ; XREF=main+519
```

適当にStringsを眺めてると怪しい文字列を発見．  
処理を追ってみると↑の文字列をシャッフルして入力と比較していることがわかる．

```
00000000004089a4	mov	rax,	qword	[ss:rbp+var_58]	;	XREF=_Z10confuseKeyPci+200
00000000004089a8	lea	rcx,	qword	[ds:rax+1]
00000000004089ac	lea	rax,	qword	[ss:rbp+var_50]
00000000004089b0	mov	edx,	0xa	;	argument	"n"	for	method	j_strncpy
00000000004089b5	mov	rsi,	rcx	;	argument	"src"	for	method	j_strncpy
00000000004089b8	mov	rdi,	rax	;	argument	"dst"	for	method	j_strncpy
00000000004089bb	call	j_strncpy
00000000004089c0	mov	rax,	qword	[ss:rbp+var_58]
00000000004089c4	lea	rcx,	qword	[ds:rax+0xb]
00000000004089c8	lea	rax,	qword	[ss:rbp+var_40]
00000000004089cc	mov	edx,	0xa	;	argument	"n"	for	method	j_strncpy
00000000004089d1	mov	rsi,	rcx	;	argument	"src"	for	method	j_strncpy
00000000004089d4	mov	rdi,	rax	;	argument	"dst"	for	method	j_strncpy
00000000004089d7	call	j_strncpy
00000000004089dc	mov	rax,	qword	[ss:rbp+var_58]
00000000004089e0	lea	rcx,	qword	[ds:rax+0x15]
00000000004089e4	lea	rax,	qword	[ss:rbp+var_30]
00000000004089e8	mov	edx,	0xa	;	argument	"n"	for	method	j_strncpy
00000000004089ed	mov	rsi,	rcx	;	argument	"src"	for	method	j_strncpy
00000000004089f0	mov	rdi,	rax	;	argument	"dst"	for	method	j_strncpy
00000000004089f3	call	j_strncpy
00000000004089f8	mov	rax,	qword	[ss:rbp+var_58]
00000000004089fc	lea	rcx,	qword	[ds:rax+0x1f]
0000000000408a00	lea	rax,	qword	[ss:rbp+var_20]
0000000000408a04	mov	edx,	0xa	;	argument	"n"	for	method	j_strncpy
0000000000408a09	mov	rsi,	rcx	;	argument	"src"	for	method	j_strncpy
0000000000408a0c	mov	rdi,	rax	;	argument	"dst"	for	method	j_strncpy
0000000000408a0f	call	j_strncpy

                                          ...

0000000000408a32	lea	rdx,	qword	[ss:rbp+var_30]
0000000000408a36	mov	rax,	qword	[ss:rbp+var_58]
0000000000408a3a	mov	rsi,	rdx	;	argument	"s2"	for	method	j_strcat
0000000000408a3d	mov	rdi,	rax	;	argument	"s1"	for	method	j_strcat
0000000000408a40	call	j_strcat
0000000000408a45	lea	rdx,	qword	[ss:rbp+var_20]
0000000000408a49	mov	rax,	qword	[ss:rbp+var_58]
0000000000408a4d	mov	rsi,	rdx	;	argument	"s2"	for	method	j_strcat
0000000000408a50	mov	rdi,	rax	;	argument	"s1"	for	method	j_strcat
0000000000408a53	call	j_strcat
0000000000408a58	lea	rdx,	qword	[ss:rbp+var_50]
0000000000408a5c	mov	rax,	qword	[ss:rbp+var_58]
0000000000408a60	mov	rsi,	rdx	;	argument	"s2"	for	method	j_strcat
0000000000408a63	mov	rdi,	rax	;	argument	"s1"	for	method	j_strcat
0000000000408a66	call	j_strcat
0000000000408a6b	lea	rdx,	qword	[ss:rbp+var_40]
0000000000408a6f	mov	rax,	qword	[ss:rbp+var_58]
0000000000408a73	mov	rsi,	rdx	;	argument	"s2"	for	method	j_strcat
0000000000408a76	mov	rdi,	rax	;	argument	"s1"	for	method	j_strcat
0000000000408a79	call	j_strcat
```

1. **{daf29f59034938ae4efd53fc275d81053ed5be8c}**から一部分をstrncpyで抜き出す x 4回．   
2. 抜き出した文字列をstrcatで連結する x 4回．  

この処理をシミュレートして文字列をシャッフルする  
```
{daf29f59034938ae4efd53fc275d81053ed5be8c}
                    ↓
{53fc275d81053ed5be8cdaf29f59034938ae4efd}
```

**RE100**に打ち込んでみると

```
$ ./RE100
Input key : {53fc275d81053ed5be8cdaf29f59034938ae4efd}
True
```

やったね

## Flag
***{53fc275d81053ed5be8cdaf29f59034938ae4efd}***
