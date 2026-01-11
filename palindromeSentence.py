def is_palindrome(sentence):
    cleaned = [char.lower() for char in sentence if char.isalnum()]

    cleaned_str = ''.join(cleaned)
    return cleaned_str == cleaned_str[:: -1]

text = "A man , a plan , a canal : panama"
print(f"is the palindrome : ", is_palindrome(text))