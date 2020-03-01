import boto3
from boto3.dynamodb.conditions import Key
from .config import Config


class DynamoSorage():
    def __init__(self, config_path, table_name="KeyValue", sort_key=False):
        super().__init__()
        self.config = Config(config_path)

        try:
            if not sort_key:
                self.dynamodb.create_table(
                    AttributeDefinitions=[
                        {
                            "AttributeName": "keyword",
                            "AttributeType": "S"
                        }
                    ],
                    TableName=table_name,
                    KeySchema=[
                        {
                            "AttributeName": "keyword",
                            "KeyType": "HASH"
                        }
                    ],
                    ProvisionedThroughput={
                        "ReadCapacityUnits": 5,
                        "WriteCapacityUnits": 5
                    }
                )
            else:
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
            print("Exception has ocurred on creating table: {}".format(
                e.__class__.__name__))
        else:
            print("Table has been created successfuly!")

        self.table = self.dynamodb.Table(table_name)

    def put(self, category, url):
        try:
            # print("Inserting ", category, "->", url)
            self.table.put_item(
                Item={
                    "keyword": category,
                    "url": url,
                }
            )
        except Exception as e:
            print("Exception has ocurred while adding item to table: {}".format(
                e.__class__.__name__))
        else:
            print("Item added successfuly!")

    def put_sort(self, label, sort, category):
        try:
            # print("Inserting (", label,",", sort, ") ->", category)
            self.labels_table.put_item(
                Item={
                    "keyword": label,
                    "inx": int(sort),
                    "category": category
                }
            )
        except Exception as e:
            print("Exception has ocurred while ocurred adding item to table: {}".format(
                e.__class__.__name__))
        else:
            print("Item added successfuly!")

    def get(self, key):
        res = self.table.query(
            KeyConditionExpression=Key("keyword").eq(key))
        categories = []
        row = []
        for item in res["Items"]:
            categories.append(item["category"])

        for cat in categories:
            r = self.images_table.get_item(
                Key={"keyword": cat},
                AttributesToGet=["url"],
            )
            row.append(r["Item"]["url"])
        return row
