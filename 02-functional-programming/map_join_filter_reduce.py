from functools import reduce


def add_one(x):
    return x + 1


mylist = [1, 2, 3, 4, 5]
mynewlist = map(add_one, mylist)

print(mylist)
print(list(mynewlist))


# Calling map with many lists
def multiply(a, b, c):
    return a * b * c

result = map(multiply, [1, 2, 3], [4, 5, 6], [7, 8, 9])
print(list(result))

def num_of_chars(s):
    return len(s)


words = ["train", "bus", "car", "bike"]
len_words = map(num_of_chars, words)
print(list(len_words))


all_words = " - ".join(words)
print(all_words)


def more_than_three(s):
    return len(s) > 3

words_more_than_3_letters = filter(more_than_three, words)
print(list(words_more_than_3_letters))


def add_numbers(a, b):
    return a + b

print(reduce(add_numbers, mylist))


def concat(s1, s2):
    return s1 + "-" + s2
print(reduce(concat, words))

