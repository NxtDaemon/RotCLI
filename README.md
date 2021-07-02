# RotCLI 
RotCLI allows users to do rotational ciphers where K = 0 -> 26  ; this allows for streamline bruteforcing <br>
this also allows you to do specific rotations and this maybe be added with multiple types of decryption 


## Usage
`python3 RotCLI.py -m "message" -N key` 
as a default this code with use N=13 or the same as Rot-13 <br>

## Flags 
```
-B | Bruteforce
-M | Message
-N | Rotational Value / Key
```

## Caesar Algorithm Implementation
this code follows the standard caesar algorithm <br>

```
C[i] - i-th character of the closed text <br>
T[i] - i-th character of the open text <br>
k - shift <br>
m - length of the alphabet <br>
```

`T[i] = (C[i] - k) mod M`
