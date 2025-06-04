from rest_framework import permissions, generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Ad, Review
from advertisements.pagination import AdPagination
from advertisements.serializers import AdSerializer, ReviewSerializer
from users.permissions import IsAuthor


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all().order_by('-created_at')
    serializer_class = AdSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']
    pagination_class = AdPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user.id)

    def perform_create(self, serializer):
        ad = serializer.save(author=self.request.user)
        ad.save()

    def get_permissions(self):
        if self.action in ('create', 'list', 'retrieve', 'update', 'destroy'):
            self.permission_classes = [IsAuthor], [IsAdminUser]
        return super().get_permissions()


class AdListAPIView(generics.ListAPIView):
    serializer_class = AdSerializer
    permission_classes = [AllowAny]
    pagination_class = AdPagination



class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer