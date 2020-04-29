class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


def my_range(start):  # GENERATORS
    current = start
    while True:
        yield current
        current += 1


nums = my_range(1)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print()
nums2 = MyRange(1,10)
for num in nums2:
    print(num)
