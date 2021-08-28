
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

# Extra Pages
def pages_timeline(request):
    greeting = {}
    greeting['title'] = "Timeline"
    greeting['path'] = "Extra Pages"
    return render(request,'pages/Extra/extrapages/pages-timeline.html',greeting)
def pages_invoice(request):
    greeting = {}
    greeting['title'] = "Invoice"
    greeting['path'] = "Extra Pages"
    return render(request,'pages/Extra/extrapages/pages-invoice.html',greeting)
def pages_directory(request):
    greeting = {}
    greeting['title'] = "Directory"
    greeting['path'] = "Extra Pages"
    return render(request,'pages/Extra/extrapages/pages-directory.html',greeting)
def pages_blank(request):
    greeting = {}
    greeting['title'] = "Starter"
    greeting['path'] = "Extra Pages"
    return render(request,'pages/Extra/extrapages/pages-blank.html',greeting)
def pages_404(request):
    greeting = {}
    greeting['title'] = "Error  404"
    greeting['path'] = "Extra Pages"
    return render(request,'pages/Extra/extrapages/pages-404.html',greeting)
def pages_500(request):
    greeting = {}
    greeting['title'] = "Error 500"
    greeting['path'] = "Extra Pages"
    return render(request,'pages/Extra/extrapages/pages-500.html',greeting)
def pages_pricing(request):
    greeting = {}
    greeting['title'] = "Pricing"
    greeting['path'] = "Extra Pages"
    return render(request,'pages/Extra/extrapages/pages-pricing.html',greeting)
def pages_gallery(request):
    greeting = {}
    greeting['title'] = "Gallery"
    greeting['path'] = "Extra Pages"
    return render(request,'pages/Extra/extrapages/pages-gallery.html',greeting)
def pages_maintenance(request):
    greeting = {}
    greeting['title'] = "Maintenance"
    greeting['path'] = "Extra Pages"
    return render(request,'pages/Extra/extrapages/pages-maintenance.html',greeting)
def pages_coming_soon(request):
    greeting = {}
    greeting['title'] = "Comming Soon"
    greeting['path'] = "Extra Pages"
    return render(request,'pages/Extra/extrapages/pages-coming-soon.html',greeting)

# Email-Templates
def email_templates_alert(request):
    greeting = {}
    greeting['title'] = "Alert Email"
    greeting['path'] = "Email-Templets"
    return render(request,'pages/Extra/email-templates/email-templates-alert.html',greeting)
def email_templates_basic(request):
    greeting = {}
    greeting['title'] = "Basic Action Email"
    greeting['path'] = "Email-Templets"
    return render(request,'pages/Extra/email-templates/email-templates-basic.html',greeting)
def email_templates_billing(request):
    greeting = {}
    greeting['title'] = "Billing  Email"
    greeting['path'] = "Email-Templets"
    return render(request,'pages/Extra/email-templates/email-templates-billing.html',greeting)

