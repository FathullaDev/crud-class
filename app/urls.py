from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from app.views import *

# urlpatterns = [
#     path('index/',index),
#     path("category/<int:pk>/",supplier_views,name="suppliers"),
#     path("suppliers/<int:pk>/",product_views,name="products"),
#
# ]

urlpatterns = [
    # path('', index, name='home'),
    # path('otm/<int:otm_id>/groups/', groups_by_otm, name='groups_by_otm'),
    # path('otm/<int:otm_id>/groups/<int:group_id>/students/', students_by_groups_and_otm, name='students_by_groups_and_otm'),
    # path('student/<int:student_id>/', view_student, name='view_student'),
    #
    # path('add_otm/',add_otm,name="add_otm"),
    # path('add_group/',add_group,name="add_group"),
    # path('add_student/',add_student,name="add_student"),
    #
    # path('update_otm/<int:otm_id>/', update_otm, name='update_otm'),
    # path('update_group/<int:group_id>/', update_group, name='update_group'),
    # path('update_student/<int:student_id>/', update_student, name='update_student'),
    #
    # path('delete_otm/<int:otm_id>/', delete_otm, name="delete_otm"),
    # path('delete_group/<int:group_id>/', delete_group, name="delete_group"),
    # path('delete_student/<int:student_id>/', delete_student, name="delete_student"),


    path('', OtmListView.as_view(), name='home'),
    path('otm/<int:otm_id>/groups/', GroupsByOtmView.as_view(), name='groups_by_otm'),
    path('otm/<int:otm_id>/groups/<int:group_id>/students/',StudentsByGroupAndOtmView.as_view(), name='students_by_groups_and_otm'),
    path('student/<int:student_id>/', StudentDetailView.as_view(), name='view_student'),

    # add
    path('add_otm/', AddOtmView.as_view(), name='add_otm'),
    path('add_group/', AddGroupView.as_view(), name='add_group'),
    path('add_student/', AddStudentView.as_view(), name='add_student'),

    # update
    path('update_otm/<int:otm_id>/', UpdateOtmView.as_view(), name='update_otm'),
    path('update_group/<int:group_id>/', UpdateGroupView.as_view(), name='update_group'),
    path('update_student/<int:student_id>/', UpdateStudentView.as_view(), name='update_student'),

    # delete
    path('delete_otm/<int:otm_id>/', DeleteOtmView.as_view(), name='delete_otm'),
    path('delete_group/<int:group_id>/', DeleteGroupView.as_view(), name='delete_group'),
    path('delete_student/<int:student_id>/', DeleteStudentView.as_view(), name='delete_student'),

]