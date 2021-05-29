from rest_framework import serializers


from ...models import Pug, Team


class PugSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pug
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = "__all__"