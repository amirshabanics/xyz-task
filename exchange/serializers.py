from rest_framework import serializers
from exchange.models import Index
import datetime


class IndexSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # index = serializers.IntegerField(min_value=0)
    value = serializers.FloatField(source="index", read_only=True)
    timestamp = serializers.SerializerMethodField(read_only=True)
    datetime = serializers.IntegerField(write_only=True, )
    index = serializers.FloatField(write_only=True, )

    def get_timestamp(self, obj: Index):
        return obj.datetime.timestamp()

    def validate_datetime(self, value):
        return datetime.datetime.fromtimestamp(value)

    class Meta:
        model = Index
        fields = ['timestamp', 'value', 'datetime', 'index']
