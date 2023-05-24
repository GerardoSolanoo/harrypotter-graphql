import graphene
from graphene_django import DjangoObjectType
from .models import Character
from graphene import Mutation

class CharacterType(DjangoObjectType):
    class Meta:
        model = Character

class Query(graphene.ObjectType):
    characters = graphene.List(CharacterType)

    def resolve_characters(self, info):
        return Character.objects.all()

class CreateCharacterMutation(Mutation):
    class Arguments:
        name = graphene.String()
        lastname = graphene.String()
        house = graphene.String()
        patronus = graphene.String()

    character = graphene.Field(CharacterType)

    def mutate(self, info, name, lastname, house, patronus):
        character = Character(name=name, lastname=lastname, house=house, patronus=patronus)
        character.save()
        return CreateCharacterMutation(character=character)

class Mutation(graphene.ObjectType):
    create_character = CreateCharacterMutation.Field()
