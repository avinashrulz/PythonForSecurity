f = open("D:/Downloads/"+"access_log.txt", "r")

# User input to search the required IP Address
strIpAdd = input("enter the IP address to search: ")

#Assuming that the log file consists of records in the following format:
#<ip address> - <other details>

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