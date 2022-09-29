# CS-635-Assignment 1
Dataset used : 6 (as my Roll number is 190100126) <br>
Data Structures used : 3 dictionaries were created namely <b>id_list</b> which stores the document IDs of a given token, <b>document_gap</b> which stores the gap between document IDs of a given token and <b>count</b> which stores the frequency of each document ID gap <br>
Algorithm used : The documents were tokenized by using the spacy library. Every token was converted to lower case letter using .lower() fuction of token.text and I ensured that the tokens are not repeated by storing them in a set. After that I iterated through all the tokens and updated my dictionaries accordingly.
