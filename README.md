# FileCrypto - Python 3 GUI application to encrypt files with the Vigenère Cipher

<h2> WARNING: DO NOT USE THIS CODE ON PRODUCTION </h2>

<h3> Lincese notice for the icon used</h3>
<a href="https://commons.wikimedia.org/wiki/User:D.s.m(h)">D.s.m(h)</a>, <a href="https://commons.wikimedia.org/wiki/File:P_cryptography.png">P cryptography</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0/legalcode" rel="license">CC BY-SA 3.0</a>

<p> My biggest project so far: A Python 3 script able to encrypt any type of file using a cipher similar to the original Vigenère Cipher. This cipher was designed only to be applied on text, so to encrypt other types of files, like images, videos or any kind of files available on a binary format, FileCrypto first encode all of the data into a base64 bytes object, then creates a list with the ASCII values of each base64 symbol. That way it is possible to apply the cipher and finally decode back to the binary that is going to be written on a file somewhere.</p>

<p>The algebric representation of the cipher is as follow:</p>
<ol>
    <li> To encrypt a letter: C = (P + K) mod64 </li>
    <li> To decrypt a letter: P = (C - K) mod64 </li>
</ol>

<p> Where C is the ciphertext, P is the plaintext and K is the key letter. Note that in the original cipher, the modulus would be 26 as the alphabet has 26 letters, but in this case, there is 64 symbols due to the base 64 encoding, so de modulus needs to be 64. Also, the key should be the same size as the message, so it will be often replicated over and over to achieve this. If the key is LEMON, it will repeat LEMONLEMONLEMON.. until it is the same size as the text to be converted.</p>

<p> Final considerations: Initially, I designed this script to encrypt and decrypt image files, but it turns out that my algorithm is able to really encrypt any kind of file because all files can be represented in a binary form. Perhaps there are some references to this in some of my comments in the source code, but I'll fix later.</p>
