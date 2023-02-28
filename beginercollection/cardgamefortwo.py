n = int(input())
cards = list(map(int, input().split()))
#sort
cards.sort(reverse=True)
alice = 0
bob = 0
alice_turn = True
for card in cards:
    if alice_turn:
        alice += card
        alice_turn = False
    else:
        bob += card
        alice_turn = True
print(alice - bob)