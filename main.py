

print("WELCOME TO MY CONSOLE APP")
print()
print()
file_name=input('ENTER COMPLETE FILE NAME: ')
print()
if ".txt" not in file_name:
	file_name = file_name + ".txt"

print('ENTER TEXT(enter "exit()" to terminate')
print()
with open(file_name,"w") as file:
	while True:
		line = input()
		if line == "exit()":
			break
		file.write(line + "\n")


