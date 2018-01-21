ES权威指南1



RESTful API

```shell
curl -X<VERB> '<PROTOCOL>://<HOST>:<PORT>/<PATH>?<QUERY_STRING>' -d '<BODY>'

eg.
curl -XGET 'http://192.168.43.29:9200/_count?pretty' -d '{
  "query":{
    "match_all":{}
  }
}'
#简写成
GET /_count
{
  "query":{
    "match_all":{}
  }
}
```



面向文档（对象）JSON

存储数据到ES的行为成为“索引”，索引一个文档

集群 - 多个索引

索引 - 多个类型

类型 - 多个文档

文档 - 多个属性





1、添加文档 PUT

```Json
curl -XPUT 'localhost:9200/megacorp/employee/1?pretty' -H 'Content-Type: application/json' -d'
{
    "first_name" : "John",
    "last_name" :  "Smith",
    "age" :        25,
    "about" :      "I love to go rock climbing",
    "interests": [ "sports", "music" ]
}
'
```



2、查找文档 GET - 根据id查找

```shell
curl -XGET 'localhost:9200/megacorp/employee/1?pretty'
```

结果：

```json
{
  "_index" : "megacorp",
  "_type" : "employee",
  "_id" : "1",
  "_version" : 1,
  "found" : true,
  "_source" : {
    "first_name" : "John",
    "last_name" : "Smith",
    "age" : 25,
    "about" : "I love to go rock climbing",
    "interests" : [
      "sports",
      "music"
    ]
  }
}
```

_index	：索引

_type  	：类型

_id      	：内置id属性，即查找的条件

found	：是否找到

_source	：查找到的内容，如果found为false则无该属性



2、查找文档 GET - 简单查找

默认查出10条记录

```shell
curl -XGET 'http://localhost:9200/megacorp/employee/_search'
```



根据参数查找

```shell
curl -XGET 'http://localhost:9200/megacorp/employee/_search?q=last_name:Smith'
```



DSL 特定领域语言 查询

```shell
curl -XGET 'localhost:9200/megacorp/employee/_search?pretty' -H 'Content-Type: application/json' -d'
{
    "query" : {
        "match" : {
            "last_name" : "Smith"
        }
    }
}
'
# 查找last_name完全匹配Smith的文档
```

e.g. 

```shell
curl -XGET 'localhost:9200/megacorp/employee/_search?pretty' -H 'Content-Type: application/json' -d'
{
    "query" : {
        "bool": {
            "must": {
                "match" : {
                    "last_name" : "smith" 
                }
            },
            "filter": {
                "range" : {
                    "age" : { "gt" : 30 } 
                }
            }
        }
    }
}
'
# 查找last_name是Smith，且age>30的文档
```



3、全文搜索

ES在全文属性上搜索并返回相关性最强的结果，相比与传统数据库，只有匹配与不匹配两种结果。

```shell
curl -XGET 'localhost:9200/megacorp/employee/_search?pretty' -H 'Content-Type: application/json' -d'
{
    "query" : {
        "match" : {
            "about" : "rock climbing"
        }
    }
}
'
# 全文查找about属性中"rock climbing"的文档，根据相关性高低输出
```

如果想要全部匹配：

```shell
curl -XGET 'localhost:9200/megacorp/employee/_search?pretty' -H 'Content-Type: application/json' -d'
{
    "query" : {
        "match_phrase" : {
            "about" : "rock climbing"
        }
    }
}
'
# about属性完全匹配"rock climbing"
```



4、分析，聚合

ES 5.x后对排序/聚合这些操作用单独的数据结构(fielddata)缓存到内存里，需要单独开启

```shell
curl -XPUT 'localhost:9200/megacorp/_mapping/employee' -H 'Content-Type: application/json' -d'
{
  "properties": {
    "interests": { 
      "type":     "text",
      "fielddata": true
    }
  }
}
'
# 开启interests字段fielddata

curl -XGET 'localhost:9200/megacorp/employee/_search?pretty' -H 'Content-Type: application/json' -d'
{
  "aggs": {
    "all_interests": {
      "terms": { 
        "field": "interests" 
      }
    }
  }
}
'
# 对interests字段进行聚合操作，命名为all_interests


curl -XGET 'localhost:9200/megacorp/employee/_search?pretty' -H 'Content-Type: application/json' -d'
{
    "aggs" : {
        "all_interests" : {
            "terms" : { "field" : "interests" },
            "aggs" : {
                "avg_age" : {
                    "avg" : { "field" : "age" }
                }
            }
        }
    }
}
'
# 在interests字段上聚合之后，求出每个聚合段内的age的平均值
```



