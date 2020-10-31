# Statement

Nos enteramos que una banda dedicada al tráfico de memes, recibió nueva mercancía.
La policía cibernética pudo interceptar parte de su tráfico web, y te necesitan para encontrar el nuevo meme.
¡Ayúdalos!

# Provided Files

```
intercepted_traffic.pcapng
```

# Procedure

This one was very straight forward. In the statement says clearly we're looking for an image. So we open the `.pcapng` file and look for all the interactions that could result in an image. 

For this, we open `File > Export Objects > HTTP` (we are assuming HTTP, but we have no clue until now that it is with this protocol).

After this we can see a list of objects that can be exported from the traffic, and from the list we can see one that in the `Content Type` column it says it is a `image/png`. We export this and we can see the meme with the flag.

# Flag

`mblue{w1r3sh4rk_3s_b4s1c0_p4r4_MITM}`
