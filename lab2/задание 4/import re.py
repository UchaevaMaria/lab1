import re

# Чтение текста из файла
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Регулярные выражения
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone_pattern = r'\b\+7-\d{3}-\d{3}-\d{2}-\d{2}\b'
capital_words_pattern = r'\b[A-ZА-ЯЁ][a-zа-яё]*\b'  # Учитываем русские буквы и букву Ё
# Поиск совпадений
emails = re.findall(email_pattern, text, flags=re.IGNORECASE)
phone_pattern = r'\+7-\d{3}-\d{3}-\d{2}-\d{2}'
phones = re.findall(phone_pattern, text)

capital_words = re.findall(capital_words_pattern, text)
with open('emails.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(emails))

with open('phones.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(phones))

with open('capital_words.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(capital_words))

print("Результаты сохранены в файлы: emails.txt, phones.txt, capital_words.txt")