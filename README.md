# Ascon
## Program options
I think that the issue I have is the sbox function. There are two differnent variations. One is called sbox and the other is called sbox_test. Sbox uses the software implementation that is in the documentation. The sbox_test does a similar operation but tries to remove the not operator from the operations. The issue with sbox is that it wants to use the ~ operater. However python does this operation in a incorrect format.
##example
we will take the binary number 10010100, which equals 148 and perform the not operator on it
### python code
```code
x =  148 binary= 0b10010100
~x= -149 binary -0b10010101
```
### c++ code
```code
x = 148 binary = 10010100
x = -149 binary = 11111111111111111111111101101011
```
~ is supposed to invert the binary digts and switch the binary digts, but it instead only adds 1 and puts a negative sign outfront. The not operater should operate like it does in c++ where each digit is inverted. 
