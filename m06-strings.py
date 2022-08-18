print('#2')
#2. We were given these lyrics to split for a karaoke machine. 
#   Split the lyrics by line using split().
lyrics = """
Katie Casey was baseball mad,
Had the fever and had it bad.
Just to root for the home town crew,
Ev'ry sou
Katie blew.
On a Saturday her young beau
Called to see if she'd like to go
To see a show, but Miss Kate said "No,
I'll tell you what you can do:"
"""
lyrics_split = lyrics.split('\n')
print(lyrics_split)

print('\n#3')
#3. We were given these lyrics to split for a karaoke machine.  
#   Split the lyrics by line using something other than split().
lyrics = """
Katie Casey was baseball mad,
Had the fever and had it bad.
Just to root for the home town crew,
Ev'ry sou
Katie blew.
On a Saturday her young beau
Called to see if she'd like to go
To see a show, but Miss Kate said "No,
I'll tell you what you can do:"
"""
lyrics_split = lyrics.splitlines()
print(lyrics_split)

print('\n#4')
#5. We want all folders in this path without additional spaces. 
#   How would you get that?
my_path = '   /c/Users/instructor/Downloads/Submit Relating the Nonrelational Assessment Download May 10, 2021 917 AM          '
my_folders = my_path.strip().split('/')
print(my_folders)

print('\n#5')
composers="Beethoven,Ludwig von;Liszt,Franz;Mozart,Wolfgang;Copland,Aaron"
composers_split = composers.split(';')
print(f'composers_split = {composers_split}')
third_composer = composers_split[2]
comma_position = third_composer.find(',')
#last_name = third_composer[0:comma_position]
last_name = third_composer[:comma_position]
first_name = third_composer[comma_position+1:len(third_composer)]
first_name = third_composer[comma_position+1:]
third_composer_name = first_name + " " + last_name
print(third_composer_name)