# Statement

Pusiste atención a los repasos?

# Files Provided

```
flag.txt
```

# Procedure

As the name suggests, we have to do a pipeline of different encoding styles. In this case the first one is obvious as we only have 0s and 1s. So the first step is to convert from binary to ASCII. We can use the [online binary to ASCII converter](https://www.rapidtables.com/convert/number/binary-to-ascii.html) we used before to obtain the following string:

```
TlZSR1k1TEZQTlJYRU1aUUw1WVhLTTI3R05aWElORFRMNVdHUzQzVUlBUVgyQ1E9Cg==
```

After giving a closer look to it, we can see that it contains upper and lowercase letters, and also ends in 2 equal signs, so it suggests that it is a base64 encoded string. After using the [online base64 decoder](https://www.base64decode.org/) we used in the previous challenges, we can obtain the following string:

```
NVRGY5LFPNRXEMZQL5YXKM27GNZXINDTL5WGS43UIAQX2CQ=
```

After giving a closer look to the new string, we can see that it is all uppercase letters and ends in an equal sign, so it suggests that it is a bae32 encoded string. After using the [online base32 decode](https://emn178.github.io/online-tools/base32_decode.html) we used before, we can obtain the flag.

We can use the Linux pipes too, but I didn't found an easy tool to convert from binary to ASCII in the command line, so it could be something like this:

```
CONVERTED_ASCII_FROM_BINARY | base64 -d | base32 -d
```

# Flag

`mblue{cr30_qu3_3st4s_list@!}` 

