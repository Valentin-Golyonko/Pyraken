from rest_framework import serializers


class DrawFlagSerializer(serializers.Serializer):
    even_number = serializers.IntegerField(
        required=True,
        min_value=1,
        label='Enter even number to draw japanese flag',
        style={'class': "form-control"},
    )

    def validate(self, attrs):
        if attrs.get('even_number') % 2:
            raise serializers.ValidationError("The number should be even!")

        return attrs
