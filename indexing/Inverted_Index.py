import os
from spacy.lang.en import English
path = r"C:\Users\tamog\PycharmProjects\CS 635 Assignment 1\Documents"
files = sorted(os.listdir(path))
tokenizer = English().tokenizer
id_list = dict() # Stores Document IDs of a given token
document_gap = dict() # Stores the gap between Document IDs of a particular token
count = {i: 0 for i in range(len(files))} # Stores the frequency of gap
for id, file in enumerate(files):
    data = open(os.path.join(path, file)).read()
    tokens = tokenizer(data)
    unique_tokens = set()
    for token in tokens:
        low = token.text.lower() # Convert tokens to lower case
        if low.isalnum(): # Checking if token is alphanumeric or not
            unique_tokens.add(low) # If it is then add it to the set
    for token in unique_tokens:
        if token in id_list.keys():
            id_list[token].append(id)
        else:
            id_list[token] = [id]
        if len(id_list[token]) == 1:
            count[id] += 1 # The first document ID in the id_list is also the gap
            document_gap[token] = [id]
        else:
            doc_id_gap = id_list[token][-1] - id_list[token][-2] # Calculating gap by subtracting last 2 elements of id_list
            count[doc_id_gap] += 1
            document_gap[token].append(doc_id_gap)
result_path = '../result/a1.txt'
open(result_path, 'w').write("\n".join(map(str, count.values())))