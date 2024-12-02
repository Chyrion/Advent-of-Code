# pylint: disable-all
# I just don't want to deal with pylint errors on AoC

def day1_1(num_list: list):
    # zip() provides a tuple for each pair in num_list (num_list[0][0], num_list[0][1]) and so on
    # These are iterated through and summed, returning the total distance
    return sum(abs(l-r) for l, r in zip(num_list[0], num_list[1]))


def day1_2(num_list: list[list, list]):
    score = 0
    for n in num_list[0]:
        score += n * num_list[1].count(n)
    return score


if __name__ == "__main__":
    file = open("./day1_input.txt", "r")
    # This is terrible, forgive me
    # I'll fix this later (trust me)
    l_list, r_list = [], []
    num_list = []
    for x in file.readlines():
        line = x.rstrip("\\n").split()
        l_list.append(int(line[0]))
        r_list.append(int(line[1]))
    l_list.sort()
    r_list.sort()
    num_list.append(l_list)
    num_list.append(r_list)

    print(day1_1(num_list))
    print(day1_2(num_list))
