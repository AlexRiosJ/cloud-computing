import keyvalue.dynamostorage as DynamoStorage
import keyvalue.parsetriples as ParseTriple
import keyvalue.stemmer as Stemmer
import sys


# Make connections to KeyValue
kv_labels = DynamoStorage.DynamoStorage("labels")
kv_images = DynamoStorage.DynamoStorage("images")

# Process Logic.
image_line = ParseTriple.ParseTriples("./dataset/images.ttl")
label_line = ParseTriple.ParseTriples("./dataset/labels_en.ttl")

quantity = int(sys.argv[1])

value_set = set()
kv_images.put_many_images(image_line, quantity, value_set)
kv_labels.put_many_labels(label_line, quantity, value_set, Stemmer)
