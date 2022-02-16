from django_elasticsearch_dsl import Document, fields 
from django_elasticsearch_dsl.registries import registry
from .models import Post, Hashtag, InstagramUser

@registry.register_document
class HashtagDocument(Document):
    class Index:
        name = 'hashtags'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}
    class Django:
        model = Hashtag
        fields = [
            'name', 
            'id'
        ]


@registry.register_document
class InstagramUserDocument(Document):
    class Index:
        name = 'instagram_users'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}
    class Django:
        model = InstagramUser
        fields = [
            'name'
        ]



@registry.register_document
class PostDocument(Document):

    instagram_user = fields.ObjectField(properties={
        'name': fields.TextField(),
    })

    hashtag = fields.ObjectField(properties={
        'name': fields.TextField(),
    })

    class Index:
        name = 'posts'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}
    class Django:
        model = Post
        fields = [
            'title'
        ]
        related_models = ['hashtag', 'instagram_users']