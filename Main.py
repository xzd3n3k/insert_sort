def insert_sort(numbers):
    for x in range(1, len(numbers)):
        tmp = numbers[x]
        i = x - 1

        while i >= 0 and tmp < numbers[i]:
            numbers[i+1] = numbers[i]
            i -= 1

        numbers[i+1] = tmp

    return numbers
