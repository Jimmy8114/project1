from rest_framework import serializers
from .models import Human

#定义序列化器，把object转换为json，以及把json转换为object
class HumanSerializer(serializers.ModelSerializer):
    #定义每一个需要序列化/反序列化的字段，跟模型的字段一样
    #humanName = serializers.CharField(label='姓名',max_length=20)
    #humanAge = serializers.IntegerField()
    class Meta:
       model = Human
       fields = '__all__'

    # 给定经过验证的数据，创建并返回一个新的 Human 实例
    def create(self, validated_data):
        return Human.objects.create(**validated_data)

    # 给定经过验证的数据，更新并返回一个已经存在的 Human 实例
    def update(self, instance, validated_data):
        instance.humanName = validated_data.get('humanName', instance.humanName)
        instance.humanAge = validated_data.get('humanAge', instance.humanAge)
        instance.save()
        return instance

