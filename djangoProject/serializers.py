from rest_framework import serializers
from .models import BookInfo
from .models import HeroInfo
class BookInfoSerializer(serializers.ModelSerializer):
    """
    图书数据序列化器
    """
    class Meta:
        model = BookInfo
        fields = '__all__'

class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    class Meta:
        model = HeroInfo
        fields = '__all__'

    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)
    hbook = serializers.PrimaryKeyRelatedField(label='图书', read_only=True)
