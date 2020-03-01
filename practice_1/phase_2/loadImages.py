# import keyvalue.sqlitekeyvalue as KeyValue
import keyvalue.dynamostorage as DynamoStorage
import keyvalue.parsetriples as ParseTriple
import keyvalue.stemmer as Stemmer
import sys


# Make connections to KeyValue
kv_labels = KeyValue.SqliteKeyValue("sqlite_labels.db","labels",sortKey=True)
kv_images = DynamoStorage.DynamoStorage("config_path","images")

# Process Logic.
imageLine = ParseTriple.ParseTriples("./dataset/images.ttl")
labelLine = ParseTriple.ParseTriples("./dataset/labels_en.ttl")
repeatedWords = {}

for i in range(int(sys.argv[1])):
    imageTriple = imageLine.getNext()
    images = {}
    if imageTriple[1] == "http://xmlns.com/foaf/0.1/depiction":
        images[imageTriple[0]] = imageTriple[2]



    # labelTriple = labelLine.getNext()
    # if labelTriple[1] == "http://www.w3.org/2000/01/rdf-schema#label":
    #     labelWords = Stemmer.stem(labelTriple[2]).split()
    #     for word in labelWords:
    #         if word not in repeatedWords:
    #             kv_labels.putSort(word, str(0), labelTriple[0])
    #             repeatedWords[word] = 1
    #         else:
    #             kv_labels.putSort(word, str(repeatedWords[word]), labelTriple[0])
    #             repeatedWords[word] += 1

# Close KeyValues Storages
kv_labels.close()
kv_images.close()







