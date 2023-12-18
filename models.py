from mongoengine import (Document, StringField, DateTimeField, ListField,
                         EmbeddedDocument, EmbeddedDocumentField)

# Embed 사용 - 하나의 문서 안에 다른 문서를 중첩시켜 저장할 수 있다.
# 내장 문서는 부모 문서에 종속되므로 부모 문서가 삭제되면 내장 문서도 함께 삭제된다.
# 게시판 목적에 더 적합하다고 판단

class Answer(EmbeddedDocument):

    #author = StringField(required=True)
    content = StringField(required=True)
    create_date = DateTimeField(required=True)

class Question(Document):

    #author = StringField(required=True)
    subject = StringField(required=True)
    content = StringField(required=True)
    create_date = DateTimeField(required=True)
    answers = ListField(EmbeddedDocumentField(Answer))