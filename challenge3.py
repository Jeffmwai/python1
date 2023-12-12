def solve(word):
    consonant_values = [sum(ord(char) - ord('a') + 1 for char in substring) for substring in word if substring not in 'aeiou']
    return max(consonant_values)
