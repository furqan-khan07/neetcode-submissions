def add_two_numbers() -> int:
    nums = input()
    numssplit = nums.split(",")

    count = 0
    for num in numssplit:
        count += int(num)

    return count



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
