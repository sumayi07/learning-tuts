# Day 18

import re

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."

def get_counts (txt):

    words = re.findall(r"\b\w+\b", txt)

    counts = {}

    for word in words:

        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

counts = get_counts(paragraph)

max_word = None
max_count = 0

for word, count in counts.items():

    if count > max_count:
        max_word = word
        max_count = count

print(max_count, max_word)

txt = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."

points =  [int(p) for p in re.findall(r"-?\d+", txt)]
distance = max(points) - min(points)
print(distance)

def is_valid_variable (name):

    pattern = r"^[a-zA-z_]\w*$"
    return bool(re.match(pattern, name))

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text (txt):

    pattern = r"[^a-zA-Z\s]"
    return re.sub(pattern, "", txt)

sentence = clean_text(sentence)
counts = get_counts(sentence)
sorted_counts = sorted(counts.items(), key = lambda x: x[1], reverse = True)

print(sorted_counts[:3])