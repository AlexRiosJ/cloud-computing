import keyvalue.dynamostorage as DynamoStorage
import keyvalue.parsetriples as ParseTriple
import keyvalue.stemmer as Stemmer
import sys

# Make connections to KeyValue
kv_labels = DynamoStorage.DynamoStorage("labels")
kv_images = DynamoStorage.DynamoStorage("images")

# Process Logic.
urls = set()
for word in sys.argv[1:]:
    word = Stemmer.stem(word)
    wikis = kv_labels.get(word)
    for wiki in wikis:
        if wiki is not None:
            res = kv_images.get(wiki)
            if res is not None and len(res) > 0:
                for url in res:
                    urls.add(url)

if len(urls) > 0:
    print(urls)
else:
    print({})