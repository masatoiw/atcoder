# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def bubble_sort(numbers):
    numbers_len = len(numbers)
    for i in range(numbers_len):

        for j in range(numbers_len - 1 - i):
            if numbers[j] > numbers[j + 1]:
                tmp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = tmp
    return numbers

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [2,3,5,6,1,9,4]
    print(bubble_sort(nums))


