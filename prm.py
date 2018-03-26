fd=open("file.txt","r")
st=fd.read()
ls1=st.split()
for i in range(len(ls1)):
  ls2=int(ls1[i])
  if ls2 >= 2:
    for i in range(2, ls2):
        if (ls2 % i) == 0:
            print(ls2, "is not a prime number")
            break
    else:
        print(ls2, "is a prime number")
  else:
       print(ls2, "is not a prime number")
