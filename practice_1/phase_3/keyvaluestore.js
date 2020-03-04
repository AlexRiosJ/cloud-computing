var AWS = require('aws-sdk');
AWS.config.loadFromPath('./config.json');

var db = new AWS.DynamoDB();

function keyvaluestore(table) {
  this.LRU = require("lru-cache");
  this.cache = new this.LRU({ max: 500 });
  this.tableName = table;
};

/**
 * Initialize the tables
 * 
 */
keyvaluestore.prototype.init = function (whendone) {

  var tableName = this.tableName;

  var params = {
    TableName: tableName
  }

  db.describeTable(params, (err, data) => {
    if (err) {
      console.log(err);
    } else {
      console.log(data);
      whendone(); //Call Callback function.
    }
  });

};

/**
 * Get result(s) by key
 * 
 * @param search
 * 
 * Callback returns a list of objects with keys "inx" and "value"
 */
keyvaluestore.prototype.get = function (search, callback) {
  var self = this;

  if (self.cache.get(search)) {
    callback(null, self.cache.get(search));
  } else {

    let params = {
      TableName: this.tableName,
      KeyConditionExpression: "#key = :keyword",
      ExpressionAttributeNames: {
        "#key": "keyword"
      },
      ExpressionAttributeValues: {
        ":keyword": { S: search }
      }
    };

    db.query(params, (err, data) => {
      if (err) {
        console.log(err);
      } else {
        let items = [];
        for (let item of data.Items) {
          items.push({
            "keyword": item.keyword,
            "value": item.value.S
          });
        }
        self.cache.set(search, items);
        callback(null, items);
      };
    });
  }
};


module.exports = keyvaluestore;
