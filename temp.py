

CONSTANTS_a= ['00000000000000f0', '00000000000000e1','00000000000000d2','00000000000000c3','00000000000000b4','00000000000000a5', '0000000000000096','0000000000000087','0000000000000078', '0000000000000069', '000000000000005a', '000000000000004b' ]
CONSTANTS_b= [0x96,0x87,0x78,0x69,0x5a,0x4b]
def convertToHex(hexText, base, bitSize):
    
    binText = hex(int(hexText))
    if(hexText > 0):
        binText = binText[2:] # removes the 0x from binary number
    else:
        binText = binText[3:] # removes the -0x from binary number
    binText = binText.zfill(bitSize) # makes it bitsize bits long
    return binText
# makes all of s strings of hex
def stateToHex(s):
    temp =[0,0,0,0,0]
    temp[0] = hex(s[0])
    temp[1] = hex(s[1])
    temp[2] = hex(s[2])
    temp[3] = hex(s[3])
    temp[4] = hex(s[4])
    return temp
    
# prints the state 
def printState(s):
    temp = stateToHex(s)
    print("state: "),
    for i in temp:
        print(i)
    print('')
# adds the constant to x2 of s
def addConstant_a(s, num):
    s[2] = (s[2]) ^ int(CONSTANTS_a[num],16)
def sBox(s):

    s[0] ^= s[4]
    s[4] ^= s[3]
    s[2] ^= s[1]
    print(s[2])
    t0 = s[0]
    t1 = s[1]
    t2 = s[2]
    t3 = s[3]
    t4 = s[4]
    print(t2,s[2])
    t0 = ~t0
    t1 = ~t1
    t2 = ~t2
    t3 = ~t3
    t4 = ~t4
    print(t2,s[2])
    #print("T's_A1: ",(t0),t1,t2,t3,t4,"\nS:",s)
    t0 &= s[1]
    t1 &= s[2]
    t2 &= s[3]
    t3 &= s[4]
    t4 &= s[0]
    print(t2,s[2])
    #print("T's_B2: ",(t0),t1,t2,t3,t4,"\nS:",s)
    s[0] ^= t1
    s[1] ^= t2
    s[2] ^= t3
    s[3] ^= t4
    s[4] ^= t0
    #print("T's_A2: ",(t0),t1,t2,t3,t4,"\nS:",s)
    s[1] ^= s[0]
    s[0] ^= s[4]
    s[3] ^= s[2]
    s[2] = ~s[2]
    
    #print("T's_3: ",(t0),t1,t2,t3,t4,"\nS:",s)
def sBox_test(s):
    
    s[0] ^= s[4]
    s[4] ^= s[3]
    s[2] ^= s[1]
    #print(s)
    t0 = s[0]
    t1 = s[1]
    t2 = s[2]
    t3 = s[3]
    t4 = s[4]
    #print("T's_B: ",bin(t0),t1,t2,t3,t4,"\nS:",s)
    t0 ^= 1
    t1 ^= 1
    t2 ^= 1
    t3 ^= 1
    t4 ^= 1
    #print("T's_A: ",bin(t0),t1,t2,t3,t4,"\nS:",s)
    t0 &= s[1]
    t1 &= s[2]
    t2 &= s[3]
    t3 &= s[4]
    t4 &= s[0]
    #print("T's_B: ",bin(t0),t1,t2,t3,t4,"\nS:",s)
    s[0] ^= t1
    s[1] ^= t2
    s[2] ^= t3
    s[3] ^= t4
    s[4] ^= t0
    #print("T's_B: ",bin(t0),t1,t2,t3,t4,"\nS:",s)
    s[1] ^= s[0]
    s[0] ^= s[4]
    s[3] ^= s[2]
    s[2] ^= 1
    #print("T's_B: ",bin(t0),t1,t2,t3,t4,"\nS:",s)
def shiftRbyn(bits, n):
    #print("before shift", bin(bits))
    #print(bin((bits) >> n))
    #print(bin((bits) << (64-n)))
    temp = (((bits) >> n) ^ ((bits) << (64-n)))
    #print("after shift", bin(temp))
    return temp
def shiftRbyn_test(bits, n):
    #print("H: ",bits,n)
    binText = bin((bits))
    # removes the 0b from binary number
    if(bits >= 0):
        binText = binText[2:]
    else:
        binText = binText[3:] 
    #print('\tSHIFT TEST: '+ binText + '\n| after: ' + binText[len(binText)-n::] + binText[:len(binText)-n:])
    return int(binText[len(binText)-n::] + binText[:len(binText)-n:],2)
def linear(s):
    printState(s)
    temp = shiftRbyn_test(s[0],19)
    #print("temp",temp)
    temp2 = shiftRbyn_test(s[0],28)
    #print("temp2",temp2)
    s[0] = (s[0]) ^ (temp) ^ (temp2)
    #print(s[0])
    temp = shiftRbyn_test(s[1],61)
    temp2 = shiftRbyn_test(s[1],39)
    s[1] = (s[1]) ^ (temp) ^ (temp2)
    #print(s[1])

    temp = shiftRbyn_test(s[2],1)
    temp2 = shiftRbyn_test(s[2],6)
    s[2] = (s[2]) ^ (temp) ^ (temp2)
    #print(s[2])

    temp = shiftRbyn_test(s[3],10)
    temp2 = shiftRbyn_test(s[3],17)
    s[3] = (s[3]) ^ (temp) ^ (temp2)
    #print(s[3])
    temp = shiftRbyn_test(s[4],7)
    temp2 = shiftRbyn_test(s[4],41)
    s[4] = (s[4]) ^ (temp) ^ (temp2)
    #print(s[4])
def permutation_a(s, num):
    for i in range(num):
        addConstant_a(s, i)
        print("add Constant")
        printState(s)
        sBox_test(s)
        print("sBox")
        printState(s)
        linear(s)
        print("Linear")
        printState(s)

def initialization(s,key_1, key_2):
   permutation_a(s,12)
   s[0] = (s[0]) ^ 0
   s[1] = (s[1]) ^ 0
   s[2] = (s[2]) ^ 0
   s[3] = (s[3]) ^ key_1
   s[4] = (s[4]) ^ key_2
   stateToHex(s)
   print("Init")
   printState(s)
    

def main():
    IV =  0x80400c0600000000
    key_1 = 0x0000000000000000
    key_2 = 0x0000000000000000
    nonce_1 = 0x0000000000000000
    nonce_2 = 0x0000000000000000

    s = [IV, key_1,key_2 ,nonce_1,nonce_2]
    print(s)
    printState(s)
    initialization(s,key_1, key_2)

    


if __name__ == '__main__':
    main()