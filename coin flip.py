from random import choice

def flip():
    choices_ = ['Heads', 'Tails']
    chosen = choice(choices_)
    return chosen

try:
    n = int(input("How many times do you want to flip the coin: "))
    ans = []
    for i in range(n):
        ans.append(flip())
    print(ans)
except:
    print("Invalid arguments given. please check again.")
