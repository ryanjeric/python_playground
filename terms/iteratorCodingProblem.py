# PROBLEM : https://www.youtube.com/watch?v=C3Z9lJXI6Qw
class Sentence:
    def __init__(self, p):
        self.value = p.split()
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        # EAFP
        try:
            current = self.current
            self.current += 1
            return self.value[current]
        except IndexError:
            raise StopIteration


# generator
def sentencetolist(sentence):
    for word in sentence.split():
        yield word


my_sentence = sentencetolist('This is a test')

#for word in my_sentence:
#    print(word)

print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))