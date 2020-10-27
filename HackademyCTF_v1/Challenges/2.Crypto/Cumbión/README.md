# Statement

En uno de mis viajes a Tlalneplanta, acabé en un templo muy curioso en el que se percibían luces desde el exterior.
Cuandé escuché [el cumbión](https://www.youtube.com/watch?v=MGKSXPY6WLo) que empezó a sonar me decidí a entrar, pero un guardia con un viejo [nokia](https://es.wikipedia.org/wiki/Nokia_3310) me detuvo y me pregúnto la clave de acceso.
Afortunadamente me hice amigo de un miembro del templo que estaba afuera, y me dió esta imagen antes de irse.

¿Me puedes ayudar a descifrar la clave antes de que termine la canción?

# Provided Files

```
clave.png
```

# Procedure

The image shows the flag format `mblue{}` with some symbols inside it. After doing some quick review of the contents of the image we can see that there's nothing hidden inside the image, and that the flag is coded with this symbols.

After doing an image search, we can see that the symbols are part of the [cipher monk](https://es.wikipedia.org/wiki/The_Ciphers_of_the_Monks) universe, so we can proceed to decode them. This is the result:

```
888 2 6 666 7777 2 22 2 444 555 2 777
```

We may think that this is the flag, but it isn't. We now have to see the pattern of the result, and see that there's no zero nor ones, and that all the numbers are repeated a certain amount of times. 

After reading again the statement we can see a reference to an old Nokia, so with this we may think that this is a [phone keypad cipher](https://www.dcode.fr/multitap-abc-cipher). After doing the decoding of this type of cypher, we can get the decoded symbols.

`v a m o s a b a i l a r`

# Flag

`mblue{vamosabailar}`
