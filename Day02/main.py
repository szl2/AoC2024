import sys


def Task1isSafe(val_list):
    diff_list = [ val_list[i+1] - val_list[i] for i in range(len(val_list) - 1)]
    if diff_list[0] < 0:
        diff_list = [-1*val for val in diff_list]

    for val in diff_list:
        if not(1 <= val and val <= 3):
            return 0
        
    return 1

def Task2isSafe(val_list):

    if Task1isSafe(val_list):
        return 1
    else:
        for i in range(len(val_list)):
            new_list = val_list[:i] + val_list[i+1:]
            if Task1isSafe(new_list):
                return 1
    
    return 0




if __name__=="__main__":
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    
    Task1Res = 0
    Task2Res = 0
    for line in lines:
        val_list = [int(val) for val in line.split()]
        
        Task1Res += Task1isSafe(val_list)
        Task2Res += Task2isSafe(val_list)
    
    print(Task1Res)
    print(Task2Res)

        
        