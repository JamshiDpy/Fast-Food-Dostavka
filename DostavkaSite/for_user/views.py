from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from . import models
from for_admin import models as admin_model

from .serializers import (BotUsersSerializer, CategorySerializer, ProductSerializer, CategoryImageSerializer,
                          BasketSerializer, OrderSerializer)


class BotUserAPIView(APIView):
    serializer_class = BotUsersSerializer

    def get_object(self, pk=None):
        print(pk)
        if pk:
            try:
                pk = int(pk)
                user = models.BotUsers.objects.get(telegram_id=pk)
                return user
            except:
                raise Http404
        users = models.BotUsers.objects.all()
        return users

    def get(self, request, **kwargs):
        if 'pk' in kwargs:
            user = self.get_object(kwargs["pk"])
            serializer = BotUsersSerializer(user)
            return Response(serializer.data, status.HTTP_200_OK)
        users = self.get_object()
        serializer = BotUsersSerializer(users, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = BotUsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        if 'pk' in kwargs:
            user = self.get_object(kwargs["pk"])
            serializer = BotUsersSerializer(instance=user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status.HTTP_201_CREATED)
        raise Http404

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_200_OK)


# class BotUsersViewSet(ModelViewSet):
#     queryset = models.BotUsers.objects.all()
#     serializer_class = BotUsersSerializer


class CategoryImageView(APIView):
    def get(self, request):
        category = admin_model.CategoryImage.objects.all()
        serializer = CategoryImageSerializer(category.first())
        return Response(serializer.data, status.HTTP_200_OK)


class CategoryView(APIView):
    def get_object(self, pk=None):
        if pk:
            try:
                return admin_model.Categories.objects.get(id=pk)
            except:
                raise Http404
        return admin_model.Categories.objects.filter(child=None)

    def get(self, request, **kwargs):
        if 'pk' in kwargs:
            category = self.get_object(pk=kwargs['pk'])
            serializer = CategorySerializer(category)
            return Response(serializer.data, status.HTTP_200_OK)
        categories = self.get_object()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class ProductView(APIView):
    serializer_class = ProductSerializer

    def get(self, request, pk):
        try:
            category = admin_model.Categories.objects.get(id=pk)
            product = admin_model.Products.objects.filter(category=category)
            serializer = ProductSerializer(product, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            raise Http404


class ProductDetailView(APIView):
    serializer_class = ProductSerializer

    def get(self, request, pk):
        try:
            product = admin_model.Products.objects.get(id=pk)
            serializer = self.serializer_class(product)
            return Response(serializer.data)
        except:
            raise Http404


# class BasketView(ModelViewSet):
#     serializer_class = BasketSerializer
#     queryset = models.Basket.objects.all()
#
#     def create(self, request, *args, **kwargs):
#         print(kwargs)

class BasketView(APIView):
    serializer_class = BasketSerializer

    def get_object(self, user_id):
        try:
            basket = models.Basket.objects.filter(user__telegram_id=user_id, ordered=False)
            return basket
        except:
            raise Http404

    def get(self, request, user_id):

        serializer = self.serializer_class(self.get_object(user_id), many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, **kwargs):
        user = models.BotUsers.objects.get(telegram_id=kwargs['user_id'])
        product = admin_model.Products.objects.get(id=kwargs['product_id'])
        basket = models.Basket.objects.create(
            user=user,
            product=product,
            quantity=kwargs['qty']
        )
        return Response(self.serializer_class(basket).data, status.HTTP_201_CREATED)

    def delete(self, request, user_id):
        baskets = models.Basket.objects.filter(user__telegram_id=user_id)
        for b in baskets:
            b.delete()
        return Response({"message": "Delete successfully", "user_lang": baskets[0].user.language}, status.HTTP_200_OK)


class OrderView(APIView):
    serializer_class = OrderSerializer

    def get_object(self, order_id):
        try:
            order = models.Order.objects.get(id=order_id)
            return order
        except:
            raise Http404

    def get(self, request, order_id):
        serializer = self.serializer_class(self.get_object(order_id))

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, **kwargs):
        user = models.BotUsers.objects.get(telegram_id=kwargs['user_id'])
        basket = models.Basket.objects.filter(user=user, ordered=False)
        order = models.Order.objects.create(
            user=user,
            latitude=kwargs['lat'],
            longitude=kwargs['long']
        )
        for b in basket:
            order.orders.add(b)
            b.ordered = True
            b.save()
        serializer = self.serializer_class(order)

        return Response(serializer.data, status.HTTP_201_CREATED)

class OrderView2(APIView):
    serializer_class = OrderSerializer

    def get_object(self, order_id):
        try:
            order = models.Order.objects.get(id=order_id)
            return order
        except:
            raise Http404

    def get(self, request, order_id):
        serializer = self.serializer_class(self.get_object(order_id))
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, **kwargs):
        user = models.BotUsers.objects.get(telegram_id=kwargs['user_id'])
        basket = models.Basket.objects.filter(user=user, ordered=False)
        order = models.Order.objects.create(
            user=user
        )
        for b in basket:
            order.orders.add(b)
            b.ordered=True
            b.save()
        return Response(self.serializer_class(order).data, status.HTTP_201_CREATED)
