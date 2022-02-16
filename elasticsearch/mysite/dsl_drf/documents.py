from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer

from .models import Publisher

# Name of the Elasticsearch index
PUBLISHER_INDEX = Index('publisher')
# See Elasticsearch Indices API reference for available settings
PUBLISHER_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

@PUBLISHER_INDEX.doc_type
class PublisherDocument(Document):
    """Publisher Elasticsearch document."""

    id = fields.IntegerField(attr='id')

    name = fields.TextField(
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    info = fields.TextField(
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    address = fields.TextField(
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    city = fields.TextField(
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    state_province = fields.TextField(
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    country = fields.TextField(
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    website = fields.TextField()

    # Location
    location = fields.GeoPointField(attr='location_field_indexing')

    class Django:
        """Meta options."""

        model = Publisher  # The model associate with this Document
