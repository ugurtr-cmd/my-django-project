from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from blog.models import yazi,category,SiteContent
from django.contrib.auth import authenticate,logout,update_session_auth_hash, login as login_auth
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect


def home(request):
    son_yazilar = yazi.objects.filter(isActive=True).order_by('-id')[:3]  # en son 3 aktif yazı
    yazilar = yazi.objects.all()
    anasayfa_alt_metin = SiteContent.objects.filter(slug='anasayfa-alt-metin').first()

    number = len(yazilar)
    sozler = [
    "Gönül ne kahve ister ne kahvehane, gönül sohbet ister kahve bahane.",
    "Kendini bilen, Rabbini bilir.",
    "Ne olursan ol yine gel.",
    "Her şey üstüne gelip seni dayanamayacağın bir noktaya getirdiğinde, sakın vazgeçme.",
    "Kalp deniz, dil kıyıdır. Denizde ne varsa kıyıya o vurur.",
    "Susmak, bazen en güçlü çığlıktır.",
    "Unutma, karanlık olmasaydı yıldızları göremezdik.",
    "Yürümeye devam eden yol alır, düşse bile kalkar.",
    "Küçük adımlar büyük yollar açar.",
    "Dünya seni yıkmadan önce sen kendini inşa et.",
    "Bazen kaybetmek, en büyük kazançtır.",
    "Gerçek güç, vazgeçmemekte saklıdır.",
    "Her gün yeni bir başlangıçtır.",
    "Karanlıktan korkma, yıldızlar orada doğar.",
    "Zihin neye inanırsa beden ona ulaşır.",
    "Bir şey değişir, her şey değişir.",
    "Düşüncelerini değiştir, hayatın değişsin.",
    "Engeller, seni durdurmak için değil, yön vermek için vardır.",
    "Başarı, tekrar tekrar denemekten geçer.",
    "Hayat seni yıkarsa, yeniden inşa et.",
    "Cesaret, korkmamak değil; korkuya rağmen yürümektir.",
    "Bugünün acısı, yarının gücüdür.",
    "Asıl savaş, insanın kendi içindedir.",
    "Kendine inandığın gün, dünya da sana inanır.",
    "Bir umut yeter, karanlığı aydınlatmaya.",
    "Hayallerini küçümseyenlerden uzak dur.",
    "Her sabah yeni bir mucizedir.",
    "Diken olmadan gül olmaz.",
    "İmkânsız, sadece daha fazla çaba gerektirir.",
    "Bazen yavaş gitmek, doğru gitmektir.",
    "Yalnızlık, bazen en iyi öğretmendir.",
    "Zor zamanlar, güçlü insanlar yaratır.",
    "Hiçbir rüzgar, yönünü bilmeyene yardım edemez.",
    "Hayat, cesur olanları ödüllendirir.",
    "Bir gün değil, her gün başla.",
    "Yüzleşmeden geçmeyen sınav, öğrenilmez.",
    "Yol senin, yürümek de.",
    "Umutsuzluk yok, sadece dinlenme molası var.",
    "Yenilmek değil, vazgeçmek kaybettirir.",
    "Kelimeler köprü kurar, sessizlik duvar.",
    "Kendinle barış, her şeyle barış getirir.",
    "Başarı, konfor alanının dışında başlar.",
    "Bir ışık ol, karanlıkta kalanlara yol göster.",
    "Kalbinin götürdüğü yere git.",
    "Beklemek değil, harekete geçmek değiştirir.",
    "Hayat kısa, hayalin peşinden git.",
    "Kırıldığın yerden güçlenirsin.",
    "Her şeyin başı niyet.",
    "Gözlerinle değil, kalbinle gör.",
    "İçindeki sesi dinle, o hiç yalan söylemez.",
    "Başlamak için mükemmel olmak zorunda değilsin.",
    "Hayal etmek başarmanın yarısıdır.",
    "Başarı, tekrar tekrar denemekten vazgeçmemektir.",
    "Yol ne kadar zor olursa olsun, vazgeçmek çözüm değildir.",
    "Bir adım at, yol seni takip edecektir.",
    "Zirveye giden yol, cesaretle başlar.",
    "Yapabileceğine inan, zaten yarısını başarmışsındır.",
    "Küçük adımlar, büyük zaferlerin başlangıcıdır.",
    "Bugün attığın adım, yarının başarısını belirler.",
    "Yorulmak, pes etmek için değil; dinlenip devam etmek içindir.",
    "Engeller, kararlılıkla aşılmak içindir.",
    "Bir fikrin varsa, bir yolun da vardır.",
    "İmkânsız, sadece daha fazla çaba gerektirir.",
    "Karanlık günler geçer, ışığı bekle.",
    "Gerçek güç, pes etmediğin an ortaya çıkar.",
    "Başarı, cesur olanların ödülüdür.",
    "Denemediğin sürece kaybetmiş sayılmazsın.",
    "Her gün yeni bir başlangıçtır.",
    "Hayat, cesur olanları ödüllendirir.",
    "Risk almadan kazanç olmaz.",
    "Zorluklar, seni güçlü kılmak için vardır.",
    "Kendine inan, çünkü başka kimse senin yerine yaşayamaz.",
    "Ne kadar yavaş ilerlediğin önemli değil, durmadığın sürece başarırsın.",
    "Her şey seninle başlar.",
    "Hayat bir aynadır, gülümsersen gülümser.",
    "Değişim, seninle başlar.",
    "En karanlık an, şafağa en yakın andır.",
    "Hayat bir mücadeledir, sen de bir savaşçısın.",
    "Düşersen kalk, çünkü ilerlemek için yürümek gerekir.",
    "Her kayıp bir ders, her ders bir adımdır.",
    "Kazanmak istemek yetmez, harekete geçmek gerekir.",
    "Bugün yapamadığın şey, yarının hedefi olsun.",
    "Kendini küçümseme, içinde evrenler var.",
    "İnandığın yolda yürü, sonunda ödül seni bulur.",
    "Özgüven, en güçlü silahtır.",
    "Unutma, en büyük başarılar en derin yaralardan doğar.",
    "Umut, en karanlık anların ilacıdır.",
    "Başarının sırrı, disiplin ve sabırdır.",
    "Bir amacı olan insanın gücüne sınır koyulamaz.",
    "Sen değişirsen dünya değişir.",
    "Küçük başarıları kutla, büyük hedeflere hazırlan.",
    "Hiçbir şey yapmamaktan iyidir denemek.",
    "Kendini geliştir, çünkü zaman seni beklemez.",
    "İnançsız bir adım bile ilerleme getirir.",
    "Kimi zaman düşmek, doğru yolu bulmak için gereklidir.",
    "Her gün bir önceki seninle yarış.",
    "Hayatta kalmak değil, yaşamak hedefin olsun.",
    "Gerçek başarı, iç huzurla gelir.",
    "Sen yeter ki başla, gerisi gelir.",
    "Zihnin sınır tanımaz, yeter ki onu serbest bırak.",
    "Bugün bir şey yap, yarın teşekkür edeceksin."
    "Kim demiş gül yaşar dikenin himayesinde? Dikenin itibarı ancak gül sayesinde",
    "Sessizlik cevapları verir",
    "İnsan kalbiyle insandır, kalpsiz beden cesettir.",
    "Susmak bazen en gür sestir."
    ]
    rastgele_soz = random.choice(sozler)
    return render(request, 'index.html', {
        'son_yazilar': son_yazilar,
        'rastgele_soz': rastgele_soz,
        'anasayfa_alt_metin': anasayfa_alt_metin,
        'number':number
    })
