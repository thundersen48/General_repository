# сложность времени O(n)
list = [1,2,3,4]
def print_num(arr: list):
    for num in arr:
        print(num)


# сложность времени O(n^2)
def print_pairs(arr: list):
    for num1 in arr:
        for num2 in arr:
            print(num1, num2)


def print_idx(arr: list, i: int):
    print(arr[i])

#print(print_idx(arr=(1,2,3,4),i=1))
print(print_pairs(arr=(1,2)))
#print(print_num(arr=(1,2,3,4)))