# Statement

Todos nosotros tenemos un amigo con gustos raros, en nuestro caso se llama Luis. Él ha guardado este archivo que revela la identidad de su artista favorito. ¡Descúbrelo! y Luis, aún así te queremos 😜

# Provided Files

```
artista_secreto.txt
```

# Procedure

After looking to the given file, we can see that it is a very big string that is probably encoded in a bas64 format. We can see this because we can see that there are no weird unicodes in the string, there are uppercase and lowercase string. 

There is a *one liner* that can solve this and it is:

```
cat artista_secreto.txt | base64 -d | imgcat
```

It puts the content of the `artista_secreto.txt` file into the `base64` utility and it passes it to the `imgcat` command. Another way to do it is to use an online tool to do this such as [this](https://www.base64decode.org/) which let you decode files and download the result.

# Flag

`mblue{4lv_c0n_l0s_gust0s_d3l_lu1s}`
