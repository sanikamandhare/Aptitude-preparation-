#Write code to check if two strings match where one string contains wildcard 

def match_with_wildcard(pattern, text):
    pattern_index = 0
    text_index = 0
    wildcard = False  # Indicates if we are in a wildcard state

    while text_index < len(text):
        if pattern[pattern_index] == '*':
            wildcard = True
            pattern_index += 1
            if pattern_index == len(pattern):  # If '*' is the last character in the pattern
                return True
            continue

        if pattern[pattern_index] == '?' or pattern[pattern_index] == text[text_index]:
            pattern_index += 1
            text_index += 1
        elif not wildcard:  # If not in wildcard state and characters don't match
            return False
        else:
            text_index += 1

    return pattern_index == len(pattern) and text_index == len(text)

# Example usage:
pattern = "h*llo"
text = "hello"
print(match_with_wildcard(pattern, text))  # Output: True
