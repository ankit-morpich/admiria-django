from django.urls import path, include
from . import views

urlpatterns = [

    # Extra-Layout-Vertical
    path('Layouts/Vertical/layouts-light-sidebar', views.layouts_light_sidebar, name="layouts-light-sidebar"),
    path('Layouts/Vertical/layouts-compact-sidebar', views.layouts_compact_sidebar, name="layouts-compact-sidebar"),
    path('Layouts/Vertical/layouts-icon-slidebar', views.layouts_icon_sidebar, name="layouts-icon-sidebar"),
    path('Layouts/Vertical/layouts-boxed', views.layouts_boxed, name="layouts-boxed"),
    path('Layouts/Vertical/layouts-colored-sidebar', views.layouts_colored_sidebar, name="layouts-colored-sidebar"),
     # Extra-Layout-Horizontal
    path('Layouts/Horizontal/layouts-hori-boxed', views.layouts_hori_boxed, name="layouts-hori-boxed"),
    path('Layouts/Horizontal/layouts-hori-topbar-light', views.layouts_hori_topbar_light, name="layouts-hori-topbar-light"),
    path('Layouts/Horizontal/layouts-horizontal', views.layouts_horizontal, name="layouts-horizontal"),

     
]
