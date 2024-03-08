languages = ["Python", "Ruby", "C", "C++", "C#", "JavaScript"]

# lengths = { language for language in languages }
# lengths = { language: len(language) for language in languages }
lengths = { language: len(language) for language in languages if "t" in language }
print(lengths)

word = "supercalifragilisticexpialidocious"

# letter_count = { letter: word.count(letter) for letter in word }
letter_count = { letter: word.count(letter) for letter in word if letter > "j" }
print(letter_count)

