#list creation with for loop

odd = []
for i in range(10):
    odd.append(i)
print(odd)


#list creation with map
odd = [1,3,5,7,9,11,13,15,17]
def odd_squared(odd):
    return odd * odd
odd_squarednum = map(odd_squared,odd)
print(list(odd_squarednum))


#list creation with List Comprehension
odd = [i for i in range(10)]
print(odd)


#list comprehension solution for odd number square
odd = [1,3,5,7,9,11,13,15,17]
odd_squared = [i*i for i in odd]
print(odd_squared)


#list comprehension using conditionals
vowels = "aeiouAEIOU"
sentence = "do I have a vowel here Please?"
search_vowel = len([i for i in sentence if i in vowels])
print(search_vowel)