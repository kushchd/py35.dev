import random
import string

def computer_guess(name):
    letters = list(name.lower())
    guessed = ["_"] * len(letters)
    alphabet = list(string.ascii_lowercase)
    attempts = 0

    while "_" in guessed and alphabet:
        # компьютер выбирает случайную букву
        letter = random.choice(alphabet)
        alphabet.remove(letter)
        attempts += 1

        if letter in letters:
            for i, ch in enumerate(letters):
                if ch == letter:
                    guessed[i] = name[i]  # сохраняем оригинальную букву
            print(f"Компьютер угадал букву '{letter}' →", " ".join(guessed))
        else:
            print(f"Буквы '{letter}' нет.")

    print("\nИмя угадано за", attempts, "попыток:", name)


# пример запуска
secret_name = "Метрондир"
computer_guess(secret_name)
