from django.urls import path

from dj07_forms_basics.web.views import index, type_of_forms, model_form, index_model, update_employee

urlpatterns = (
    path('', index, name='index'),
    path('types-of-forms/', type_of_forms, name='types'),
    path('model-form/', model_form, name='model_form'),
    path('modelform-class/', index_model, name='index-models'),
    path('modelform-class/<int:pk>/', update_employee, name='update-employee')
)