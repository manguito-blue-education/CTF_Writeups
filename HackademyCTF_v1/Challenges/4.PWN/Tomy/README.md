# Statement

Una de las innovaciones más grandes dentro de Manguito Blue ha sido la creación de un ente con inteligencia artificial denominado Tomy. Tomy es muy listo y no te dará la bandera, excepto que lo agarres dormido. ¿Tienes la paciencia suficiente para esperar a que se duerma profundamente?

# Provided Files

```
tomy
```

# Procedure

To recognize which type of file we are facing, we can use the `file` command. If we execute:

```bash
file tomy
```

We can obtain:

```bash
tomy: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=af45f60aa815e37754705ae1182a6574dbff1087, for GNU/Linux 3.2.0, not stripped
```

So if we proceed to execute this file, we can see that it throws a lot of prints after some time. This can be mainly done with `sleep` functions. So probably we need to skip somehow this `sleep` functions to get the flag.

We can debug this executable with `gdb`, as it is an ELF file for GNU/Linux. If we open the executable with `gdb` we can do the following:

## 1. First set the disassembly flavor to intel

```bash
(gdb) set disassembly-flavor intel
```

This will set the display info with the intel format that is a little bit more friendly than the original one.

## 2. Set a breakpoint in the `main` function.

```bash
(gdb) b *main
```

b is the shortcut for breakpoint. It is safe to use the `main` function as every executable should have one function named like this to be able to be executed.

## 3. Run the executable

```bash
(gdb) run
```

This will run the executable but will stop in the first breakpoint possible, in this case, the main function from the last step.

## 4. Disassemble main function

```bash
(gdb) disassemble main
```

This would show us all the functions in assembly language that are executed inside the file.

```
 0x000055bb2dbbf279 <+0>:	endbr64
   0x000055bb2dbbf27d <+4>:	push   rbp
   0x000055bb2dbbf27e <+5>:	mov    rbp,rsp
   0x000055bb2dbbf281 <+8>:	lea    rdi,[rip+0xd80]        # 0x55bb2dbc0008
   0x000055bb2dbbf288 <+15>:	call   0x55bb2dbbf080 <puts@plt>
   0x000055bb2dbbf28d <+20>:	lea    rdi,[rip+0xd94]        # 0x55bb2dbc0028
   0x000055bb2dbbf294 <+27>:	call   0x55bb2dbbf080 <puts@plt>
   0x000055bb2dbbf299 <+32>:	mov    edi,0x3
   0x000055bb2dbbf29e <+37>:	call   0x55bb2dbbf0b0 <sleep@plt>
   0x000055bb2dbbf2a3 <+42>:	lea    rdi,[rip+0xdbe]        # 0x55bb2dbc0068
   0x000055bb2dbbf2aa <+49>:	call   0x55bb2dbbf080 <puts@plt>
   0x000055bb2dbbf2af <+54>:	mov    edi,0x5
   0x000055bb2dbbf2b4 <+59>:	call   0x55bb2dbbf0b0 <sleep@plt>
   0x000055bb2dbbf2b9 <+64>:	lea    rdi,[rip+0xdc7]        # 0x55bb2dbc0087
   0x000055bb2dbbf2c0 <+71>:	call   0x55bb2dbbf080 <puts@plt>
   0x000055bb2dbbf2c5 <+76>:	mov    edi,0x7
   0x000055bb2dbbf2ca <+81>:	call   0x55bb2dbbf0b0 <sleep@plt>
   0x000055bb2dbbf2cf <+86>:	lea    rdi,[rip+0xdce]        # 0x55bb2dbc00a4
   0x000055bb2dbbf2d6 <+93>:	call   0x55bb2dbbf080 <puts@plt>
   0x000055bb2dbbf2db <+98>:	mov    edi,0xa
   0x000055bb2dbbf2e0 <+103>:	call   0x55bb2dbbf0b0 <sleep@plt>
   0x000055bb2dbbf2e5 <+108>:	lea    rdi,[rip+0xdcf]        # 0x55bb2dbc00bb
   0x000055bb2dbbf2ec <+115>:	call   0x55bb2dbbf080 <puts@plt>
   0x000055bb2dbbf2f1 <+120>:	mov    edi,0x14
   0x000055bb2dbbf2f6 <+125>:	call   0x55bb2dbbf0b0 <sleep@plt>
   0x000055bb2dbbf2fb <+130>:	lea    rdi,[rip+0xdc4]        # 0x55bb2dbc00c6
   0x000055bb2dbbf302 <+137>:	call   0x55bb2dbbf080 <puts@plt>
   0x000055bb2dbbf307 <+142>:	lea    rdi,[rip+0xdda]        # 0x55bb2dbc00e8
   0x000055bb2dbbf30e <+149>:	call   0x55bb2dbbf080 <puts@plt>
   0x000055bb2dbbf313 <+154>:	mov    edi,0x14
   0x000055bb2dbbf318 <+159>:	call   0x55bb2dbbf0b0 <sleep@plt>
   0x000055bb2dbbf31d <+164>:	lea    rdi,[rip+0xdfc]        # 0x55bb2dbc0120
   0x000055bb2dbbf324 <+171>:	call   0x55bb2dbbf080 <puts@plt>
   0x000055bb2dbbf329 <+176>:	mov    edi,0x57e40
   0x000055bb2dbbf32e <+181>:	call   0x55bb2dbbf0b0 <sleep@plt>
   0x000055bb2dbbf333 <+186>:	lea    rdi,[rip+0xe1e]        # 0x55bb2dbc0158
   0x000055bb2dbbf33a <+193>:	call   0x55bb2dbbf080 <puts@plt>
   0x000055bb2dbbf33f <+198>:	mov    eax,0x0
   0x000055bb2dbbf344 <+203>:	call   0x55bb2dbbf1a9 <imprimir_bandera>
   0x000055bb2dbbf349 <+208>:	mov    eax,0x0
   0x000055bb2dbbf34e <+213>:	pop    rbp
   0x000055bb2dbbf34f <+214>:	ret
```

We can see that at the end that there is a function called `imprimir_bandera` that seems to be an interesting function. We can execute this function by jumping directly to it inside the debugger, we can do that with:

```bash
(gdb) jump imprimir_bandera
```

After executing this function, it will print the flag.

# Flag

`mblue{y4_t3_3st4s_v0lv13nd0_bu3n0_3n_35t0}` 
