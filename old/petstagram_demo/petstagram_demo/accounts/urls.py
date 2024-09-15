from django.urls import path, include

from petstagram_demo.accounts.views import (signup_user, signin_user, signout_user,
                                            details_profile, edit_profile, delete_user)

urlpatterns = (
    path('signup/', signup_user, name='signup user'),
    path('signin/', signin_user, name='signin user'),
    path('signout/', signout_user, name='sign out'),
    path('profile/<int:pk>/', include([
        path('', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_user, name='delete profile'),
    ])),
)