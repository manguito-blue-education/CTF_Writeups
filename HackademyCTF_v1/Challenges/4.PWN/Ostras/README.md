# Statement

¿De dónde son las mejores oSTRas?

# Provided Files

```
ostras
```

# Procedure

The name suggests that the challenge has some relation with the `strings` word. As this is a binary, we can execute the `strings` command to print every printable string included in the binary. This would be:

```bash
strings ./ostras
```

After this, the flag will be printed directly in the console. If we want to only print the flag, we can pipe the output from the `strings` command into `grep` command and search for only the flag.

```bash
# We know that the flag format is mblue{FLAG} so we
# only need to check for the initial characters

strings ./ostras | grep mblue{
```

# Flag

`mblue{b13nv3n1d0_4l_4n4l1s1s_d3_b1n4r10s}`
