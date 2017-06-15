import matplotlib.pyplot as plt
import random


def dice(n):
    """
    投掷n个骰子，和为[n, 6n]，求每种可能出现的次数
    动态分布：
    f(n, s)表示：n个骰子、和为s的出现次数
    f(n+1, s)表示：再投一个骰子、和为s的次数，
    再投的一个骰子可能出现1-6，
    故，f(n+1, s) = f(n, s-1) + f(n, s-2) + ... + f(n, s-6)
    """
    rst = [0] * (6 * n + 1)
    tmp = [0] * (6 * n + 1)
    for i in range(1, 7):
        tmp[i] = 1
    for m in range(2, n + 1):
        for s in range(m, 6 * m + 1):
            a = 0
            for i in range(1, 7):
                if s - i > 0:
                    a += tmp[s - i]
            rst[s] = a
        rst[:m] = [0] * m
        rst, tmp = tmp, rst
    print(tmp[n:])


def pull_Pallet_Truck():
    def check_truck(role: list):
        nonlocal game
        card = role.pop(0)
        if card in game:
            idx = game.index(card)
            role.append(card)
            role += game[idx:][::-1]
            game = game[:idx]
            return True
        else:
            game.append(card)
            return False

    pokers = list('123456789#JQK' * 4 + 'UU')
    random.shuffle(pokers)
    print(pokers)
    m = len(pokers) >> 1
    role1 = pokers[:m]
    role2 = pokers[m:]
    game = []
    rounds = 1
    # print(len(role1), len(role2))
    rl1, rl2 = [], []
    while len(role1) > 0 and len(role2) > 0:
        if rounds & 1:
            if check_truck(role1):
                continue
        else:
            if check_truck(role2):
                continue
        rounds += 1
        rl1.append(len(role1))
        rl2.append(len(role2))
        # print(len(role1), len(role2), len(game))
    print(rounds)
    print(rl1)
    print(rl2)
    plt.plot(rl1, label='role1')
    plt.plot(rl2, label='role2')
    plt.legend(loc='upper left')
    plt.show()


if __name__ == '__main__':
    pull_Pallet_Truck()
