import nltk
import numpy
import collections

#text_to_parse = "How much wood could a woodchuck burn if a woodchuck could obtain wood"
text_to_parse = "They refuse to permit us to obtain the refuse permit. How could they refuse us?"

text = nltk.word_tokenize(text_to_parse)
output = nltk.pos_tag(text)

#print output

noun_list = []
verb_list = []

for element in output:
    if "NN" in str(element[1]):
        noun_list.append(element[0])
    if "VB" in str(element[1]):
        verb_list.append(element[0])

#print noun_list
#print verb_list

noun_counter = collections.Counter(noun_list)
noun_counts = noun_counter.most_common()
print noun_counts

verb_counter = collections.Counter(verb_list)
verb_counts = verb_counter.most_common()
print verb_counts

keywords = "Nouns:"

for noun_tuple in noun_counts:
    #print noun_tuple
    noun_str = str(noun_tuple[0]) + " : " + str(noun_tuple[1])
    keywords = keywords + "\n" + noun_str


keywords = keywords + "\n" + "Verbs:"

for verb_tuple in verb_counts:
    #print verb_tuple
    verb_str = str(verb_tuple[0]) + " : " + str(verb_tuple[1])
    keywords = keywords + "\n" + verb_str


print keywords 

print "Nouns:\nHow : 1\nrefuse : 1\npermit. : 1\nVerbs:\nrefuse : 2\nobtain : 1\npermit : 1"