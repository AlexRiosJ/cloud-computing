import boto3
from boto3.dynamodb.conditions import Key


class DynamoStorage():
    def __init__(self, table_name="KeyValue"):
        super().__init__()

        self.dynamodb = boto3.resource("dynamodb")

        try:
            # pylint: disable=maybe-no-member
            self.dynamodb.create_table(
                AttributeDefinitions=[
                    {
                        "AttributeName": "keyword",
                        "AttributeType": "S"
                    },
                    {
                        "AttributeName": "inx",
                        "AttributeType": "N"
                    }
                ],
                TableName=table_name,
                KeySchema=[
                    {
                        "AttributeName": "keyword",
                        "KeyType": "HASH"
                    },
                    {
                        "AttributeName": "inx",
                        "KeyType": "RANGE"
                    }
                ],
                ProvisionedThroughput={
                    "ReadCapacityUnits": 5,
                    "WriteCapacityUnits": 5
                }
            )
        except Exception as e:
            print("Exception has ocurred on creating table '" + table_name + "': {}".format(
                e.__class__.__name__))
        else:
            print("Table '" + table_name + "' has been created successfuly!")

        self.table = self.dynamodb.Table(table_name) # pylint: disable=maybe-no-member

    def put_many_images(self, image_line, quantity, value_set):
        with self.table.batch_writer() as batch:
            repeated = {}
            for _ in range(quantity):
                image_triple = image_line.getNext()
                if image_triple[1] == "http://xmlns.com/foaf/0.1/depiction":
                    value_set.add(image_triple[0])
                    if image_triple[0] not in repeated:
                        batch.put_item(
                            Item={
                                "keyword": image_triple[0],
                                "inx": 0,
                                "value": image_triple[2],
                            }
                        )
                        repeated[image_triple[0]] = 1
                    else:
                        batch.put_item(
                            Item={
                                "keyword": image_triple[0],
                                "inx": repeated[image_triple[0]],
                                "value": image_triple[2],
                            }
                        )
                        repeated[image_triple[0]] += 1

    def put_many_labels(self, label_line, quantity, value_set, Stemmer):
        with self.table.batch_writer() as batch:
            repeated = {}
            for _ in range(quantity):
                label_triple = label_line.getNext()
                if label_triple[1] == "http://www.w3.org/2000/01/rdf-schema#label":
                    label_words = Stemmer.stem(label_triple[2]).split()
                    for word in label_words:
                        if label_triple[0] in value_set:
                            if word not in repeated:
                                batch.put_item(
                                    Item={
                                        "keyword": word,
                                        "inx": 0,
                                        "value": label_triple[0],
                                    }
                                )
                                repeated[word] = 1
                            else:
                                batch.put_item(
                                    Item={
                                        "keyword": word,
                                        "inx": repeated[word],
                                        "value": label_triple[0],
                                    }
                                )
                                repeated[word] += 1

    def get(self, key):
        res = self.table.query(
            KeyConditionExpression=Key("keyword").eq(key))
        matches = []
        for item in res["Items"]:
            matches.append(item["value"])

        return matches
