'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #check if word is less than 2 characters, since we need at least 2 for "th"
    if len(word) < 2:
        return 0
    #check if "th" is in word up to the the 2nd index(non-inclusive)
    #if it is, return 1 + plus recursive call, which will continue returning +1 untul the string is no longer found
    if "th" in word[:2]:
        return 1 + count_th(word[2:])
    #else, return recursive call of function again, skipping over the first letter
    else:
        return count_th(word[1:])
