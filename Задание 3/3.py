def message_set_handler():
    n = int(input())

    messages = []

    for _ in range(n):
        message = input()
        m_id, m_p = map(int, message.split()[0:2])
        m_text = ' '.join(message.split()[2:])
        messages.append([m_id, m_p, m_text])

    messages.sort(key=lambda x: x[0])

    sorted_messages = []
    current_parent = [-1]
    first_time = 1
    while messages:
        del_count = 0
        new_parent = []
        for i in range(len(messages)):
            if messages[i - del_count][1] in current_parent:
                new_parent.append(messages[i - del_count][0])
                add_value_to_sorted_messages(sorted_messages, messages.pop(i - del_count))
                del_count += 1
        current_parent = new_parent

        if first_time:
            messages.reverse()
            first_time = 0

    print_sorted_messages(sorted_messages)


def is_same_level_next(sorted_messages, ind):
    level = sorted_messages[ind][3]
    for i in range(ind + 1, len(sorted_messages)):
        if sorted_messages[i][3] < level:
            return 0
        if sorted_messages[i][3] == level:
            return 1
    return 0


def print_sorted_messages(sorted_messages):
    levels = [0 for _ in range(1000)]
    for ind, message in enumerate(sorted_messages):
        levels[message[3]] = 1

        for i in range(message[3]):
            if levels[i]:
                print("|", end=" ")
            else:
                print(" ", end=" ")
        print("")

        for i in range(message[3]):
            if levels[i]:
                print("|", end="")
            else:
                print(" ", end="")
            if i == message[3] - 1:
                print("-", end="")
            else:
                print(" ", end="")

        print(message[2])

        if message[3] != 0:
            levels[message[3] - 1] = is_same_level_next(sorted_messages, ind)


def add_value_to_sorted_messages(sorted_messages, message):
    if message[1] == -1:
        sorted_messages.append(message + [0])
        return
    parent_ind = -1
    for i in range(len(sorted_messages)):
        if sorted_messages[i][0] == message[1]:
            parent_ind = i
    sorted_messages.insert(parent_ind + 1, message + [sorted_messages[parent_ind][3] + 1])


for _ in range(int(input())):
	message_set_handler()