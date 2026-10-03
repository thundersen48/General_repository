import re

product_review = '''Это прекрасное молоко, но товарная линейка, похоже, ограничена спектром имеющихся цветов. Я смог найти только белый цвет.'''

sentence_pattern = re.compile(r'(.*?\.)(\s|$)', re.DOTALL)
matches = sentence_pattern.findall(product_review)
sentences = [match[0] for match in matches]

word_pattern = re.compile(r"([\w\-']+)([\s,.])?")
for sentence in sentences:
    matches = word_pattern.findall(sentence)
    words = [match[0] for match in matches]
    print(words)