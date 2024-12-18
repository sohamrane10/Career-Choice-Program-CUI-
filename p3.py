#CUI 

name = input("Enter your name ")

op = int(input("1 Job, 2 MS and 3 MBA "))
if op == 1:
	choice = "Job"
elif op == 2:
	choice = "MS"
else:
	choice = "MBA"
msg= " name = "+ name +" choice = "+ choice
print(msg)