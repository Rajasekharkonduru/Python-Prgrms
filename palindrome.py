
str=input("Enter a string:")
s=str.lower()
l=[]
for i in s:
	if i.isalnum():
		l.append(i)
rev = l[::-1]
if l==rev:
	print("palindrome")
else:
	print("not a pal")