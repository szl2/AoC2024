import re

def extract_and_sum_mul(sequence):
    pattern = re.compile(r'mul\((\d+),(\d+)\)')
    sequence = pattern.findall(sequence)
    total_sum = sum(int(x) * int(y) for x, y in sequence)
    
    return total_sum

def task2(sequence):
    tokens = re.split(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', sequence)

    enable_pattern = re.compile(r'do\(\)')
    disable_pattern = re.compile(r"don't\(\)")
    mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')

    total_sum = 0
    enabled = True  

    for token in tokens:
        if not token or token.isspace():
            continue

        if enable_pattern.fullmatch(token):
            enabled = True
        elif disable_pattern.fullmatch(token):
            enabled = False
        else:
            match = mul_pattern.fullmatch(token)
            if match and enabled:
                x, y = [int(num) for num in  match.groups()]
                total_sum += x * y
    
    return total_sum


if __name__=="__main__":
    with open('input.txt', 'r') as file:
        input_sequence = file.read()
    
    result = extract_and_sum_mul(input_sequence)
    print("Task 1: ", result)
    result = task2(input_sequence)
    print("Task 2: ", result)
