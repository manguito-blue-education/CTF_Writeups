# Statement

De vez en cuando es bueno darse un respiro. En esta imagen viene una muy buena sugerencia para tu siguiente descanso, ¿puedes ver cuál es?

# Provided Files

```
zima_blue.png
```

# Procedure

If we try to open the image (at least in unix based systems) it would open to an empty image, or a weird blue one. This suggests that something is broken within the image.

If we run:

```
exiftool zima_blue.png
```

We can see that there is a warning attribute that says that it is a corrupted PNG. This suggests that there is something inside the file itself that cannot coexist without breaking the file.

If we open the image with an editor, like `vim zima_blue.png` or with any editor that let us see the unicode symbols. We can see a "comment" that says:

```
CREISTE QUE SERIA TAN FACIL? ----->
```

After giving a second look, we can see that there is a repeated header in line 6, so it means that the first header is useless. So if we delete the first 5 lines from the file and then save it. We can open it as a normal image.

# Flag

`mblue{5ug3r3nc14:_l0v3_d34th_4nd_r0b0t5}`
