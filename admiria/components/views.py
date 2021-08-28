from django.shortcuts import render



# UI Elements
def buttons(request):
    greeting = {}
    greeting['title'] = "Buttons"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-buttons.html',greeting)
def colors(request):
    greeting = {}
    greeting['title'] = "Colors"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-colors.html',greeting)
def cards(request):
    greeting = {}
    greeting['title'] = "Cards"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-cards.html',greeting)
def tabs_accordions(request):
    greeting = {}
    greeting['title'] = "Tabs & Accordions"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-tabs-accordions.html',greeting)
def modals(request):
    greeting = {}
    greeting['title'] = "Modals"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-modals.html',greeting)
def images(request):
    greeting = {}
    greeting['title'] = "Images"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-images.html',greeting)
def alerts(request):
    greeting = {}
    greeting['title'] = "Alerts"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-alerts.html',greeting)
def progressbars(request):
    greeting = {}
    greeting['title'] = "Progress Bars"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-progressbars.html',greeting)
def dropdowns(request):
    greeting = {}
    greeting['title'] = "Dropdowns"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-dropdowns.html',greeting)
def lightbox(request):
    greeting = {}
    greeting['title'] = "Lightbox"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-lightbox.html',greeting)
def navs(request):
    greeting = {}
    greeting['title'] = "Navs"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-navs.html',greeting)
def pagination(request):
    greeting = {}
    greeting['title'] = "Pagination"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-pagination.html',greeting)
def popover_tooltips(request):
    greeting = {}
    greeting['title'] = "Popover & Tooltips"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-popover-tooltips.html',greeting)
def badge(request):
    greeting = {}
    greeting['title'] = "Badge"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-badge.html',greeting)
def carousel(request):
    greeting = {}
    greeting['title'] = "Carousel"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-carousel.html',greeting)
def video(request):
    greeting = {}
    greeting['title'] = "Video"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-video.html',greeting)
def typography(request):
    greeting = {}
    greeting['title'] = "Typography"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-typography.html',greeting)
def sweet_alert(request):
    greeting = {}
    greeting['title'] = "Sweet-Alert"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-sweet-alert.html',greeting)
def grid(request):
    greeting = {}
    greeting['title'] = "Grid system"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-grid.html',greeting)
def animation(request):
    greeting = {}
    greeting['title'] = "Animation"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-animation.html',greeting)
def highlight(request):
    greeting = {}
    greeting['title'] = "Highlight"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-highlight.html',greeting)
def rating(request):
    greeting = {}
    greeting['title'] = "Rating"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-rating.html',greeting)
def nestable(request):
    greeting = {}
    greeting['title'] = "Nestable List"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-nestable.html',greeting)
def alertify(request):
    greeting = {}
    greeting['title'] = "Alertify"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-alertify.html',greeting)
def rangeslider(request):
    greeting = {}
    greeting['title'] = "Range Slider"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-rangeslider.html',greeting)
def sessiontimeout(request):
    greeting = {}
    greeting['title'] = "Session Timeout"
    greeting['path'] = "UI Elements"
    return render(request,'pages/Components/ui/ui-sessiontimeout.html',greeting)
# Form-Elements

def form_elemet(request):
    greeting = {}
    greeting['title'] = " Form Elements"
    greeting['path'] = "Form Elements"
    return render(request,'pages/Components/formelement/form-elements.html',greeting)
def form_validation(request):
    greeting = {}
    greeting['title'] = " Form Validation"
    greeting['path'] = "Form Elements"
    return render(request,'pages/Components/formelement/form-validation.html',greeting)
def form_advanced(request):
    greeting = {}
    greeting['title'] = "Form Advanced"
    greeting['path'] = "Form Elements"
    return render(request,'pages/Components/formelement/form-advanced.html',greeting)
def form_wizard(request):
    greeting = {}
    greeting['title'] = "Form Wizard"
    greeting['path'] = "Form Elements"
    return render(request,'pages/Components/formelement/form-wizard.html',greeting)
def form_editors(request):
    greeting = {}
    greeting['title'] = "Form Editors"
    greeting['path'] = "Form Elements"
    return render(request,'pages/Components/formelement/form-editors.html',greeting)
def form_uploads(request):
    greeting = {}
    greeting['title'] = "File Uploads"
    greeting['path'] = "Form Elements"
    return render(request,'pages/Components/formelement/form-uploads.html',greeting)
def form_mask(request):
    greeting = {}
    greeting['title'] = "Form Mask"
    greeting['path'] = "Form Elements"
    return render(request,'pages/Components/formelement/form-mask.html',greeting)
def form_xeditable(request):
    greeting = {}
    greeting['title'] = "Form Xeditable"
    greeting['path'] = "Form Elements"
    return render(request,'pages/Components/formelement/form-xeditable.html',greeting)

