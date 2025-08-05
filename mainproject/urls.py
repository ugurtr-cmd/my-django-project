from django.urls import path
from django.http import HttpResponse
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('index', views.home, name="home"),
    path('hakkimda', views.about, name="hakkimda"),
    path('iletisim', views.iletisim ,name="iletisim"),
    path('admin-paneli', views.adminpanel, name="admin-paneli"),
    path('admin-paneli/yazilar/', views.admin_yazi_listesi, name='admin-yazi-listesi'),
    path('admin-paneli/yazilar/<int:id>', views.yazi_guncelle, name='yazi-guncelle'),
    path('admin-paneli/yazilar/sil/<int:id>/', views.admin_yazi_sil, name='yazi-sil'),
    path('admin-paneli/ogrenciler/', views.ogrenci_listesi, name='ogrenci_listesi'),
    path('admin-paneli/ogrenci/ekle/', views.ogrenci_ekle, name='yeni_ogrenci'),
    path('admin-paneli/ogrenci/duzenle/<int:id>/', views.ogrenci_duzenle, name='ogrenci_duzenle'),
    path('admin-paneli/ogrenci/<int:id>/not/', views.ogrenci_not_ekle, name='ogrenci_not_ekle'),
    path('ogrenci/sil/<int:ogrenci_id>/', views.ogrenci_sil, name='ogrenci_sil'),
    path('admin-paneli/ogrenci/detay/<int:id>/', views.ogrenci_detay, name='ogrenci_detay'),
    path('giris', views.login,name="login"),
    path('admin-paneli/parola_guncelle', views.change_password,name="parola_guncelle"),

    path('cikis', views.user_logout, name="cikis"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
