from bisect import bisect_left, bisect_right

n = input()
cards = list(map(int, input().split()))
m = input()
think = list(map(int, input().split()))

cards.sort()
for i in think:
    print(bisect_right(cards, i) - bisect_left(cards, i), end=' ')

