def find_sum(n):
    res = 0
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res

print(find_sum(5))
print(find_sum(10))

def find_sum2(n):
    return sum (i for i in range(n + 1) if i % 3 ==0 or i % 5 == 0)
print(find_sum2(5))
print(find_sum2(10))



def get_names(names):
    return [i for i in names if len(i) ==4]
names =['Rayan','Kieran','Mark','John','David','Paul']
print(get_names(names))
