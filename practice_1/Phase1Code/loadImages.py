import keyvalue.sqlitekeyvalue as KeyValue
import keyvalue.parsetriples as ParseTriple
import keyvalue.stemmer as Stemmer


# Make connections to KeyValue
kv_labels = KeyValue.SqliteKeyValue("sqlite_labels.db","labels",sortKey=True)
kv_images = KeyValue.SqliteKeyValue("sqlite_images.db","images")

# Process Logic.
imageLine = ParseTriple.ParseTriples('./dataset/images.ttl')
labelLine = ParseTriple.ParseTriples('./dataset/labels_en.ttl')

print(labelLine.getNext()[2].split()) # Para obtener las palabras

# for i in range(1000):
#     imageTriple = imageLine.getNext()
#     if imageTriple[1] == 'http://xmlns.com/foaf/0.1/depiction':
#         kv_images.put(imageTriple[0], imageTriple[2])

#     labelTriple = labelLine.getNext()
#     if labelTriple[1] == 'http://www.w3.org/2000/01/rdf-schema#label':
#         kv_labels.putSort(labelTriple[0], 0, labelTriple)

# Close KeyValues Storages
kv_labels.close()
kv_images.close()







