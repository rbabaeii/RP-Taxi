from django.urls import path , include
from  . import views
from rest_framework import routers
from dj_rest_auth.urls import PasswordResetConfirmView
# import dj_rest_auth.registration.urls
# router = routers.SimpleRouter()
# router.register('account/' , views.Balanceapiview)
urlpatterns = [
    path('list/' , views.UserList.as_view() , name='userlist'),
    path('<int:pk>/', views.UserDetail.as_view() , name='userdetail'),
    path('edit-profile/<int:pk>/' , views.EditProfile.as_view() , name = 'edit-profile'),
    path('auth/', include('rest_framework.urls')),
    path('account/auth/' , include('dj_rest_auth.urls')),
    path('account/auth/registration/' , include('dj_rest_auth.registration.urls')),
    path('api/rest-auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('test/<int:pk>/' , views.PayTravel.as_view()),
    path('add/<int:pk>/' , views.AddBalanceapiview.as_view())
]
