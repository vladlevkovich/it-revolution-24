from rest_framework import serializers
from .models import *


class AllGenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'


class AllSpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = '__all__'


class AllFishSerializer(serializers.ModelSerializer):
    gender = AllGenderSerializer()
    species = AllSpeciesSerializer()

    class Meta:
        model = Fish
        fields = '__all__'


class AddFishSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(min_length=1)
    species = serializers.CharField(min_length=1)
    quantity = serializers.IntegerField()

    class Meta:
        model = Fish
        fields = ('gender', 'species', 'quantity')

    def create(self, validated_data):
        gender = validated_data.get('gender')
        species = validated_data.get('species')
        quantity = validated_data.get('quantity')

        species = Species.objects.get_or_create(name=species)

        fish = Fish.objects.create(
            gender=gender,
            species=species.id,
            quantity=quantity
        )
        fish.save()
        return fish


class AlgaeSerializer(serializers.ModelSerializer):
    species = serializers.CharField(min_length=1)
    quantity = serializers.IntegerField()

    class Meta:
        model = Algae
        fields = ('species', 'quantity')

    def create(self, validated_data):
        species = validated_data.get('species')
        quantity = validated_data.get('quantity')

        species = Species.objects.get_or_create(name=species)

        algae = Algae.objects.create(
            species=species.id,
            quantity=quantity
        )
        algae.save()
        return algae


class AllAlgaeSerializer(serializers.ModelSerializer):
    species = AllSpeciesSerializer()

    class Meta:
        model = Algae
        fields = '__all__'


class ShrimpSerializer(serializers.ModelSerializer):
    # gender = serializers.CharField(min_length=1)
    species = serializers.CharField(min_length=1)
    quantity = serializers.IntegerField()

    class Meta:
        model = Shrimp
        fields = ('species', 'quantity')

    def create(self, validated_data):
        # gender = validated_data.get('gender')
        species = validated_data.get('species')
        quantity = validated_data.get('quantity')

        species = Species.objects.get_or_create(name=species)

        shrimp = Shrimp.objects.create(
            species=species.id,
            quantity=quantity
        )
        shrimp.save()
        return shrimp
