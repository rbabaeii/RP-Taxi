from django.urls import path , include
from  . import views
from dj_rest_auth.urls import PasswordResetConfirmView
import dj_rest_auth.registration.urls

urlpatterns = [
    path('list/' , views.UserList.as_view() , name='userlist'),
    path('<int:pk>/', views.UserDetail.as_view() , name='userdetail'),
    path('auth/', include('rest_framework.urls')),
    path('account/auth/' , include('dj_rest_auth.urls')),
    path('account/auth/registration/' , include('dj_rest_auth.registration.urls')),
    path('api/rest-auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]