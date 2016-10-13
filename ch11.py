# Create a dictionary named holidays that pairs the name of
# the holiday with the date it will occur this year, include at least four
# key-value pairs # example: holiday = {'Independence Day':  'July 4'}
holiday = {'Halloween': 'October 31', 'Thanksgiving': 'November 24', 'Christmas': 'December 25', 'New Years Day': 'January 1'}

# print holiday -  does the order match what you put it in?
# The order is changed from the original state which I entered it in.
print(holiday)
print('\n')

# run the len function on holiday - how does it calculate the results?
# The len function calculates the results by key-value pair returning 4.
# ** print(len(holiday))
print(len(holiday))
print('\n')

# Write the code to use the "in" function to find one of the keys in your dictionary. Make sure to surround the
# code with a print statement so that the result prints on screen
print('Halloween' in holiday)
print('\n')

# now write the code to look for a key that is not in the dictionary. Make sure to surround the code
# with a print statement so the result prints on screen
print('Labor Day' in holiday)
print('\n')

# now write the code to find a value in your dictionary, use the print statement to show the results
val = holiday.values()
print('November 24' in val)
print('\n')

# print all of the values in the dictionary
print(val)
print('\n')

# 11.2 Looping and Dictionaries
# Write the histogram code and test it by passing in a word that has at least two of one letter
# Print the result of running the histogram code


def histogram(s):
    h = dict()
    for c in s:
        if c not in h:
            h[c] = 1
        else:
            h[c] += 1
    return h

d = histogram('these')
print(d)
print('\n')
# Exercise 11.2 Rewrite the histogram code using the get method, test with the same word, name the function histogram2
# hint assign the result of d.get(c,0) to a value then add one to the value of d[c]


def histogram2(s):
    h = dict()
    for b in s:
        h.get(b, 0)
        h[b] = 1
    else:
        h[b] += 1
        return h

n = histogram2('these')
print(n)
print('\n')
# Looping and Dictionaries
# use a for statement to print your holiday dictionary
# What prints? The keys or the values?
# The keys print when using the for statement.

for r in holiday:
    print(r)

print ("\n\n\n")  # leave this code so that there are blank lines before the next exercise
# now write code that prints all of the keys and all of their values in the holiday dictionary
# if you use the print statement then values separated by commas they appear on the same line


def print_hol(q):
    for w in q:
        print w, q[w]

x = holiday
print_hol(x)

print ("\n\n\n")  # leave this code so that there are blank lines before the next exercise

# Reverse Lookup
# Type the code for the Reverse Lookup from 11.3 below


def reverse_lookup(u, v):
    for k in u:
        if u[k] == v:
            return k
        raise ValueError

# Test the code by calling it with the holiday dictionary and one of your values (print the result)

print(reverse_lookup(holiday, 'January 1'))

print ("\n")
# Call the code a second time with a value that doesn't exist, run the program

# print(reverse_lookup(holiday, 'February 8'))

# Copy and paste the error code here, add # as needed to make the error a comment

# Traceback (most recent call last):
# File "/Users/ryanhanks/Documents/PRG_105/ch11/ch11.py", line 107, in <module>
# print(reverse_lookup(holiday, 'February 8'))
# File "/Users/ryanhanks/Documents/PRG_105/ch11/ch11.py", line 99, in reverse_lookup
# raise ValueError
# ValueError

# leave the line of code that caused the error, but put a # in front of it to make it a comment


# 11.4 Dictionaries and lists
# Type in the code to invert a dictionary


def invert_dict(p):
    inverse = dict()
    for key in p:
        valu = p[key]
        if valu not in inverse:
            inverse[valu] = [key]
        else:
            inverse[valu].append(key)
    return inverse

# Call the invert_dict function with the holiday dictionary
os = invert_dict(holiday)

# print the results

print(os)

print ("\n\n")


# Exercise 11.5 Exercise 11.5. Read the documentation of the dictionary method setdefault and use it to write a
# more concise version of invert_dict. Solution: http://thinkpython.com/code/invert_dict. py .
# define
def invert_dict(z):
    # create empty dict
    inverse = {}
    # call for key/val in named dict
    for key, vale in z.items():
        # invert to val then key
        inverse.setdefault(vale, []).append(key)
    # return the inverse
    return inverse

fs = invert_dict(holiday)

print(fs)
