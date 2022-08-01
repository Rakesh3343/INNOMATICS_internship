def average(array):
    a=sum(set(array))/len(set(array))
    return a

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)