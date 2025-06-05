from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Ad, Review
from advertisements.pagination import AdPagination
from advertisements.serializers import AdSerializer, ReviewSerializer
from users.permissions import IsAuthor


class AdViewSet(ModelViewSet):
    """
    CRUD объявлений
    """
    queryset = Ad.objects.all().order_by('-created_at')
    serializer_class = AdSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']
    pagination_class = AdPagination
    permission_classes = [IsAuthenticated, IsAuthor | IsAdminUser]

    def perform_create(self, serializer):
        ad = serializer.save(author=self.request.user)
        ad.save()


class AdListAPIView(generics.ListAPIView):
    """
        Контроллер для вывода списка объявлений
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [AllowAny]
    pagination_class = AdPagination



class ReviewViewSet(ModelViewSet):
    """
        CRUD комментариев
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsAuthor | IsAdminUser]

    def perform_create(self, serializer):
        review= serializer.save(author=self.request.user)
        review.save()

