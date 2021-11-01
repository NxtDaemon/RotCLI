# RotCLI

NOTE: this maybe be added with multiple types of decryption <br><br>
RotCLI allows users to do rotational ciphers where K = 0 -> 26 ; this allows for streamlined bruteforcing <br>
this also allows you to do specific rotations.

## Usage

```
python3 RotCLI.py -m "message" -N key
python3 Rot.py -M "$(cat ../output)" -B
```

This script uses argparse to parse the input, due to the fact this will mostly by used while in a bash or zsh shell I have decided to not add an input file section to achieve the same result you can use the above syntax. As a default this code will use N=13 if the value of N is not given alongside it's flag e.g. `-N K` <br>

## Flags

```
-B | Bruteforce
-M | Message
-N | Rotational Value / Key
```

## Caesar Algorithm Implementation

This code follows the standard caesar algorithm <br>

```
C[i] - i-th character of the ciphertext
P[i] - i-th character of the plaintext
k - Shift value
m - Length of the alphabet (26)
```

This means encryption is done using the following <br>

```
T[i] = (C[i + k % 26)]
```

hence decryption is done using <br>

```
P[i] = T[i - (k % 26)]
```

it is worth noting that due to how most decryption methods work, they use wrap around values only using the encryption algorithm, since that K=-12 is the same as K=14 hence to fit in with this commonplace the script only uses the first mentioned method. <br>
