def two_sum_2(numbers, target):
    start = 0
    end = len(numbers) - 1

    for i in range(len(numbers)):

        numSum = numbers[start] + numbers[end]

        if target > numSum:
            end -= 1
        elif target < numSum:
            start += 1

        else:
            return [start + 1, end + 1]
