dct = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13,
       'A': 14}


def get_deck_power(cards):
    temp_value = [card[0] for card in cards]

    max_value = 0
    max_count = 0

    for card in cards:
        value = dct[card[0]]
        count = temp_value.count(card[0])
        if count > max_count:
            max_count = count
            max_value = value
            continue
        if value > max_value and count == max_count:
            max_value = value
            continue

    result = 0
    for i in range(max_count):
        result *= 15
        result += max_value

    return result



for _ in range(int(input())):

	cards_left = []

	# Initialize deck
	for value in ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']:
		for suit in ['S', 'C', 'D', 'H']:
			cards_left.append(value + suit)

	# Read players cards and delete them from the deck
	players_cards = []
	n = int(input())
	for i in range(n):
		players_cards.append(input().split())
		cards_left.remove(players_cards[i][0])
		cards_left.remove(players_cards[i][1])

	# Calculate count of win conditions
	win_conditions = []
	for i in range(len(cards_left)):
		card = [cards_left[i]]
		my_power = get_deck_power(players_cards[0] + card)
		flag = 1
		for j in range(1, n):
			if get_deck_power(players_cards[j] + card) > my_power:
				flag = 0
				break
		if flag:
			win_conditions.append(card)

	print(len(win_conditions))
	for card in win_conditions:
		print(*card)