thm = int(0)
print("Enter the Number of Requests : ") #Number of I/O Requets
req = int(input())
print("Enter the Initial Head Position : ") #Initial position of Head
hp = int(input())
pos = hp
print("Enter the Seek Rate : ")
srate = int(input())
print("Enter the Requests : ")
arr = [ int(input()) for i in range(req)]
start = min(arr)
end = max(arr) #Start and End of Head Positions
print(hp, end='')
if(hp<100):
    for i in range(pos, start-1, -1):
        if i in arr:
            thm+= abs(pos-i)
            pos = i
            print(" -> ",i, end='')
            arr.remove(i)
    thm+= abs(pos-start)
    pos = end
    print(" -> ", start, end='')
    print(" -> ", end, end='')
    for i in range(end, hp+1, -1): #Scans back to start
        if i in arr:
            thm+= abs(pos-i)
            pos = i
            print(" -> ", i, end='')
            arr.remove(i)
else:
    for i in range(pos, end+1):
        if i in arr: 
            thm+= abs(pos-i)
            pos = i
            print(" -> ", i, end='')
            arr.remove(i)
    thm+= abs(pos-end)
    pos=end
    print(" -> ", end, end='')
    for i in range(start,hp+1):
        if i in arr:
            time+=abs(pos-i)
            pos=i
            print(" -> ",i, end='')
            arr.remove(i)
stime = thm * srate
print("\nThe Total Head Movement is",thm)
print("The Seek Time is",stime)