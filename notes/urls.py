from .views import note_list_view, finished_item, delete_item, recover_item
from django.urls import path

urlpatterns = [
    path('',note_list_view, name = 'note-list' ),
    path('finish-item/<id>/',finished_item, name = 'finish-note-item'),
    path('delelte-item/<id>/',delete_item, name = 'delete-note-item'),
    path('recover-item/<id>/',recover_item, name = 'recover-note-item'),
    

]