import sys


def task1(list1, list2):
    list1.sort()
    list2.sort()

    res = sum([abs(n1 - n2) for n1,n2 in zip(list1, list2)])

    print(res)

def task2(list1, list2):
    list2_freq = {}
    
    for n2 in list2:
        list2_freq[n2] = 1 + list2_freq.get(n2, 0)
    

    # print([list2_freq.get(n1,0) for n1 in list1])

    res = sum([n1 * list2_freq.get(n1,0) for n1 in list1])

    print(res)


if __name__=="__main__":
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    
    list1, list2 = [],[]
    for line in lines:
        [val1, val2] = line.split()
        list1.append(int(val1))
        list2.append(int(val2))
    
    task1(list1, list2)
    task2(list1, list2)

    
    