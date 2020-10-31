# Statement

Alan está entusiasmado con la idea de JuanDrive, y se propuso a armar un registro para aquellos interesados en la plataforma.
Él aprendió del error de Fernando, y ya usó tecnologías más recientes, aparte de que programó un algoritmo para evitar que bots usen el registro y lo puedan hackear.
¿Será que ya la plataforma es segura?

# Provided Files

```
main.py
```

# Procedure

If we take a look, the server just execute the `main.py` in every connection. So if we took a look at this script, we can see that it uses `python3` because the print functions uses parenthesis.

After testing the script, we can see that it requests a math operation to verify if you're human or not. If we take closer look, we can see that this operation is executed in the `eval` function, and compared to the original number, so the `eval` function is the vulnerable part of this challenge.

We can see that the input is passed directly to the `eval` function, so if we write `os.system("/bin/bash")` we can obtain a shell and interact with the system. To list the files we can use `ls` and to print the content of the `bandera.txt` file we can use `cat bandera.txt`.

We could have used directly `os.system("cat bandera.txt")` but it's more fun to obtain a shell.

# Flag

`mblue{nunc4_c0nf13s_3n_l4s_entr4d4s_d3l_usu4r10}`
