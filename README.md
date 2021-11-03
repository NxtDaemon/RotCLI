# RotCLI

NOTE: this maybe be added with multiple types of decryption <br><br>
RotCLI allows users to do rotational ciphers where K = 0 -> 26 ; this allows for streamlined bruteforcing <br>
this also allows you to do specific rotations.
<br>

## Usage

```
python3 RotCLI.py -m "message" -N key # For direct N=key
python3 Rot.py -M "$(cat ../output)" -B # Bruteforcing All Keys
python3 Rot.py -M "$(cat test.txt)" -B -L # For Large Sample Size
```

This script uses argparse to parse the input, due to the fact this will mostly by used while in a bash or zsh shell I have decided to not add an input file section to achieve the same result you can use the above syntax. As a default this code will use N=13 if the value of N is not given alongside it's flag e.g. `-N K` <br>
<br>

## Flags

```
-M | Pass the Message to run through the rotational cipher
-N | Pass the N-rotational value [Default is 13]
-B | Switch for bruteforce the N-val
-L | Switch for Letter-Goodness
```

<br>

## Output

```
python3 Rot.py -M "$(cat ../file)" -N 14
[🔑] -> 14
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
        ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullam
        co laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit
         in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat c
        upidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```

```
python3 Rot.py -M "$(cat test.txt)" -B -L
[*] - Printing Message with Highest Letter Goodness

[🔑] -> 19 [43.06239999999993]
        Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph
        is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and
         coherence of ideas among sentences is what constitutes a paragraph. A paragraph is defined as “a group of sen
        tences or a single sentence that forms a unit” (Lunsford and Connors 116). Length and appearance do not determ
        ine whether a section in a paper is a paragraph. For instance, in some styles of writing, particularly journal
        istic styles, a paragraph can be just one sentence long. Ultimately, a paragraph is a sentence or group of sen
        tences that support one main idea. In this handout, we will refer to this as the “controlling idea,” because i
        t controls what happens in the rest of the paragraph.

[?] - Do you Want to Print the Next Value? q

[$] - Hope you Got your Result ／人◕ __ ◕人＼
```

<br>

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
