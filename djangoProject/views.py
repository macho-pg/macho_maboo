from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, CreateAPIView, UpdateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer

class BookListView():
    # 定义查询集以及序列化器类
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    def get(self, request, pk):
        book = self.get_object()
        s_book = self.get_serializer(book)
        return Response(s_book.data)



