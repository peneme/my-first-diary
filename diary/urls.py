from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),#/diary/
    path('add/', views.AddView.as_view(), name='add'),#/diary/add/ ⇨admin:diary_day_addで管理者のみ
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),#'admin:diary_day_change'
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),#'admin:diary_day_delete' 
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
]

"""
urlpatterns = [
    path('', views.index, name='index'),#/diary/
    path('add/', views.add, name='add'),#/diary/add/
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('detail/<int:pk>', views.detail, name='detail'),
]
"""