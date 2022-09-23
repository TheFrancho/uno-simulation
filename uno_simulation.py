import random

COLOURS = ['Red', 'Blue', 'Yellow', 'Green']

NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ZEROS = [0]
SPECIAL_CARDS = ['Skip', 'Reverse', '+2']
WILDCARDS = ['Wildcard', 'Wildcard +4']

def create_deck():
    zeros_deck = []
    numbers_deck = []
    specials_deck = []
    wildcards_deck = []
    for color in COLOURS:

        for zeros in ZEROS:
            zeros_deck.append((color, zeros))

        for number in NUMBERS:
            numbers_deck.append((color, number))

        for special in SPECIAL_CARDS:
            specials_deck.append((color, special))

    for wildcard in WILDCARDS:
        wildcards_deck.append(('Wildcard', wildcard))

    numbers_deck *= 2
    specials_deck *=2
    wildcards_deck *= 4

    deck = zeros_deck + numbers_deck + specials_deck + wildcards_deck

    return deck

def get_hand(deck, hand_size):
    hand = random.sample(deck, hand_size)
    return hand

def at_least_one_plus_for(hands):
    check_wildcard = False
    for hand in hands:
        if hand[1] == 'Wildcard +4':
            check_wildcard = True
            break
    return check_wildcard

def all_wildcards(hands):
    check_wildcard = 0
    for hand in hands:
        if hand[0] == 'Wildcard':
            check_wildcard+=1
    return True if check_wildcard / len(hands) == 1 else False

def no_wildcards(hands):
    no_wildcards = True
    for hand in hands:
        if hand[0] == 'Wildcard':
            no_wildcards = False
            break
    return no_wildcards

def all_same_colour(hands):
    colours = {
        'Red': 0, 
        'Blue' : 0, 
        'Yellow' : 0,  
        'Green' : 0,
        'Wildcard' : 0
    }
    for hand in hands:
        colours[hand[0]] +=1
    
    for color_value in colours.values():
        if color_value / len(hands) == 1:
            return True
    return False

def all_plus_four(hands):
    plus_four_counter = 0
    for hand in hands:
        if hand[1] == 'Wildcard +4':
            plus_four_counter += 1
    if plus_four_counter / 4 == 1:
        return True
    return False

def main(tries = 1000000, hand_size = 7):
    deck = create_deck()
    all_hands_generated = []

    at_least_one_plus_four_counter = 0
    all_wildcards_counter = 0
    no_wildcards_counter = 0
    all_same_colour_counter = 0
    all_plus_four_counter = 0

    for _ in range(tries):
        hand  = get_hand(deck, hand_size)
        all_hands_generated.append(hand)
    
    #for each hand generated
    for hand in all_hands_generated:
        #Check if there is a single wildcard on your hand
        at_least_one_plus_four_counter += at_least_one_plus_for(hand)
        #Check if your hand is full of wildcards
        all_wildcards_counter += all_wildcards(hand)
        #check if your hand does not have a single wildcard
        no_wildcards_counter += no_wildcards(hand)
        #check if all your cards are of the same colour
        all_same_colour_counter += all_same_colour(hand)
        #check if you got all the +4 of the game
        all_plus_four_counter += all_plus_four(hand)
    
    print(f'Over {tries} tries in a deck of {hand_size} cards: \n')
    
    print(f'Total predictions for at least one +4 in your deck: {0 if not at_least_one_plus_four_counter else at_least_one_plus_four_counter}')
    print(f'It is about {round(100*(at_least_one_plus_four_counter / tries), 2)}% of your average games\n')
   
    print(f'Total predictions for only wildcards in your deck: {0 if not all_wildcards_counter else all_wildcards_counter}')
    print(f'It is about {round(100*(all_wildcards_counter / tries), 2)}% of your average games\n')  
    
    print(f'Total predictions for no wildcards in your deck: {0 if not no_wildcards_counter else no_wildcards_counter}')
    print(f'It is about {round(100*(no_wildcards_counter / tries), 2)}% of your average games\n')
    
    print(f'Total predictions for all cards of the same colour: {0 if not all_same_colour_counter else all_same_colour_counter}')
    print(f'It is about {round(100*(all_same_colour_counter / tries), 2)}% of your average games\n')

    print(f'Total predictions for getting all the +4 in your deck: {0 if not all_plus_four_counter else all_plus_four_counter}')
    print(f'It is about {round(100*(all_plus_four_counter / tries), 2)}% of your average games\n')

    
if __name__ == '__main__':
    main()