# Charts

def charts_morris(request):
    greeting = {}
    greeting['title'] = "Morris Charts"
    greeting['path'] = "Charts"
    return render(request,'pages/Components/charts/charts-morris.html',greeting)
def charts_chartist(request):
    greeting = {}
    greeting['title'] = "Chartist Charts"
    greeting['path'] = "Charts"
    return render(request,'pages/Components/charts/charts-chartist.html',greeting)
def charts_chartjs(request):
    greeting = {}
    greeting['title'] = "Chartjs Charts"
    greeting['path'] = "Charts"
    return render(request,'pages/Components/charts/charts-chartjs.html',greeting)
def charts_flot(request):
    greeting = {}
    greeting['title'] = "Flot Charts"
    greeting['path'] = "Charts"
    return render(request,'pages/Components/charts/charts-flot.html',greeting)
def charts_c3(request):
    greeting = {}
    greeting['title'] = "C3 Charts"
    greeting['path'] = "Charts"
    return render(request,'pages/Components/charts/charts-c3.html',greeting)
def charts_sparkline(request):
    greeting = {}
    greeting['title'] = "Sparkline Charts"
    greeting['path'] = "Charts"
    return render(request,'pages/Components/charts/charts-sparkline.html',greeting)
def charts_other(request):
    greeting = {}
    greeting['title'] = "Jquery Knob Charts"
    greeting['path'] = "Charts"
    return render(request,'pages/Components/charts/charts-other.html',greeting)
def charts_peity(request):
    greeting = {}
    greeting['title'] = "Peity Charts"
    greeting['path'] = "Charts"
    return render(request,'pages/Components/charts/charts-peity.html',greeting)

#Table

def tables_basic(request):
    greeting = {}
    greeting['title'] = "Basic Tables"
    greeting['path'] = "Tables"
    return render(request,'pages/Components/Table/tables-basic.html',greeting)
def tables_datatable(request):
    greeting = {}
    greeting['title'] = "Data Tables"
    greeting['path'] = "Tables"
    return render(request,'pages/Components/Table/tables-datatable.html',greeting)
def tables_editable(request):
    greeting = {}
    greeting['title'] = "Editable Table"
    greeting['path'] = "Tables"
    return render(request,'pages/Components/Table/tables-editable.html',greeting)
def tables_responsive(request):
    greeting = {}
    greeting['title'] = "Responsive Table"
    greeting['path'] = "Tables"
    return render(request,'pages/Components/Table/tables-responsive.html',greeting)


# Icons

def icons_material(request):
    greeting = {}
    greeting['title'] = "Material Design Icons"
    greeting['path'] = "Icons"
    return render(request,'pages/Components/iconfile/icons-material.html',greeting)
def icons_ion(request):
    greeting = {}
    greeting['title'] = "Ion Icons"
    greeting['path'] = "Icons"
    return render(request,'pages/Components/iconfile/icons-ion.html',greeting)
def icons_fontawesome(request):
    greeting = {}
    greeting['title'] = "Font Awesome Icons"
    greeting['path'] = "Icons"
    return render(request,'pages/Components/iconfile/icons-fontawesome.html',greeting)
def icons_themify(request):
    greeting = {}
    greeting['title'] = "Themify Icons"
    greeting['path'] = "Icons"
    return render(request,'pages/Components/iconfile/icons-themify.html',greeting)
def icons_dripicons(request):
    greeting = {}
    greeting['title'] = "Dripicons Icons"
    greeting['path'] = "Icons"
    return render(request,'pages/Components/iconfile/icons-dripicons.html',greeting)
def icons_typicons(request):
    greeting = {}
    greeting['title'] = "Typicon Icons"
    greeting['path'] = "Icons"
    return render(request,'pages/Components/iconfile/icons-typicons.html',greeting)
def icons_weather(request):
    greeting = {}
    greeting['title'] = "Weather Icons"
    greeting['path'] = "Icons"
    return render(request,'pages/Components/iconfile/icons-weather.html',greeting)
def icons_mobirise(request):
    greeting = {}
    greeting['title'] = "Mobirise Icons"
    greeting['path'] = "Icons"
    return render(request,'pages/Components/iconfile/icons-mobirise.html',greeting)

#  Map

def maps_google(request):
    greeting = {}
    greeting['title'] = "Google Map"
    greeting['path'] = "Maps"
    return render(request,'pages/Components/map/maps-google.html',greeting)
def maps_vector(request):
    greeting = {}
    greeting['title'] = "Vector Map"
    greeting['path'] = "Maps"
    return render(request,'pages/Components/map/maps-vector.html',greeting)