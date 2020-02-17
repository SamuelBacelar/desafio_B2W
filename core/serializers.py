from rest_framework import serializers
from .models import Planet


class PlanetSerializer(serializers.ModelSerializer):
    # climate = serializers.CharField(required=False)
    # terrain = serializers.CharField(required=False)
    # moviesAppearances = serializers

    class Meta:
        model = Planet
        fields = (
            'name', 'climate', 'terrain', 'moviesAppearances'
        )