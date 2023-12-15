from django.contrib import admin
from django.urls import path
from product import views
from users import views as users_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/category/', views.category_list_view),
    path('api/v1/category/<int:id>', views.category_detail_view),
    path('api/v1/product/', views.product_list_view),
    path('api/v1/product/<int:id>', views.product_detail_view),
    path('api/v1/review/', views.review_list_view),
    path('api/v1/review/<int:id>', views.review_detail_view),
    path('api/v1/products/reviews/', views.product_reviews_list_view),
    path('api/v1/users/register/', users_view.register_api_view),
    path('api/v1/users/login/', users_view.login_api_view),
    path('api/v1/users/confirm/', users_view.confirm_user_api_view),

]
