# Statement

Cuando ando atorado en un problema, me gusta ver vídeos sin razón como [éste](https://www.youtube.com/watch?v=jRu8VEZfo_Y).
Este video en particular me gustó tanto que lo descargué, y al verlo por 285va vez recordé lo que un mentor me dijo alguna vez.

> Cuando estés atorado en un problema, recuerda que el **duplicador de datos** debe llevar un tamaño de bloque 1, un salto de 420 y una cuenta de 57.

Espero que tú puedas entender lo que quiso decir, porque cuando lo dijo, estaba pensando en otro meme.

# Provided Files

```
no_pasa_nada_oiga.mp4
```

# Procedure

If we try to open the file (at least in Linux and MacOS) we can hear the sound of the video, but we can see no image. This can suggest to us that there is some corruption in the video, i.e. there is something hidden in the video.

If we take a closer look to the phrase in the statement, we can see something about `data duplicator`, a famous utility in unix systems to copy data from one file to another.

So we try the `dd` command with the given file and the provided parameters:

```
dd if=no_pasa_nada_oiga.mp4 of=something.txt bs=1 skip=420 count=57
```

After executing that command, we can get a file called `something.txt` (this can be any name) and it contains a string. We can assume it is a `base64` encoded string as it has both lowercase and uppercase letters and it ends in an equal sign.

```
bWJsdWV7eTRfbjBfZDNiM3IxNHNfdjNyX3Q0bnQwc19tM20zcyEhfQo=
```

After decoding this string, we can obtain the flag:

```
cat something.txt | base64 -d
```

# Flag

`mblue{y4_n0_d3b3r14s_v3r_t4nt0s_m3m3s!!}`
