num = int(input( ))
result=[]
count=0

for i in str(num):
    result.append(int(i))

while len(result) != 1:
    total = sum(result)
    
    result = list(map(int,str(total)))
    count += 1
    
print(count)