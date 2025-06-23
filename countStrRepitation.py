s1 = "abcbcbcb"
s2 = "cbc"
index_s = 0
count = 0
for i in range(len(s1)):
    if(s1.find(s2,index_s,index_s + len(s2)) != -1):
        count+=1
    index_s +=1        
print("The Count is : ",count)
