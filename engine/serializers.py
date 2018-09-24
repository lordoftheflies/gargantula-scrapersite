from django.contrib.auth import models as auth_model
from rest_framework import serializers as rest_serializers
from . import models


class ArgumentSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = models.ArgumentModel
        fields = ['id', 'slug', 'friendly_name', 'description', 'data_type', 'default_value', 'tag']


class PropertySerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = models.PropertyModel
        fields = ['id', 'slug', 'friendly_name', 'description', 'data_type', 'default_value', 'tag']


class ProcessSerializer(rest_serializers.ModelSerializer):
    queryset = models.ProcessModel.objects.all()
    arguments = ArgumentSerializer(many=True, read_only=True)
    properties = PropertySerializer(many=True, read_only=True)

    class Meta:
        model = models.ProcessModel
        fields = [
            'id',
            'slug',
            'friendly_name',
            'description',
            'active',
            'arguments',
            'parameters',
            'notebook',
            'properties',
            'schema',
            'notebook_filename',
            'notebook_basename',
        ]


class ProcessItemSerializer(rest_serializers.ModelSerializer):
    queryset = models.ProcessModel.objects.all()

    # arguments = ArgumentSerializer(many=True, source='arguments', read_only=True)

    class Meta:
        model = models.ProcessModel
        fields = [
            'id',
            'slug',
            'friendly_name',
            'description',
            'active'
        ]


class ExecutionSerializer(rest_serializers.ModelSerializer):
    queryset = models.ExecutionModel.objects.all()
    process = rest_serializers.PrimaryKeyRelatedField(required=True, queryset=models.ProcessModel.objects.all())

    class Meta:
        model = models.ExecutionModel
        fields = [
            'id',
            'process',
            'started',
            'ended',
            'arguments',
            'status',
            'friendly_name'
        ]

class ExecutionItemSerializer(rest_serializers.ModelSerializer):
    queryset = models.ExecutionModel.objects.all()
    # process = rest_serializers.PrimaryKeyRelatedField(required=True, queryset=models.ProcessModel.objects.all())

    class Meta:
        model = models.ExecutionModel
        fields = [
            'id',
            # 'process',
            'started',
            'ended',
            'arguments',
            'status',
            'friendly_name'
        ]

class ExecutionDashbordSerializer(rest_serializers.ModelSerializer):
    queryset = models.ExecutionModel.objects.all()

    class Meta:
        model = models.ExecutionModel
        fields = [
            'id',
            'process',
            'started',
            'ended',
            'dashboard',
            'status',
            'friendly_name'
        ]


class UserSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = auth_model.User
        fields = ['id', 'username', 'email']
