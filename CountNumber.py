def findMax(numbers):
    GiaTriLonNhat = numbers[0]
    for number in numbers:
        if number > GiaTriLonNhat:
            GiaTriLonNhat = number
    return GiaTriLonNhat
