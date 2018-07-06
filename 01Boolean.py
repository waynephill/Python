#Calculate alphabetical order of two words
print ("Alphabetical order of two words:")
word1 = "cat"
word2 = "dog"

if word1<word2:
    word1first = True
else:
    word1first = False

if word1first:
    print(word1 + " comes before " + word2)
else:
    print(word1 + " comes after " + word2)
