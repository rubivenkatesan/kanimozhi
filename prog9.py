num= int(raw_input())
sum=0
if(num<=0):
	print("enter a positive number")
for i in range(1,num+1):
	sum=sum+i
print(sum)
