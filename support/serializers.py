from rest_framework import serializers

from .models import *


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    ticket_detail = serializers.HyperlinkedIdentityField(many=False, view_name='support:tickets-detail', read_only=True)
    messages = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Tickets
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    serializers.CharField()
    ticket = serializers.PrimaryKeyRelatedField(queryset=Tickets.objects.all())
    owner = serializers.StringRelatedField(many=False)
    class Meta:
        model = Message
        fields = '__all__'