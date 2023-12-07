# AoC Day 4.1

sum_scores = 0

with open('2023/Day04/input.txt', 'r') as f:
    for card in f:
        card_score = 0
        common = 0
        winning_numbers = set()
        card_numbers = set()
        card = card[5:]
        cardnumber = int(card.split(':')[0].strip())
        card = card.split(':')[1].strip()
        
        winning_nums = card.split(' | ')[0].split(' ')
    
        for item in winning_nums:
            if len(item) == 0:
                pass
            else:
                winning_numbers.add(int(item))
        
        card_nums = card.split(' | ')[1]
        card_nums = card_nums.split(' ')
        
        for item in card_nums:
            if len(item) == 0:
                pass
            else:
                card_numbers.add(int(item))
        common = card_numbers.intersection(winning_numbers)
        
        if len(common) == 1:
            card_score = 1
        elif len(common) > 1:
            card_score = 2**(len(common)-1)

        sum_scores += card_score
    print(sum_scores)