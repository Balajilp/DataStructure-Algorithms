def BinarySearch(list1, key):
    low = 0
    high = len(list1)-1
    Found = False
    while low <= high and not Found:
        mid = (low+high)//2
        if key == list1[mid]:
            Found = True
        elif key > list1[mid]:
            low = mid+1
        else:
            high = mid-1
    if Found:
        print('Key is Found')
    else:
        print('Key is not found')

list1 = list(map(int, input().split()))
list1.sort()
key = int(input())
BinarySearch(list1, key)



