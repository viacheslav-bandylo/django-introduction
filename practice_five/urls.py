from django.urls import path, include
from practice_five.views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation for the project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@local.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'addresses', AddressViewSet)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('orders/', OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailUpdateDeleteView.as_view(), name='order-list'),
    path('products/<int:pk>/', ProductDetailUpdateDeleteView.as_view()),
    path('product-details/', ProductDetailListCreateView.as_view()),
    path('product-details/<int:pk>/', ProductDetailRetrieveUpdateDeleteView.as_view()),
    path('customers/', CustomerListCreateView.as_view()),
    path('customers/<int:pk>/', CustomerDetailUpdateDeleteView.as_view()),
    path('orders/statistics/', OrderStatisticsView.as_view(), name='order-statistics'),
]
