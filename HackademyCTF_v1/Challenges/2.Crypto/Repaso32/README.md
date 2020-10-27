# Statement

Los números son la BASE de todo.

# Files Provided

```
flag.txt
```

# Procedure

After viewing the `flag.txt` we can see that it is an encoded string that probably contains the flag. After giving a closer look, we can see that the string ends in more than 2 equal signs `=` and all letters are uppercase, discarding the base64 encoding. The most popular encoding technique that let the result ends in more than 2 equal signs is the base32 encoding (the title of the challenge can confirm this hypothesis).

After using an [online base32 decode](https://emn178.github.io/online-tools/base32_decode.html) we can copy and paste there the content of the txt file and get the flag.

# Flag

`mblue{ll3v4s_bu3n_r1tm0_y4_h4b14s_h3ch0_3st0?}` 
