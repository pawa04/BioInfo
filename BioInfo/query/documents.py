# myapp/documents.py

from elasticsearch_dsl import Document, Text, Date

class MyDocument(Document):
    title = Text()
    content = Text()
    created_at = Date()
