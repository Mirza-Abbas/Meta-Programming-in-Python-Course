def isPalindrome(str):
    startingIndex = 0
    endingIndex = len(str) - 1

    for x in str:
        if str[startingIndex] != str[endingIndex]:
            return False
    
    return True

print(isPalindrome('racecar'))

print(isPalindrome('racecars'))