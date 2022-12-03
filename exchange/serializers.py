from rest_framework import serializers
from exchange.models import Index


class IndexSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # index = serializers.IntegerField(min_value=0)
    # timestamp = serializers.CharField()

    class Meta:
        model = Index
        fields = ['id', 'index', 'timestamp']
