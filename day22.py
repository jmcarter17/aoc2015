from utils import timer


def sim(boss, actions, part):
    boss_hp, boss_dmg = boss["HP"], boss["Damage"]
    hp, mana, armor = 50, 500, 0
    turn, turn_c = 0, 0
    mana_spent = 0
    poison_left, shield_left, recharge_left = 0, 0, 0
    my_turn = True
    spell_cost = {"M": 53, "D": 73, "S": 113, "P": 173, "R": 229}

    while True:
        if len(actions) <= turn_c:
            return
        if poison_left:
            poison_left -= 1
            boss_hp -= 3
        if shield_left:
            shield_left -= 1
            armor = 7
        else:
            armor = 0
        if recharge_left:
            recharge_left -= 1
            mana += 101
        if my_turn:
            if part == 2:
                hp -= 1
                if hp <= 0:
                    return
            action = actions[turn_c]
            mana -= spell_cost[action]
            mana_spent += spell_cost[action]
            if action == "M":
                boss_hp -= 4
            elif action == "D":
                boss_hp -= 2
                hp += 2
            elif action == "S":
                if shield_left:
                    return
                shield_left = 6
            elif action == "P":
                if poison_left:
                    return
                poison_left = 6
            elif action == "R":
                if recharge_left:
                    return
                recharge_left = 5
            if mana < 0:
                return
        if boss_hp <= 0:
            return mana_spent
        if not my_turn:
            hp -= max(boss_dmg - armor, 1)
            if hp <= 0:
                return
        if my_turn:
            turn_c += 1
        my_turn = not my_turn
        turn += 1


def iterate_actions(actions, pos):
    actions[pos] = "DSPRM"["MDSPR".index(actions[pos])]
    if actions[pos] == "M":
        if pos + 1 <= len(actions):
            iterate_actions(actions, pos + 1)


def solve(boss, part):
    actions = ["M"] * 10
    min_spent = 10000

    for i in range(100000):
        iterate_actions(actions, 0)
        result = sim(boss, actions, part)
        if result:
            min_spent = min(result, min_spent)
    return min_spent


@timer
def main():
    boss = {
        "HP": 58,
        "Damage": 9
    }

    print(solve(boss, 1))
    print(solve(boss, 2))


if __name__ == "__main__":
    main()
