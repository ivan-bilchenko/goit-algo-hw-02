from collections import deque

def is_palindrome(input_string):
    cleaned_string = ''.join(input_string.split()).lower()
    
    char_deque = deque(cleaned_string)
    
    while len(char_deque) > 1:
        front_char = char_deque.popleft()
        back_char = char_deque.pop()
        if front_char != back_char:
            return False
    return True

def main():
    test_strings = [
        "A man a plan a canal Panama",
        "Racecar",
        "Python",
    ]

    for s in test_strings:
        result = is_palindrome(s)
        print(f"'{s}' -> {result}")

if __name__ == "__main__":
    main()