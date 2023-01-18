from rest_framework import serializers
from core.models import Tag, Ingredient, Recipe


class TagSerializer(serializers.ModelSerializer):
	"""docstring for TagSerialiser"""
	class Meta():
		model = Tag
		fields = ('id','name')
		read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
	class Meta():
		model = Ingredient
		fields = ('id','name')
		read_only_fields = ('id',)


class RecipeSerializer(serializers.ModelSerializer):
	ingredients = serializers.PrimaryKeyRelatedField(
		many=True,
		queryset=Ingredient.objects.all()
	)
	Tag = serializers.PrimaryKeyRelatedField(
		many=True,
		queryset=Tag.objects.all()
	)
	class Meta:
		model = Recipe
		fields = ('id','title','ingredient','tag','time_minutes','price','link')
		read_only_fields = ('id',)


class RecipeDetailSerializer(RecipeSerializer):
	ingredients = IngredientSerializer(many=True, read_only=True)
	tags = TagSerializer(many=True, read_only=True)
 