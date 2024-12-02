# pylint: disable-all

# This is ugly
def day2_1(reports: list[list[int]]):
    safe = 0
    for r in reports:
        x = sorted(r)
        y = list(reversed(x))
        if r == x or r == y:
            a = 0
            for n in range(1, len(r)):
                if abs(r[n]-r[n-1]) in range(1, 4):
                    a += 1
            if a == len(r)-1:
                safe += 1

    return safe


if __name__ == "__main__":

    file = open("./day2_input.txt", "r")
    reports = []
    for x in file.readlines():
        reports.append(list(map(int, x.split())))
    print(day2_1(reports))
