def vigenere(text, key, mode='encrypt'):
    alphabet_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet_upper = alphabet_lower.upper()
    n = len(alphabet_lower)

    result = []
    key_index = 0

    for char in text:
        if char in alphabet_lower:
            text_pos = alphabet_lower.index(char)
            key_char = key[key_index % len(key)].lower()
            key_pos = alphabet_lower.index(key_char)

            if mode == 'encrypt':
                new_char = alphabet_lower[(text_pos + key_pos) % n]
            else:
                new_char = alphabet_lower[(text_pos - key_pos) % n]

            result.append(new_char)
            key_index += 1

        elif char in alphabet_upper:
            text_pos = alphabet_upper.index(char)
            key_char = key[key_index % len(key)].lower()
            key_pos = alphabet_lower.index(key_char)

            if mode == 'encrypt':
                new_char = alphabet_upper[(text_pos + key_pos) % n]
            else:
                new_char = alphabet_upper[(text_pos - key_pos) % n]

            result.append(new_char)
            key_index += 1

        else:
            result.append(char)

    return ''.join(result)

print("Выберите режим:")
print("1 — Шифрование")
print("2 — Дешифрование")

choice = input("Введите 1 или 2: ").strip()

if choice == '1':
    mode = 'encrypt'
elif choice == '2':
    mode = 'decrypt'
else:
    print("Неверный выбор.")
    exit()

text = input("Введите текст: ")
key = input("Введите ключ: ")

result = vigenere(text, key, mode)

print("\nРезультат:")
print(result)