if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    s = set(arr)
    for i in s:
        count = 0
        for j in s:
            if i < j:
                count += 1
        print(count)
        if count == 1:
            print(i)
            break