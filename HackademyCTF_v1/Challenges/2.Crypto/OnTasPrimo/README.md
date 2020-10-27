# Statement

Después de investigar acerca de la encriptación y esas cosas esotéricas que nadie entiende, me decidí a implementar un algoritmo con un **secreto perfecto** que mi primo el Vernam me enseñó. Emocionado, cifré el primer mensaje de prueba y lo publiqué en Facebook para ganar unos cuantos "me enjaja".

> Publicación:
> mbleu{esta_no_es_una_bandera_asi_que_no_te_emociones_pero_estas_cerca} ->
> IS5YM0YkNkA3M2w6WwAhQAA4Xz5rLiZeNlQmLG8+QicbQiYmbig9azYpbCkhWzVaMD1WMA1DMUYwG1YsOVAsay8iQjFQKQ==

Posteriormente me di cuenta que podía ser un buen reto para este evento, y **sin modificar nada más**, cifré la bandera.

Bandera cifrada: **IS5YI1YkPQMcNgA2By11BywSQ2xBP3NCDV04eUZsQhE0ByF3bnU+aw0YY21tSQ==**

Como tengo secrecía perfecta, la bandera es indescifrable, ¿o no?

# Provided Files

```
cipher.py
```

# Procedure

The statement says that the cipher has perfect secrecy, and names Vernam. This suggests, with the title too, that this is uses a one time pad cipher.
This uses a key to xor it to a string (the flag) that we want to hide. The problem is that you shouldn't reuse the key because it can be very useful to decode another message.

The previous algorithm can be summarized in this way:

```
message xor key = encoded_message
```

This shows clearly that if we `xor` the encoded message with the original one, we can obtain the key.

If we do this it would result the following:

``` mbleu{esta_no_es_una_bandera_asi_que_no_te_emociones_pero_estas_cerca} xor IS5YM0YkNkA3M2w6WwAhQAA4Xz5rLiZeNlQmLG8+QicbQiYmbig9azYpbCkhWzVaMD1WMA1DMUYwG1YsOVAsay8iQjFQKQ== -> LL4V3_S3CR3T4_D3_M1_4LG0R1TM0_1ND3SC1FR4BL3LL4V3_S3CR3T4_D3_M1_4LG0R1T
```

We can see that it outputs the key.

Then we can use that key with the ciphered flag to get the original flag.

# Flag

`mblue{n0_d3b3r14s_r3us4r_ll4v3s_p4r4_3l_OTP!!}`
