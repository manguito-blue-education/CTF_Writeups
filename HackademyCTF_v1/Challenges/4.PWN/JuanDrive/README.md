# Statement

Fernando como buen emprendedor decidió hacer su propio servicio de almecenamiento en la nube llamado "JuanDrive".
El problema es que hace ya muchos años que no programa, y se aferra a usar tecnologías obsoletas.
¡Demuéstrale que esas tecnologías ya no son seguras!

```
nc IP_ADDRESS PORT
```

# Provided Files

```
login.py
```

# Procedure

After connecting to the provided IP address, we can see that it executes the `login.py` file with each connection. So if we take a look at this file, we can see that it is using `python2.7` as the print functions doesn't contain the parenthesis. Also, we can see that it is using the `input` function to receive the info from the user.

This is the vulnerable thing from this script as this function, with this python version, will not parse anything. We can test this by executing the python script and writing something without the quotes. The output should be something similar to "your_input is not defined".

To exploit this we can abuse some of the already imported libraries, in this case `os`. In the input of the script we can write `os.system("/bin/bash")`, so the script will execute bash and give us a terminal.

Inside this terminal, we can type `ls` to see the folder content, and then `cat bandera.txt` to print the content of the flag. 

We could have written directly `os.system("cat bandera.txt")`, but I think it's more fun to obtain a shell and interact with all the vulnerable system.

# Flag

`mblue{y4_n0_d3b3r14s_us4r_pyth0n2_ch4t0!!!}`
