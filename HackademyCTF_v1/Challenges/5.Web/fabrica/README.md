# Statement

Una fábrica de galletas nos pidió que revisaramos si su aplicación para _admin_ es segura. ¿Será que las 5 cajas que nos darán como paga, valdrán la pena?

# Provided Files

N/A

# Procedure

After entering to the provided URL we can see another basic login page, with no visible extra info. The console is empty and there is no more visible clues available.

If we give a closer look to the statement and the page, there are many references to the cookie thing, so we proceed to check the page cookies. 

In the cookies section, we can see many cookies, but only one seems to be interesting for us, the `user_type`. This cookie has the value `user` that seems to be the default value as we tried to delete it and the site always returned the `user` value for this cookie.

![Step 1](https://res.cloudinary.com/dmrgfufa4/image/upload/v1604180361/writeups/HackademyCTF_v1/web_3_1.png)

Let's change the `user_type` cookie to another value than user, and the best intuitive value instead of `user` could be `admin`. After changing the value to `admin` we can see that another page is loaded with the flag inside it.

![Step 2](https://res.cloudinary.com/dmrgfufa4/image/upload/v1604180361/writeups/HackademyCTF_v1/web_3_2.png)

# Flag

`mblue{d3b3s_d3_t3n3r_cu1d4d0_c0n_tus_g4ll3t4s!}`

# Try it yourself!

```bash
docker run --rm -p 3000:3000 roeeyn/challenge_web_3
```
