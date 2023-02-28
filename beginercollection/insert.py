def insert_sort(numbers):
    numbers_len = len(numbers)
    for i in range(1, numbers_len):
        temp = numbers[i]
        j = i - 1
        while j >=0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = temp
    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0,100) for i in range(8)]
    print(insert_sort(nums))