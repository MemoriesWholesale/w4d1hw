#Make a function that takes a string and returns the most common letter lowercased 
# in the string regardless of capitalization.
# ignore spaces
# assume only one letter will have the most occurances
#ex) "John Loves to Play Baseball and Joanie Loves to Play Basketball, but Jenny Likes To Dance"
#output: l

"""
initialize an empty dictionary
for each letter in the string, set a key in the dictionary, starting at one and incrementing every time you 
see another instance of that letter
then return the key from the dictionary that has the hightest value
"""

def solution(s):
    counts = {}
    for i in s.lower():
        if i.isalpha():
            counts[i] = counts.get(i,0) + 1
    countsmax = max([counts[k] for k in counts])
    return [key for key in counts if counts[key] == countsmax][0]