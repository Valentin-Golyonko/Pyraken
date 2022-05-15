from rest_framework import serializers


class DrawFlagSerializer(serializers.Serializer):
    number = serializers.IntegerField(
        required=True,
        min_value=1,
    )

    def validate(self, attrs: dict) -> dict:
        if attrs.get('number') % 2:
            raise serializers.ValidationError({'number': "The number should be even!"})

        return attrs
