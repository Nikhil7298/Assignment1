even=0
odd=0
for i in range(2,20):
  if i%2==0:
    even=even+1
  else:
    odd=odd+1
print('number of even',even)
print('number of odd',odd)