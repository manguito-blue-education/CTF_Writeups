# Statement

Dicen en Los Mochis que sólo los chidos pueden obtener la bandera.

# Provided Files

N/A

# Procedure

If we enter the URL provided, we could see a basic login page, with username and password inputs. If we open the inspector to try to investigate a little more about the application, we can see that there is an interesting console log:

![Step1](https://res.cloudinary.com/dmrgfufa4/image/upload/v1604179648/writeups/HackademyCTF_v1/web_2_1.png)

```
No eres chido, eres Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36
```

This suggests that the agent have to be changed, as the statement says that only the 'chido's could obtain the flag. So if we change the agent, we obtain another page, with the flag in it.

To change the agent in Chrome, you need to go inside the Dev tools > More Tools > Network Conditions, and then select the custom agent option.


![Step 2](https://res.cloudinary.com/dmrgfufa4/image/upload/v1604179648/writeups/HackademyCTF_v1/web_2_2.png)

![Step 3](https://res.cloudinary.com/dmrgfufa4/image/upload/v1604179648/writeups/HackademyCTF_v1/web_2_3.png)

# Flag

`mblue{l0_un1c0_ch1d0_s0n_l4s_t0rt4s_d3_t4m4l}`

# Try it yourself!

```bash
docker run --rm -p 3000:3000 roeeyn/challenge_web_2
```
