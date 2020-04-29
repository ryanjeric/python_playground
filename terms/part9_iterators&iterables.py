# Iterable - can be loop over
# Iterator is an object, which is used to iterate over an iterable object using __next__() method
# Every iterator is also an iterable, but not every iterable is an iterator

# https://www.youtube.com/watch?v=jTYiNjvnHZY
# https://www.geeksforgeeks.org/python-difference-iterable-iterator/

nums = [1, 2, 3]
# for num in nums:
#    print(num)

i_nums = iter(nums)
print(i_nums)
# print(dir(i_nums))

# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums)) # StopIteration - no more values

while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break

# print(dir(nums))
# print(next(nums)) # TypeError: 'list' object is not an iterator
