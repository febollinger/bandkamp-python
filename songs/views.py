from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from .models import Song
from .serializers import SongSerializer


class PaginationSong(PageNumberPagination):
    page_size = 1


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_url_kwarg = "pk"

    pagination_class = PaginationSong

    def perform_create(self, serializer):
        return serializer.save(album_id=self.kwargs.get("pk"))
