def select_sort(numbers):
    numbers_len = len(numbers)
    for i in range(numbers_len):
        min_index = i
        for j in range(i+1, numbers_len):
            if numbers[min_index] > numbers[j]:
                numbers[min_index], numbers[j] = numbers[j], numbers[min_index]
    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0,100) for i in range(8)]
    print(select_sort(nums))