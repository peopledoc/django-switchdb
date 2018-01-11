# -*- coding: utf-8 -*-

from rest_framework import serializers

from demo_app.models import ItemForTest


class ItemForTestSerializer(serializers.Serializer):
    number_items_for_test = serializers.SerializerMethodField()

    class Meta:
        fields = ('number_items_for_test',)

    def get_number_items_for_test(self, data):
        return ItemForTest.objects.all().count()
