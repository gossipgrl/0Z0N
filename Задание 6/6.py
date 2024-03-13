import sys
import queue

def fast_input():
    return sys.stdin.readline().rstrip("\r\n")

def fast_output(x):
    sys.stdout.write(str(x))


def handle_marks():
    n, m = map(int, fast_input().split())

    marks = []
    for _ in range(n):
        mark_row = []
        mark_row_str = input()
        for i in range(len(mark_row_str)):
            mark_row.append(int(mark_row_str[i]))
        marks.append(mark_row)

    if n == m == 2:
        max_value = 0
        x, y = 0, 0
        for i in range(2):
            for j in range(2):
                if max_value < marks[i][j]:
                    max_value = marks[i][j]
                    x, y = 2 - i, 2 - j

        fast_output(f"{x} {y}\n")
        return 

    q = queue.PriorityQueue()

    for i in range(n):
        for j in range(m):
            q.put((marks[i][j], i, j))

    min_value = 10
    row_skip = 0
    column_skip = 0
    value_for_return = []
    
    # Column
    value, row, column = q.get()
    value_for_return.append((value, row, column))
    while True:
        new_value, new_row, new_column = q.get()
        value_for_return.append((new_value, new_row, new_column))
        if new_row != row:
            min_value = get_min_value(marks, row, new_column)
            row_skip = row
            column_skip = new_column
            break

    for item in value_for_return:
        q.put(item)

    # Row
    value, row, column = q.get()
    while True:
        new_value, new_row, new_column = q.get()
        
        if new_column != column:
            if min_value < get_min_value(marks, new_row, column):
                row_skip = new_row
                column_skip = column
            break
            
    fast_output(f"{row_skip + 1} {column_skip + 1}\n")


def get_min_value(marks, i_skip, j_skip):
    min_value = 10
    for i in range(len(marks)):
        if i == i_skip:
            continue
        for j in range(len(marks[i])):
            if j == j_skip:
                continue
            min_value = min(min_value, marks[i][j])

    return min_value


n = int(fast_input())
for _ in range(n):
	handle_marks()