from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch("http://localhost:9200")

query = {
    "any":"data", 
    "timestamp":datetime.now()
}

# es = Elasticsearch({"scheme": "http", "host": "localhost", "port": 9200})
es.index(index="my_another_index", doc_type="test_type", id=42, body=query)