import keyvalue.sqlitekeyvalue as KeyValue
import keyvalue.parsetriples as ParseTripe
import keyvalue.stemmer as Stemmer
import sys

# Make connections to KeyValue
kv_labels = KeyValue.SqliteKeyValue("sqlite_labels.db","labels",sortKey=True)
kv_images = KeyValue.SqliteKeyValue("sqlite_images.db","images")

# Process Logic.
urls = set()
for word in sys.argv[1:]:
    word = Stemmer.stem(word)
    wikis = kv_labels.get(word)
    for wiki in wikis:
        wiki = wiki[0]
        if wiki is not None:
            url = kv_images.get(wiki)
            if url is not None and len(url) > 0:
                urls.add(url[0][0])

print(list(urls))

# Close KeyValues Storages
kv_labels.close()
kv_images.close()







