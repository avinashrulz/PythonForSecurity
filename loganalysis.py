f = open("D:/Downloads/"+"access_log.txt", "r")
#lines = f.readlines()

strIpAdd = input("enter the IP address to search: ")

for line in iter(f):
    ip = line.split(" - ")[0]
    if ip == strIpAdd:
        print (line)

#SECOND METHOD
# lines = f.readlines()
# for ip in lines:
#    if ip.find(userinput) != -1:
#       print (ip)

#print(lines[2])
f.close()