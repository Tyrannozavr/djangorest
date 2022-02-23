from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from .tasks import send

from .serializers import *
from authentication.permissions import IsOwnerOrReadOnly, IsStaff

@api_view(['GET'])
def root(request, format=None):
    return Response({
        'tickets': reverse('support:tickets-list', request=request, format=format),
        'message': reverse('support:message-list', request=request, format=format),
    })


class TicketList(ListCreateAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, status='unsolved')

class TicketDetail(RetrieveUpdateAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsStaff,)

    def perform_update(self, serializer):
        email = self.request.user.email
        serializer.save(status=self.request.data.get('status', ''))
        instance = serializer.save()
        # send.delay(email)


class MessageList(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        message = user.message.all()
        return message

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data.get('ticket').user, self.request.user)
        if serializer.validated_data.get('ticket').user == self.request.user or self.request.user.is_staff:

            serializer.save(owner=self.request.user)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class MessageDetail(RetrieveUpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsOwnerOrReadOnly,)

