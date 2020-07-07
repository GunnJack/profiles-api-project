from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out api view"""
    name = serializers.CharField(max_length=10)
    
