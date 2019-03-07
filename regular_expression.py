import re

with open('example.ini') as f:
    data = f.read()

# To match first and last name
first = re.match(r'Sam', data)   # Only checks the start of string
last = re.search(r'Karis', data)

print(first, last)

"""
Escape Characters and they match
\w - Any unicode word character
\W - Anything that isn't Unicode Character
\s - Any whitespace
\S - Anything that isn't whitespace
\d - Any number from 0-9
\D - Anything that isn't a number
\b - matches word boundaries. What's a word boundary? It's the edges of word, defined by white space or the edges of the string.
\B - matches anything that isn't the edges of a word.
"""

number = re.search(r'\(\d\d\d\)\s\d\d\d\s\d\d\d\s\d\d\d', data)
first_name = re.match(r'\w\w\w\s', data)
last_name = re.search(r'\s\w\w\w\w\w', data)
print(number, first_name, last_name)

"""
Counts
\w{3} - matches any three word characters in a row.
\w{,3} - matches 0, 1, 2, or 3 word characters in a row.
\w{3,} - matches 3 or more word characters in a row. There's no upper limit.
\w{3, 5} - matches 3, 4, or 5 word characters in a row.
\w? - matches 0 or 1 word characters.
\w* - matches 0 or more word characters. Since there is no upper limit, this is, effectively, infinite word characters.
\w+ - matches 1 or more word characters. Like *, it has no upper limit, but it has to occur at least once.
.findall(pattern, text, flags) - Finds all non-overlapping occurrences of the pattern in the text.
"""
# number with specific counts
number_count = re.search(r'\(\d{3}\)\s\d{3}\s\d{3}\s\d{3}', data)
first_name = re.match(r'\w{3}', data)
last_name = re.search(r'\s\w{5}', data)
# number without specific digits
number = re.search(r'\(\d+\)\s\d+\s\d+\s\d+', data)
# make () optional and search all numbers
all_numbers = re.findall(r'\(?\d+\)?\s\d+\s\d+\s\d+', data)
print(number_count, first_name, last_name, number, all_numbers)


"""
Sets
[abc] - this is a set of the characters 'a', 'b', and 'c'. It'll match any of those characters, in any order, but only once each.
[a-z], [A-Z], or [a-zA-Z] - ranges that'll match any/all letters in the English alphabet in lowercase, uppercase, or both upper and lowercases.
[0-9] - range that'll match any number from 0 to 9. You can change the ends to restrict the set.
[^abc] - a set that will not match, and, in fact, exclude, the letters 'a', 'b', and 'c'.
re.IGNORECASE or re.I - flag to make a search case-insensitive. re.match('A', 'apple', re.I) would find the 'a' in 'apple'.
re.VERBOSE or re.X - flag that allows regular expressions to span multiple lines and contain (ignored) whitespace and comments.
"""

emails = re.findall(r'[-\w\d+]+@[-\w\d]+\.[-\w\d]+', data)
print(emails)

"""
Groups
([abc]) - creates a group that contains a set for the letters 'a', 'b', and 'c'. This could be later accessed from the Match object as .group(1)
(?P<name>[abc]) - creates a named group that contains a set for the letters 'a', 'b', and 'c'. This could later be accessed from the Match object as .group('name').
.groups() - method to show all of the groups on a Match object.
re.MULTILINE or re.M - flag to make a pattern regard lines in your text as the beginning or end of a string.
^ - specifies, in a pattern, the beginning of the string.
$ - specifies, in a pattern, the end of the string.
"""

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r'''
	(?P<email>[-\w+]+@[-\w.+]+), \s
    (?P<phone>\d{3}-\d{3}-\d{4})
''', string, re.X | re.M)
print(contacts.groupdict())

twitters = re.search(r'''
    (?P<twitters>@[-\w]+)$
''', string, re.X | re.M)
print(twitters)

"""
Compile
re.compile(pattern, flags) - method to pre-compile and save a regular expression pattern, and any associated flags, for later use.
.groupdict() - method to generate a dictionary from a Match object's groups. The keys will be the group names. The values will be the results of the patterns in the group.
re.finditer() - method to generate an iterable from the non-overlapping matches of a regular expression. Very handy for for loops.
.group() - method to access the content of a group. 0 or none is the entire match. 1 through how ever many groups you have will get that group. Or use a group's name to get it if you're using named groups.
"""
contacts = re.compile(r'''
	(?P<email>[-\w+]+@[-\w.+]+), \s
    (?P<phone>\d{3}-\d{3}-\d{4})
''', re.X | re.M)

# How to use
print(re.search(contacts, string).groupdict())
print(contacts.search(string).groupdict())

for contact in contacts.finditer(string):
    print(contact.group('email'))
    print(contact.group('phone'))



string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r"""
	^(?P<last_name>[\w\s]+), \s
    (?P<first_name>[\w\s]+): \s
    (?P<score>\d+)$
""", string, re.X|re.M)

print(players.groupdict())
