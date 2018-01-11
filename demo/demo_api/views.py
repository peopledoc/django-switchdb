# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .serializers import ItemForTestSerializer


class ItemForTestApiView(GenericAPIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    renderer_classes = (JSONRenderer,)
    serializer_class = ItemForTestSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={})
        serializer.is_valid()
        return Response(serializer.data)
