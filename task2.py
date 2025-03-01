print('narayana')
def narayana(arr, length):
    result = []
    from itertools import combinations
    for combo in combinations(arr, length):
        current = list(combo)
        print(current)
        result.append(current.copy())
        while True:
            index_j = -1
            for i in range(length - 2, -1, -1):
                if current[i] < current[i + 1]:
                    index_i = i
                    break
            else:
                break
            for j in range(length - 1, -1, -1):
                if current[j] > current[index_i]:
                    index_j = j
                    break
            current[index_i], current[index_j] = current[index_j], current[index_i]
            current[index_i + 1:] = current[:index_i:-1]
            print(current)
            result.append(current.copy())
    return result
list1 = [1, 2, 3]
list1.sort()
permutations = narayana(list1, 2)
print(len(permutations))
print('itertools')
import itertools
a = 0
for p in itertools.permutations(list1, 2):
    a += 1
    print(p)
print(a)
