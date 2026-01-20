from django.contrib.auth.models import User
from rest_framework import generics, viewsets, permissions
from .serializers import UserSerializer, NoteSerializer
from .models import Note

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only show notes owned by the current user
        return Note.objects.filter(owner=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        # Set the owner to the current user when creating
        serializer.save(owner=self.request.user)
