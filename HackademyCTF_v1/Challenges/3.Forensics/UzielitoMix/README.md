# Statement

Hablando de Luis, él siempre tendrá marcado el momento en el que Uzielito Mix y Pablito Mix hicieron un dueto en el EDC.
¿Puedes descubrir qué mensaje dejó en la imagen?

# Provided Files

```
back_to_back.png
```

# Procedure

If we open the file provided we can see it's just a simple image. The first thing I would do would be to look for metadata in the file. In this case, one of the best tools to obtain metadata from an image would be `exiftool`. 

If we run:

```
exiftool back_to_back.png
```

We can see that there is one attribute that is called `Bandera` and it contains the flag.

# Flag

`mblue{3l_3g0_h4st4_3l_c13l0_y_3l_p3rr30_h4st4_3l_su3l0}`

