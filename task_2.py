from collections import deque


def is_palindrome(text) -> bool:

    chars = deque(char for char in text.casefold() if not char.isspace())

    while len(chars) > 1:
        if chars.popleft() != chars.pop():
            return False
    return True


def main():
    text = input("Введіть рядок: ")

    print(f"Рядок '{text}' {'є' if is_palindrome(text) else 'не є'} паліндромом.")


if __name__ == "__main__":
    main()
