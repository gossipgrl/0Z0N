import sys
import json

def fast_input():
    return sys.stdin.readline().rstrip("\r\n")

def fast_output(x):
    sys.stdout.write(str(x))


def handle_files():
    n = int(fast_input())
    directory_str = ""

    for _ in range(n):
        directory_str += input().strip()
          
    directory = json.loads(directory_str)

    file_count, hacked_count = count_hacks(directory)
    print(hacked_count)
          
def count_hacks(directory):
    files_count, hacked_count = 0, 0
    is_hacked = 0
    if 'files' in directory.keys():
        for file_name in directory['files']:
            files_count += 1
            if (file_name.find('.hack') != -1):
                is_hacked = 1
    
    if 'folders' in directory.keys():
        for dir_name in directory['folders']:
            sub_files_count, sub_hacked_count = count_hacks(dir_name)
            files_count += sub_files_count
            hacked_count += sub_hacked_count
    
    if is_hacked:
        hacked_count = files_count

    return files_count, hacked_count


for _ in range(int(fast_input())):
	handle_files()