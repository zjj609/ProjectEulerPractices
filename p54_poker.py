from collections import Counter

file_url = open(r'G:\\test_c\\projectEuler\\p054_poker.txt')
hands = (line.split() for line in file_url.readlines())
#line = '8C TS KC 9H 4S 7D 2S 5D 3S AC'
#hands = line.split()

#print hands

values = {r:i for i,r in enumerate('23456789TJQKA', start=2)}
straights = [(v, v-1, v-2, v-3, v-4) for v in range(14, 5, -1)] + [(14, 5, 4, 3, 2)]
ranks = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(),(),(3,2),(4,1)]

def hand_rank(hand):
	score = zip(*sorted(((v, values[k]) for
		k,v in Counter(x[0] for x in hand).items()), reverse=True))
	score[0] = ranks.index(score[0])
	if len(set(card[1] for card in hand)) == 1: score[0] = 5  # flush
	if score[1] in straights: score[0] = 8 if score[0] == 5 else 4  # str./str. flush
	return score

summ = 0
for hand in hands:
	if hand_rank(hand[:5]) > hand_rank(hand[5:]):
		summ += 1

print "Project Euler 54 Solution =", summ

