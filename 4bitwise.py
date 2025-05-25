#Python Bitwise Operators
#Python Bitwise operator works on b#its and performs bit by bit operation. These operators are used to compare binary numbers.
a = 20            
b = 10            

print ('a=',a,':',bin(a),'b=',b,':',bin(b))
c = 0

c = a & b;        
print ("result of AND is ", c,':',bin(c))

c = a | b;     
print ("result of OR is ", c,':',bin(c))

c = a ^ b;        
print ("result of EXOR is ", c,':',bin(c))

c = ~a;           
print ("result of COMPLEMENT is ", c,':',bin(c))

c = a << 2;       
print ("result of LEFT SHIFT is ", c,':',bin(c))

c = a >> 2;       
print ("result of RIGHT SHIFT is ", c,':',bin(c))