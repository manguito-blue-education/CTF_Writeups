# Statement

Si te dijera que la bandera sí se ve, me creerías?

# Provided Files

N/A

# Procedure

If we open the page provided, we can see that there is nothing but a big button saying "Ten tu bandera" (obtain your flag). After clicking it, a GIF of Rick Astley shows up.

![Step 1](https://res.cloudinary.com/dmrgfufa4/image/upload/v1604180817/writeups/HackademyCTF_v1/web_1_1.png)

If we inspect that GIF container, we can see that the flag is just behind that GIF using a different z-index so it cannot be visible.

![Step 2](https://res.cloudinary.com/dmrgfufa4/image/upload/v1604180817/writeups/HackademyCTF_v1/web_1_2.png)

# Flag

`mblue{N3v3r_g0nna_g1v3_u_uP!}`

# Try it yourself!

```bash
docker run --rm -p 3000:80 roeeyn/challenge_web_1
```
