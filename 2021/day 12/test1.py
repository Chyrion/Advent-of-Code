from collections import defaultdict
from functools import lru_cache

edges = defaultdict(list)
for line in open("input.txt").readlines():
    src, dst = map(lambda s: s.strip(), line.split("-"))
    edges[src].append(dst)
    edges[dst].append(src)

@lru_cache(maxsize=None)
def dfs(current, visited, twice=True):
    if current.islower():
        visited |= {current}
    num_paths = 0
    for dst in edges[current]:
        if dst == "end":
            num_paths += 1
        elif dst != "start":
            if dst not in visited:
                num_paths += dfs(dst, visited, twice)
            elif not twice:
                num_paths += dfs(dst, visited, True)
    return num_paths


print("Part 1:", dfs("start", frozenset()))
print("Part 2:", dfs("start", frozenset(), False))