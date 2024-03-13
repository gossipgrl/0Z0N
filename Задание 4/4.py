import sys

def fast_input():
    return sys.stdin.readline().rstrip("\r\n")

def fast_output(x):
    sys.stdout.write(str(x))


def handle_log():
    n = int(fast_input())
    log = fast_input()
    
    dct = {}
    dct['X'] = 0
    dct['Y'] = 0

    x_in_stack_count = 0
    y_in_stack_count = 0
    x_count = log.count('X')
    y_count = log.count('Y')
    z_count = log.count('Z')

    for let in log:
        if let == 'X':
            x_count -= 1
            x_in_stack_count += 1
            dct['X'] += 1
        elif let == 'Y':
            y_count -= 1
            if (x_in_stack_count + x_count + y_in_stack_count < y_count + z_count):
                dct['Y'] += 1
                y_in_stack_count += 1
                continue
            if dct['X'] != 0:
                dct['X'] -= 1
                x_in_stack_count -= 1
            else:
                y_in_stack_count += 1
                dct['Y'] += 1 
            
        elif let == 'Z':
            ind = -1
            z_count -= 1
            if dct['Y'] != 0:
                dct['Y'] -= 1
                y_in_stack_count -= 1
                continue
            if dct['X'] != 0:
                dct['X'] -= 1
                y_in_stack_count -= 1
                continue
            fast_output("No\n")
            return


    if dct['X'] + dct['Y'] == 0:
        fast_output("Yes\n")
    else:
        fast_output("No\n")


n = int(fast_input())
for _ in range(n):
	handle_log()