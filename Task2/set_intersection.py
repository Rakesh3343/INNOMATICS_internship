n_eng = int(input())
roll_eng = set(map(int, input().split()))
n_french = int(input())
roll_french = set(map(int, input().split()))

print(len(roll_eng.intersection(roll_french)))