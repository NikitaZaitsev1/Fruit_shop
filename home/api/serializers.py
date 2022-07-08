from rest_framework.serializers import ModelSerializer

from home.models import FeedBack


class FeedBackSerializer(ModelSerializer):
    class Meta:
        model = FeedBack
        fields = ('id','full_name','phone','email','message')
