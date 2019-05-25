# We define an anagram to be a word whose characters can be rearranged to create
# another word. Given two strings, we want to know the minimum number of
# characters in either string that we must modify to make the two strings
# anagrams. If it's not possible to make the two strings anagrams, we consider
# this number to be -1.
#
# For example:
# - tea and ate are anagrams, so we would need to modify 0 characters.

# t, e, a, t => t: 2, ...
# a, t, e, s => t: 1, s: 1

# - tea and toe are not anagrams, but we can modify 1 character in either string (
# o -> a or a -> o) to make them anagrams.
# - act and acts are not anagrams and cannot be converted to anagrams because
# they contain different numbers of characters.
#
# Requirements:
# Write a function to return minimum number of characters in two strings that
# need to be modified to make the two strings anagrams. If it's not possible,
# return -1.

def anagrams(s1, s2):
    if len(s1) != len(s2):
        return -1
    m1 = {}
    m2 = {}

    for i in range(len(s1)):
        if s1[i] not in m1:
            m1[s1[i]] = 1
        else:
            m1[s1[i]] += 1
        if s2[i] not in m2:
            m2[s2[i]] = 1
        else:
            m2[s2[i]] += 1

    print(m1)
    print(m2)

    min_diff = 0
    for k, v in m1.items():
        if k not in m2:
            min_diff += v
    print(min_diff)
    return min_diff


result = anagrams("ates", "sate")
assert(result == 0)
result = anagrams("ttes", "tttt")
assert(result == 2)
result = anagrams("oat", "oats")
assert(result == -1)
result = anagrams("xxxx", "yyyy")
assert(result == 4)
result = anagrams("", "")
assert(result == 0)



