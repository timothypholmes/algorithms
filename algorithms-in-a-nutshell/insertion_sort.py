


def sort_val(a: list) -> list:
    print('input array: {}'.format(a))
    for i in range(0, len(a)):
        output = insert(a, i, a[i])
    return output

def insert(a: list, pos: int, val: int) -> list:
    i = pos - 1
    while i >= 0 and a[i] > val:
        a[i + 1] = a[i]
        i = i - 1
    a[i + 1] = val
    return a

if __name__ == "__main__":
    output = sort_val([5, 9, 1, 4, 8, 7])
    print('output array: {}'.format(output))
