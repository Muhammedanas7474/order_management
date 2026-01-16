from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Product, Order, OrderItem
from .serializers import RegisterSerializer, ProductSerializer, OrderSerializer
from .permissions import IsAdmin


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered"})
        return Response(serializer.errors, status=400)


class ProductAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request):
        products = Product.objects.all()
        return Response(ProductSerializer(products, many=True).data)



class OrderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        order = Order.objects.create(customer=request.user)

        for item in request.data.get('items', []):
            product = Product.objects.get(id=item['product'])
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item['quantity'],
                price=product.price
            )

        return Response(OrderSerializer(order).data, status=201)

    def get(self, request):
        if request.user.is_admin:
            orders = Order.objects.all()
        else:
            orders = Order.objects.filter(customer=request.user)

        return Response(OrderSerializer(orders, many=True).data)