def about(request):
    hakkimda = SiteContent.objects.filter(slug='hakkimda').first()
    return render(request,'hakkimda.html', {
        "hakkimda":hakkimda,
    })

# def details(request,titlem):
#     yazilar = yazi.objects.get()

#     return render(request,'details.html', context={
#         'yazilar':titlem
#     })

def iletisim(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # E-posta içeriğini daha düzenli hale getirme
        subject = f"SEYMAA.COM -  Yeni İletişim Formu: {name}"
        email_message = f"""
        Ad Soyad: {name}
        E-posta: {email}
        
        Mesaj:
        {message}
        
        Bu mesaj {settings.SITE_NAME} iletişim formundan gönderilmiştir.
        """
        
        try:
            # Mail gönderiminden önce bilgileri kontrol et
            
            send_mail(
                subject=subject,
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            messages.success(request, 'Mesajınız başarıyla gönderildi! En kısa sürede sizinle iletişime geçeceğim.')
            return redirect('iletisim')
            
        except Exception as e:
            error_msg = f"Mail gönderilemedi. Hata: {str(e)}"
            print(error_msg)  # Konsola hata detayını yaz
            messages.error(request, 'Mesajınız gönderilirken bir hata oluştu. Lütfen daha sonra tekrar deneyin.')
    
    return render(request, 'iletisim.html')

# def slayt(request):
#     return render(request, 'slayt.html')


# def depolama(request):
#     return render(request, 'depolama.html')
@login_required(login_url='login')
def admin_yazi_listesi(request):
    yazilar = yazi.objects.all()
    return render(request, 'list.html', {'yazilar': yazilar})

@login_required(login_url='login')
def yazi_guncelle(request, id):
    yazim = get_object_or_404(yazi, id=id)

    if request.method == 'POST':
        yazim.title = request.POST.get('baslik')
        yazim.description = request.POST.get('description')
        yazim.isActive = request.POST.get('aktif')
        
        # Resim güncelleme
        if 'image' in request.FILES:
            yazim.imageUrl = request.FILES['image']
            
        yazim.save()
        return redirect('admin-yazi-listesi')

    return render(request, 'list_duzenle.html', {'yazi': yazim})

@login_required(login_url='login')
def admin_yazi_sil(request, id):
    yazi_obj = get_object_or_404(yazi, id=id)
    if request.method == 'POST':
        yazi_obj.delete()
        return redirect('admin-yazi-listesi')
    return render(request, 'yazi_sil_onay.html', {'yazi': yazi_obj})

@login_required(login_url='login')
def adminpanel(request):
    kategoriler = category.objects.all()
    msg = ""
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        imageUrl = request.FILES.get('image')
        isActive = request.POST.get("isActive",False)

        isActive = True if isActive == "on" else False

        if title == "":
            msg+="Şeyma başlık girmek zorunlu"
            return render(request, 'admin.html',{
                    'error':True,
                    'msg':msg,
                    'kategoriler':kategoriler,}
                  )
        elif len(title) < 5 :
            msg+="Şeyma sence de başlık çok kısa değil mi?"
            return render(request, 'admin.html',{
                    'error':True,
                    'msg':msg,
                    'kategoriler':kategoriler,}
                  )
        elif description == "":
            msg+="Sence yazı içeriği olmadan paylaşım olur mu Şeyma?"
            return render(request, 'admin.html',{
                    'error':True,
                    'msg':msg,
                    'kategoriler':kategoriler,}
                  )
        elif len(description)<50:
            msg+="Şeyma yazı çok mu kısa oldu ne"
            return render(request, 'admin.html',{
                    'error':True,
                    'msg':msg,
                    'kategoriler':kategoriler,}
                  )

        yazilar = yazi(title = title, description = description, imageUrl = imageUrl, isActive = isActive)
        yazilar.save()
        
        return redirect('/blog')
        
    return render(request, 'admin.html',{
                  'kategoriler':kategoriler,}
                  )

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login_auth(request, user)
            messages.add_message(request,messages.SUCCESS,"Giriş Başarılı")
            return redirect('home')
        else:
            messages.add_message(request,messages.WARNING,"Kullanıcı ismi veya parola hatalı")
            return render(request, 'giris.html')
    return render(request, 'giris.html')

@login_required(login_url='login')
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request, "Parola başarıyla güncellendi.")
            return redirect("parola_guncelle")
        else:
            return render(request,"parola_guncelle.html", {'form': form})

    return render(request,'parola_guncelle.html')

def user_logout(request):
    messages.add_message(request,messages.SUCCESS,"Çıkış Yapıldı")
    logout(request)
    return render(request,'index.html')


from mainproject.models import Ogrenci, EzberKaydi

@login_required(login_url='login')
def ogrenci_duzenle(request, id):
    ogrenci = get_object_or_404(Ogrenci, id=id)
    
    if request.method == 'POST':
        # Güncelleme işlemleri
        ogrenci.ad_soyad = request.POST.get('ad_soyad')
        ogrenci.seviye = request.POST.get('seviye')
        ogrenci.mevcut_cuz = request.POST.get('mevcut_cuz')
        ogrenci.hedef_cuz = request.POST.get('hedef_cuz')
        ogrenci.puan = request.POST.get('puan')
        ogrenci.ozel_notlar = request.POST.get('ozel_notlar')
        
        # Profil fotoğrafı güncelleme
        if 'profil_foto' in request.FILES:
            ogrenci.profil_foto = request.FILES['profil_foto']
        
        ogrenci.save()
        messages.success(request, 'Öğrenci bilgileri güncellendi')
        return redirect('ogrenci_detay', id=ogrenci.id)
    
    seviyeler = Ogrenci.SEVIYE_CHOICES
    return render(request, 'ogrenci_duzenle.html', {
        'ogrenci': ogrenci,
        'seviyeler': seviyeler
    })

@login_required(login_url='login')
def ogrenci_detay(request, id):
    ogrenci = get_object_or_404(Ogrenci, id=id)
    kayitlar = EzberKaydi.objects.filter(ogrenci=ogrenci).order_by('-tarih')
    
    # Tahmini bitiş süresi
    kalan_cuz = ogrenci.hedef_cuz - ogrenci.mevcut_cuz
    tahmini_gun = None
    if kayitlar and kalan_cuz > 0:
        ortalama_ilerleme = sum(k.ilerleme() for k in kayitlar) / len(kayitlar)
        if ortalama_ilerleme > 0:
            tahmini_gun = (kalan_cuz * 20) / ortalama_ilerleme  # Her cüz ~20 sayfa
    
    return render(request, 'ogrenci_detay.html', {
        'ogrenci': ogrenci,
        'kayitlar': kayitlar,
        'tahmini_gun': tahmini_gun
    })


@login_required
def ogrenci_listesi(request):
    # Tüm öğrencileri al, kayıt tarihine göre ters sırala (en yeni en üstte)
    tum_ogrenciler = Ogrenci.objects.all().order_by('-kayit_tarihi')
    
    # Arama fonksiyonelliği
    arama_terimi = request.GET.get('q')
    if arama_terimi:
        tum_ogrenciler = tum_ogrenciler.filter(ad_soyad__contains=arama_terimi)
    
    # Sayfalama
    sayfa = request.GET.get('sayfa', 1)
    paginator = Paginator(tum_ogrenciler, 10)  # Sayfa başına 10 öğrenci
    
    try:
        ogrenciler = paginator.page(sayfa)
    except PageNotAnInteger:
        ogrenciler = paginator.page(1)
    except EmptyPage:
        ogrenciler = paginator.page(paginator.num_pages)
    
    # Seviye seçeneklerini al
    seviyeler = Ogrenci.SEVIYE_CHOICES
    
    return render(request, 'ogrenci_listesi.html', {
        'ogrenciler': ogrenciler,
        'seviyeler': seviyeler,
        'arama_terimi': arama_terimi
    })

@login_required(login_url='login')
def ogrenci_not_ekle(request,id):
    ogrenci = get_object_or_404(Ogrenci, id=id)
    if request.method == 'POST':
        ogrenci.ozel_notlar = request.POST.get('ozel_not', '')
        ogrenci.save()
        messages.success(request, 'Notlar başarıyla kaydedildi')
    return redirect('ogrenci_detay', id=ogrenci.id)

@login_required(login_url='login')
def ogrenci_ekle(request):
    if request.method == 'POST':
        # Formdan gelen verileri al
        ad_soyad = request.POST.get('ad_soyad')
        ad_soyad = ad_soyad.title()
        seviye = request.POST.get('seviye')
        mevcut_cuz = request.POST.get('mevcut_cuz', 1)
        hedef_cuz = request.POST.get('hedef_cuz', 30)
        puan = request.POST.get('puan', 5)
        ozel_notlar = request.POST.get('ozel_notlar', '')
        # Yeni öğrenci oluştur
        yeni_ogrenci = Ogrenci(
            ad_soyad=ad_soyad,
            seviye=seviye,
            mevcut_cuz=mevcut_cuz,
            hedef_cuz=hedef_cuz,
            puan=puan,
            ozel_notlar=ozel_notlar
        )
        
        # Profil fotoğrafı varsa ekle
        if 'profil_foto' in request.FILES:
            yeni_ogrenci.profil_foto = request.FILES['profil_foto']
        
        yeni_ogrenci.save()
        messages.success(request, 'Öğrenci başarıyla eklendi')
        return redirect('ogrenci_listesi')
    
    # GET isteği ise formu göster
    seviyeler = Ogrenci.SEVIYE_CHOICES
    return render(request, 'yeni_ogrenci.html', {'seviyeler': seviyeler})

@login_required
def ogrenci_sil(request, ogrenci_id):
    ogrenci = get_object_or_404(Ogrenci, id=ogrenci_id)
    
    if request.method == 'POST':
        ogrenci.delete()
        messages.success(request, f'{ogrenci.ad_soyad} başarıyla silindi')
        return redirect('ogrenci_listesi')
    
    return render(request, 'ogrenci_sil_onay.html', {'ogrenci': ogrenci})