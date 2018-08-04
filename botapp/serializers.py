# from rest_framework import generics, serializers
# from botapp import models as botapp_models
#
#
# class ProjectItemSerializer(serializers.ModelSerializer):
#     queryset = botapp_models.ProjectModel.objects.all()
#
#     class Meta:
#         model = botapp_models.ProjectModel
#         fields = ('pk', 'name', 'version', 'spider')
#
# class ProjectDetailsSerializer(serializers.ModelSerializer):
#     queryset = botapp_models.ProjectModel.objects.all()
#     steps = serializers.PrimaryKeyRelatedField(many=True, queryset=botapp_models.ProjectStepModel.objects.all())
#
#     class Meta:
#         model = botapp_models.ProjectModel
#         fields = ('pk', 'name', 'version', 'spider', 'steps')
#
# class ProjectStepSerializer(serializers.ModelSerializer):
#     queryset = botapp_models.ProjectStepModel.objects.all()
#
#     class Meta:
#         model = botapp_models.ProjectStepModel