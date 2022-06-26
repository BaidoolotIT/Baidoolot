def binare(search):
    n = len(search)
    for num in range(n - 1):
        for j in range(0, n - num - 1):
            if search[j] > search[j + 1]:
                search[j], search[j + 1] = search[j + 1], search[j]
list = [2,4,1,5,3,9,6,8,7,10,0]
binare(list)

print(f"binare_search: {list}")



def buble(sort):
    for i in range(0, len(sort) - 1):
        smallest = i
        for j in range(i + 1, len(sort)):
            if sort[j] < sort[smallest]:
                smallest = j
        sort[i], sort[smallest] = sort[smallest], sort[i]
list2 = [2,4,1,5,3,9,6,8,7,10,0]
buble(list2)

print(f"buble_sort: {list2}")
