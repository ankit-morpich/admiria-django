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

     # Extra-Pages
    path('Extra-pages/pages-timeline', views.pages_timeline, name="pages-timeline"),
    path('Extra-pages/pages-invoice', views.pages_invoice, name="pages-invoice"),
    path('Extra-pages/pages-directory', views.pages_directory, name="pages-directory"),
    path('Extra-pages/pages-blank', views.pages_blank, name="pages-blank"),
    path('Extra-pages/pages-404', views.pages_404, name="pages-404"),
    path('Extra-pages/pages-500', views.pages_500, name="pages-500"),
    path('Extra-pages/pages-pricing', views.pages_pricing, name="pages-pricing"),
    path('Extra-pages/pages-gallery', views.pages_gallery, name="pages-gallery"),
    path('Extra-pages/pages-maintenance', views.pages_maintenance, name="pages-maintenance"),
    path('Extra-pages/pages-coming_soon', views.pages_coming_soon, name="pages-coming-soon"),
    
      # Ecommerce-Pages
    path('Email-Templets/email-templates-alert', views.email_templates_alert, name="email-templates-alert"),
    path('Email-Templets/email-templates-basic', views.email_templates_basic, name="email-templates-basic"),
    path('Email-Templets/email-templates-billing', views.email_templates_billing, name="email-templates-billing"),

]
