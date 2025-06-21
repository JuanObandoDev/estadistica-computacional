import random
import collections

VALUES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k']
SUITS = ['hearts', 'diamonds', 'clubs', 'spades']

def create_deck():
    decks = []
    for suit in SUITS:
        for value in VALUES:
            decks.append((suit, value))

    return decks

def get_hand(decks, hand_size=5):
    hand = random.sample(decks, hand_size)
    return hand

def main(hand_size=5, attempts=1):
    decks = create_deck()
    hands = []
    for _ in range(attempts):
        hand = get_hand(decks, hand_size)
        hands.append(hand)

    royal_flush = 0
    straight_flush = 0
    four_of_a_kind = 0
    full_house = 0
    flush = 0
    straight = 0
    three_of_a_kind = 0
    two_pair = 0
    pair = 0
    

    for hand in hands:
        values = []
        suits = []
        for card in hand:
            values.append(card[1])
            suits.append(card[0])

        if len(set(suits)) == 1:
            if sorted(values) == ['10', 'as', 'j', 'q', 'k']:
                royal_flush += 1
            elif len(set(values)) == 5 and (VALUES.index(max(values)) - VALUES.index(min(values)) == 4):
                straight_flush += 1
            else:
                flush += 1
        if len(set(values)) == 2:
            if max(collections.Counter(values).values()) == 4:
                four_of_a_kind += 1
            else:
                full_house += 1
        elif len(set(values)) == 3:
            if max(collections.Counter(values).values()) == 3:
                three_of_a_kind += 1
            else:
                two_pair += 1
        elif len(set(values)) == 4:
            pair += 1
        elif len(set(values)) == 5:
            if sorted(values) == ['10', 'as', 'j', 'q', 'k'] or sorted(values) == ['2', '3', '4', '5', '6']:
                straight += 1

    print(f"Royal Flush probability: {royal_flush / attempts:.4f}")
    print(f"Straight Flush probability: {straight_flush / attempts:.4f}")
    print(f"Four of a Kind probability: {four_of_a_kind / attempts:.4f}")
    print(f"Full House probability: {full_house / attempts:.4f}")
    print(f"Flush probability: {flush / attempts:.4f}")
    print(f"Straight probability: {straight / attempts:.4f}")
    print(f"Three of a Kind probability: {three_of_a_kind / attempts:.4f}")
    print(f"Two Pair probability: {two_pair / attempts:.4f}")
    print(f"Pair probability: {pair / attempts:.4f}")

if __name__ == "__main__":
    hand_size = int(input("Enter the hand size (default is 5): ") or 5)
    attempts = int(input("Enter the number of attempts (default is 1): ") or 1)
    main(hand_size, attempts)