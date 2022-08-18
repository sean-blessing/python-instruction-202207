# a list of numbers, 0 to 10
nbrs = [0,1,2,3,4,5,6,7,8,9,10]

for i in range(len(nbrs)):
    print(f'i = {i}')

# a list of strings
bands = ['Foo Fighters', 'Bob Marley', 'The Police', 'Ariana Grande', 'Bruno Mars', 'P!nk', 'Wet Leg']
for band in bands:
    print(band)

# build a list of even #s with list comprehension - example from book
evens = [num for num in range (0,11) if num % 2 == 0]
print(evens)

# fizz buzz: /3 fizz, /5 buzz, /3 and /5 fizzbuxx, else #
fizzbuzz = ['fizzbuzz' if v%3 == 0 and v%5 == 0 else 'fizz' if v % 3 == 0 else 'buzz' if v % 5 == 0 else v for v in range(1, 51)]
print(fizzbuzz)