from sklearn.preprocessing import MultiLabelBinarizer
import numpy
import math


def normalize(termFreqList):
    magnitude_val = 0
    pow_val = 0
    normalize_list = []
    for freq in termFreqList:
        pow_val += pow(freq, 2)
    magnitude_val = math.sqrt(pow_val)
    for freq in termFreqList:
        normalize_list.append(freq / magnitude_val)
    return normalize_list


def cosineSimilarity(tweet_dict1, tweet_dict2):
    terms_list = []
    terms_doc_matrix = []
    dict1List = sorted([w for w, val in tweet_dict1.items()])
    dict2List = sorted([w for w, val in tweet_dict2.items()])
    terms_list.extend(dict1List)
    terms_list.extend(
        [w for w in dict2List if w not in dict1List])
    terms_list = sorted(terms_list)
    bag_vector = [0] * len(terms_list)
    for w in dict1List:
        for i, word in enumerate(terms_list):
            if word == w:
                bag_vector[i] += 1
    terms_doc_matrix.append(bag_vector)
    bag_vector = [0] * len(terms_list)
    for w in dict2List:
        for i, word in enumerate(terms_list):
            if word == w:
                bag_vector[i] += 1
    terms_doc_matrix.append(bag_vector)
    normalize_vector1 = normalize(terms_doc_matrix[0])
    normalize_vector2 = normalize(terms_doc_matrix[1])

    prodA_B = 0
    normA = 0
    normB = 0

    for i in range(len(bag_vector)):
        prodA_B += normalize_vector1[i] * normalize_vector2[i]
        normA += math.pow(normalize_vector1[i], 2)
        normB += math.pow(normalize_vector2[i], 2)

    return prodA_B/(math.sqrt(normA) * math.sqrt(normB))

    # print(terms_doc_matrix)
    # print("{0}\n{1}\n".format(dict1List, bag_vector))

    # return terms_list
