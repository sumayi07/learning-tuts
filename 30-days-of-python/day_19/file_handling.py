# Day 19

# need to download all test files for the code to work

# import json
# import re
# import csv
# from stop_words import stop_words

# def line_word_count (file_name):

#     with open (file_name) as f:

#         lines = f.read().splitlines()
#         word_count = 0

#         for line in lines:

#             words = line.split()
#             word_count += len(words)

            
#         print(f"Line count: {len(lines)}")
#         print(f"Word count: {word_count}")

# line_word_count("obama_speech.txt")
# line_word_count("michelle_obama_speech.txt")
# line_word_count("donald_speech.txt")
# line_word_count("melina_trump_speech.txt")

# def most_spoken_languages (file_name, num):

#     with open (file_name) as f:

#         countries_dct = json.loads(f.read())
#         languages = {}

#         for c in countries_dct:

#             for lang in c["languages"]:

#                 if lang in languages:
#                     languages[lang] += 1
#                 else:
#                     languages[lang] = 1

#         return sorted(languages.items(), key = lambda x: x[1], reverse = True)[:num]

# print(most_spoken_languages("countries_data.json", 10))

# def most_populated_countries (file_name, num):

#     with open (file_name) as f:

#         countries_dct = json.loads(f.read())
#         countries = []

#         for c in countries_dct:

#             countries.append({"country": c["name"], "population": c["population"]})

#         return sorted(countries, key = lambda x: x["population"], reverse = True)[:num]

# print(most_populated_countries("countries_data.json", 3))

# def extract_emails (file_name):

#     with open (file_name) as f:

#         pattern = r"^From .*"
#         lines = re.findall(pattern, f.read(), re.M)

#         emails = []

#         for line in lines:
#             emails.append(line.split()[1])

#         return emails

# print(extract_emails("email_exchanges_big.txt"))

# def find_most_common_words (file_name, num):

#     with open (file_name) as f:

#         words = {}

#         for word in f.read().split():

#             if word in words:
#                 words[word] += 1
#             else:
#                 words[word] = 1

#     return sorted(words.items(), key = lambda x: x[1], reverse = True)[:num]

# print(find_most_common_words("obama_speech.txt", 10))
# print(find_most_common_words("michelle_obama_speech.txt", 10))
# print(find_most_common_words("donald_speech.txt", 10))
# print(find_most_common_words("melina_trump_speech.txt", 10))
# print(find_most_common_words("romeo_and_juliet.txt", 10))

# def clean_text (txt):

#     return re.findall(r"[a-zA-Z]+", txt)

# def remove_stop_words (words):

#     return [word.lower() for word in words if word.lower() not in stop_words]

# def check_text_similarity (txt_one, txt_two):

#     all_words = set(txt_one + txt_two)
#     shared_words = set(txt_one).intersection(set(txt_two))

#     return len(shared_words)/len(all_words)


# michelle_speech = None
# melina_speech = None

# with open ("michelle_obama_speech.txt") as f:
#     michelle_speech = f.read()

# with open ("melina_trump_speech.txt") as f:
#     melina_speech = f.read()

# michelle_speech = remove_stop_words(clean_text(michelle_speech))
# melina_speech = remove_stop_words(clean_text(melina_speech))


# print(check_text_similarity(michelle_speech, melina_speech))

# with open ("hacker_news.csv") as f:

#     csv_reader = csv.reader(f, delimiter = ",")
#     python_count = 0
#     js_count = 0
#     java_count = 0

#     for row in csv_reader:

#         row_text = " ".join(row).lower()

#         if "python" in row_text or "Python" in row_text:
#             python_count += 1
#         elif "JavaScript" in row_text or "javascript" in row_text or "Javascript" in row_text:
#             js_count += 1
#         elif "Java" in row_text or "java" in row_text:
#             java_count += 1

#     print(python_count)
#     print(js_count)
#     print(java_count)