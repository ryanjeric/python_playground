import itertools

my_list = [1, 2, 3, 4, 5, 6]

combinations = itertools.combinations(my_list, 3)
permutations = itertools.permutations(my_list, 3)

print([result for result in combinations if sum(result) == 10])
# print([result for result in permutations if sum(result) == 10])

word = 'sample'
my_letters = 'plmeas'

word_combinations = itertools.combinations(my_letters, 6)
word_permutations = itertools.permutations(my_letters, 6)

for p in word_permutations:
    # print(p)
    if ''.join(p) == word:
        print('Match')
        break
else:
    print('No match')
