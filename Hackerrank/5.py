str=input()
substr=input()
cnt=0
for i in range (len(str) - len(substr)+1):
    if(str[i:i+len(substr)]==substr):
        cnt+=1;
print(cnt)