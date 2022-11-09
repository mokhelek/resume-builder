from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('',views.landing_page , name = "landing_page"),
	path('profile/', views.index , name = 'index'),
    path("pdf_view/<int:profile_id>/",views.render_pdf_view , name = "pdf_view" ),
    
]


#path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
   # path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),