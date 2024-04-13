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
        user = self.context['request'].user
        gender = validated_data.get('gender')
        species = validated_data.get('species')
        quantity = validated_data.get('quantity')

        species, _ = Species.objects.get_or_create(name=species)

        fish = Fish.objects.create(
            user=user,
            gender=gender,
            species=species.id,
            quantity=quantity
        )
        aquarium = Aquarium.objects.get(user=user)
        aquarium.fish.add(fish)
        fish.save()
        return fish


class AlgaeSerializer(serializers.ModelSerializer):
    species = serializers.CharField(min_length=1)
    quantity = serializers.IntegerField()

    class Meta:
        model = Algae
        fields = ('species', 'quantity')

    def create(self, validated_data):
        user = self.context['request'].user
        species = validated_data.get('species')
        quantity = validated_data.get('quantity')

        species, _ = Species.objects.get_or_create(name=species)

        algae = Algae.objects.create(
            user=user,
            species=species.id,
            quantity=quantity
        )
        aquarium = Aquarium.objects.get(user=user)
        aquarium.algae.add(algae)
        algae.save()
        return algae


class AllAlgaeSerializer(serializers.ModelSerializer):
    species = AllSpeciesSerializer()

    class Meta:
        model = Algae
        fields = '__all__'


class AllShrimpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shrimp
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
        user = self.context['request'].user
        species = validated_data.get('species')
        quantity = validated_data.get('quantity')

        species, _ = Species.objects.get_or_create(name=species)

        shrimp = Shrimp.objects.create(
            user=user,
            species=species.id,
            quantity=quantity
        )
        aquarium = Aquarium.objects.get(user=user)
        aquarium.shrimp.add(shrimp)
        shrimp.save()
        return shrimp


class ResidentSerializer(serializers.ModelSerializer):
    fish = AllFishSerializer(many=True, required=False)
    algae = AllAlgaeSerializer(many=True, required=False)
    shrimp = AllShrimpSerializer(many=True, required=False)

    class Meta:
        model = Aquarium
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        fish_data = validated_data.pop('fish', [])
        algae_data = validated_data.pop('algae', [])
        shrimp_data = validated_data.pop('shrimp', [])

        aquarium = Aquarium.objects.create(user=user)

        for fish_id in fish_data:
            fish = Fish.objects.get(pk=fish_id)
            aquarium.fish.add(fish)

        for algae_id in algae_data:
            algae = Algae.objects.get(pk=algae_id)
            aquarium.algae.add(algae)

        for shrimp_id in shrimp_data:
            shrimp = Shrimp.objects.get(pk=shrimp_id)
            aquarium.shrimp.add(shrimp)

        aquarium.save()
        return aquarium

