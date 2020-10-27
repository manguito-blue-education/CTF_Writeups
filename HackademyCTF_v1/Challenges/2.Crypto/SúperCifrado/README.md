# Statement

Yo, al aprender más acerca de la codificación en base64, y ver que no era realmente un cifrado, me propuse a hacer un algoritmo con un poco de ofuscación extra para prevenir que el mensaje fuera descifrado por alguien al que no era destinado.

¿Verdad que mi algoritmo sí es seguro?


# Files Provided

```
cipher.py
```

# Procedure

We have to give a look at the given file. The file gives a string and says that it is the result of the `super_cifrar` function. After examining that function we can see that it encodes the output of the `magic` function. If we look at that function we can see that it alternates between uppercase and lowercase.

In other words, what the original script does is that it encodes a string (the flag) in base64 and then it alternates the lowercase and uppercase letters.

So the solution can be done in one line with Python:

``` python
    descifrada = decode_base64(magic(str(bandera_cifrada))[2:-1])
```

# Flag

`mblue{f3l1c1d4d35_p0r_tu_1ng3n13r1a_1nv3rs4!}`
