
from django.shortcuts import render

# Vertical

def layouts_light_sidebar(request):
    greeting = {}
    greeting['title'] = "Light Sidebar"
    greeting['path'] = "Layouts"
    return render(request,'pages/Extra/Layout/vertical/layouts-light-sidebar.html',greeting)
def layouts_compact_sidebar(request):
    greeting = {}
    greeting['title'] = "Compact Sidebar"
    greeting['path'] = "Layouts"
    return render(request,'pages/Extra/Layout/vertical/layouts-compact-sidebar.html',greeting)
def layouts_icon_sidebar(request):
    greeting = {}
    greeting['title'] = "Icon Sidebar"
    greeting['path'] = "Layouts"
    return render(request,'pages/Extra/Layout/vertical/layouts-icon-sidebar.html',greeting)
def layouts_boxed(request):
    greeting = {}
    greeting['title'] = "Boxed Layout"
    greeting['path'] = "Layouts"
    return render(request,'pages/Extra/Layout/vertical/layouts-boxed.html',greeting)
def layouts_colored_sidebar(request):
    greeting = {}
    greeting['title'] = "Colored Sidebar"
    greeting['path'] = "Layouts"
    return render(request,'pages/Extra/Layout/vertical/layouts-colored-sidebar.html',greeting)

# Horizontal
def layouts_hori_boxed(request):
    greeting = {}
    greeting['title'] = "Horizontal Boxed Layout"
    greeting['path'] = "Layouts"
    return render(request,'pages/Extra/Layout/horizontal/layouts-hori-boxed.html',greeting)
def layouts_hori_topbar_light(request):
    greeting = {}
    greeting['title'] = "Horizontal Light Topbar"
    greeting['path'] = "Layouts"
    return render(request,'pages/Extra/Layout/horizontal/layouts-hori-topbar-light.html',greeting)
def layouts_horizontal(request):
    greeting = {}
    greeting['title'] = "Horizontal Layout"
    greeting['path'] = "Layouts"
    return render(request,'pages/Extra/Layout/horizontal/layouts-horizontal.html',greeting)
