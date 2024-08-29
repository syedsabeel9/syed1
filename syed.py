import math
p=3
q=7
n=p*q
print("n=",n)
phi=(p-1)*(q-1)
e=2
while(e<phi):
    if(math.gcd(e,phi)==1):
        break
    else: 
        e +=1
        print("e =",e)
        k=2
        d=((k*phi)+1)/e
        print("d =",d)
        print(f'public key:{e, n}')
        print(f'public key:{d, n}')
        msg=11
        print(f'original message:{msg}')
        c=pow(msg,e)
        c=math.fmod(c,n)
        print(f'encrypted message:{c}')
        m=pow(c,d)
        m=math.fmod(m,n)
        print(f'decrypted message:{m}')