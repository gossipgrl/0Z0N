import sys

def fast_input():
    return sys.stdin.readline().rstrip("\r\n")

def fast_output(x):
    sys.stdout.write(str(x))


n = int(fast_input())
pswds = set()

for i in range(n):
	pswd = list(fast_input())
	pswds.add(''.join(pswd))

	for i in range(len(pswd) - 1):
		pswd[i], pswd[i + 1] = pswd[i + 1], pswd[i] 
		pswds.add(''.join(pswd))
		pswd[i], pswd[i + 1] = pswd[i + 1], pswd[i]

m = int(fast_input())

for _ in range(m):
	new_pswd = fast_input()
	
	if new_pswd in pswds:
		fast_output(f"1\n")
	else:
		fast_output(f"0\n")

