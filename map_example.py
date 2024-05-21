def capitalize_and_ascii_sum(word: str):
    # """
    # This method capitalizes the word and finds out the sum of ASCII
    # all characters of a word
    # """
    return sum(ord(x)for x in word.capitalize())


animals =['cat', 'dog','cow']
animal_output = []

animal_output = list(map(capitalize_and_ascii_sum,animals))
print(animal_output)


#%%%%%%%%%%%%%%%%
def square(x):
    return x**2

numbers = [1,2,3,4,5]

square = map(lambda x: x ** 2, numbers)
print(list(square))