

print("WELCOME TO MY CONSOLE APP")
print()
print()
file_name=input('ENTER COMPLETE FILE NAME: ')
print()
print('ENTER TEXT(enter "exit()" to terminate')
print()
with open(file_name,"w") as file:
	while True:
		line = input()
		if line == "exit()":
			break
		file.write(line + "\n")


