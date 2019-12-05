# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def build_binary(N):
    # return a list containing the binary form of the number
    ret = []
    while (N > 1):
        ret.append(N%2)
        N = int(N/2)
    ret.append(N)
    ret.reverse()
    return ret

def solution(N):
    # write your code in Python 3.6
    # for i in range(N):
    #     print(i, build_binary(i))
    bin = build_binary(N)
    long_bin_gap = 0

    gap = False
    count_gap = 0
    for i in bin:
        # for each element in the list, check if it's 1 to control gaps
        if i:
            if gap:
                long_bin_gap = count_gap if count_gap > long_bin_gap else long_bin_gap
                count_gap = 0
            else:
                gap = True
        else:
            count_gap += 1
    return long_bin_gap

if __name__ == '__main__':
    test = [
        (1041,5),
        (32,0),
        (9, 2),
        (529, 4),
        (20, 1),
        (15, 0),
        (328, 2),
        (1162, 3),
        (51712, 2),
        (6291457, 20),
        (805306373, 25),
        (1610612737, 28)
    ]

    for i in test:
        res = solution(i[0])
        assert res==i[1], f'Error for {i[0]} - Expected {i[1]} got {res}'
        print(f'OK for {i[0]} - Expected {i[1]} got {res}')
