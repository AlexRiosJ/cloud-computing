import keyvalue.sqlitekeyvalue as KeyValue
import keyvalue.parsetriples as ParseTriple
import keyvalue.stemmer as Stemmer


# Make connections to KeyValue
kv_labels = KeyValue.SqliteKeyValue("sqlite_labels.db","labels",sortKey=True)
kv_images = KeyValue.SqliteKeyValue("sqlite_images.db","images")

# Process Logic.
line = ParseTriple.ParseTriples('./dataset/images.ttl')
for i in range(1000):
    triple = line.getNext()
    if triple[1] == 'http://xmlns.com/foaf/0.1/depiction':
        kv_images.put(triple[0], triple[2])

# Close KeyValues Storages
kv_labels.close()
kv_images.close()







