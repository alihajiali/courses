from elasticsearch import Elasticsearch

es = Elasticsearch("http://157.90.207.108:6700",
    basic_auth=("elastic", "ali110ali"))

q = {
  "query": {
    "match_all": {}
  }
}

res = es.search(index="insta_posts", body=q)

# es.index(index='aliii', document={"field1": "salam"})

print(res)

