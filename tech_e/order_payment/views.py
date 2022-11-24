from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from authenticate.models import UserProfile
from django.contrib.auth.models import User
from order_payment.models import Order, OrderDetail
from order_payment.serializer import OrderDetailSerializer, OrderSerializer
from rest_framework import status
from django.http.request import QueryDict, MultiValueDict

class OrderViewSet(ViewSet):
    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create', 'destroy']:
            return [AllowAny(), ]
        return super().get_permissions()
    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    def retrieve(self, request, pk=None):
        product = Order.objects.filter(pk=pk).get()
        serializer = OrderSerializer(product)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    def create(self, request):
        data_request = request.data
        serializer = OrderSerializer(data=data_request)
        if not serializer.is_valid():
            return Response({
                    'message':'Order is failed!',
                    'errors': serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer.save()
        return Response({
                'message':'Order is Success!',
                'data':serializer.data
            },
            status=status.HTTP_201_CREATED,
        )
    def destroy(self, request, pk=None):
        order = Order.objects.get(pk=pk)
        if order is None:
            return Response({
                'message':'Order do not Exists!',
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
        order.delete()
        return Response({
                'message':'Delete order is success',
            },
            status=status.HTTP_200_OK,
        )


class OrderDetailViewSet(ViewSet):
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny(), ]
        return super().get_permissions()

    def list(self, request):
        queryset = OrderDetail.objects.all()
        serializer = OrderDetailSerializer(queryset, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        product = OrderDetail.objects.filter(pk=pk).get()
        serializer = OrderDetailSerializer(product)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)