# PDF Ayıklayıcı 2

PDF Ayıklayıcı 2, Windows Explorer'da bir PDF dosyasına sağ tıklayıp **PDF AYIKLA** seçeneğini kullanarak PDF'nin her sayfasını ayrı PDF dosyalarına çıkaran taşınabilir bir Windows aracıdır.

Bu depo, uygulamanın final USB paketini (`PDF_Ayikla_USB`) ve kaynak/derleme dosyalarını (`PDF_Ayikla_USB_BUILD`) içerir.

## Özellikler

- Windows Explorer sağ-tık menüsü entegrasyonu
- Her PDF sayfasını ayrı PDF olarak oluşturma
- Sıralı çıktı isimleri: `belge_001.pdf`, `belge_002.pdf`, ...
- PDF sayfalarını görüntüye dönüştürmeden doğrudan aktarma
- Python, pip, PyMuPDF veya internet gerektirmeden çalışan taşınabilir EXE
- USB bellekten çalışacak biçimde göreli yol kullanan kurulum betikleri

## Kullanım

1. `PDF_Ayikla_USB` klasörünü USB belleğe veya bilgisayarınıza kopyalayın.
2. `Kur.bat` dosyasını çift tıklayın.
3. Bir PDF dosyasına sağ tıklayın ve **PDF AYIKLA** seçeneğini seçin.
4. Sayfalar kaynak PDF ile aynı klasöre `dosya_001.pdf`, `dosya_002.pdf` biçiminde yazılır.

Windows 11'de komut ilk sağ-tık menüsünde görünmüyorsa **Diğer seçenekleri göster** menüsüne bakın.

## Kaldırma

Sağ-tık menüsü kaydını kaldırmak için `PDF_Ayikla_USB/Kaldir.bat` dosyasını çalıştırın. Bu işlem EXE dosyasını, kaynak PDF'leri veya çıkarılmış sayfaları silmez.

## Kaynaktan derleme

Python 3.10 veya üzeri gerekir.

```powershell
git clone https://github.com/morfiyus-sys/PDF-Ayiklayici2.git
cd PDF-Ayiklayici2
python -m pip install -r requirements.txt -r requirements-build.txt
python -m PyInstaller --noconfirm --clean --onefile --noconsole --name PDF_Ayikla .\PDF_Ayikla_USB_BUILD\PDF_Ayikla.py
```

Oluşan `dist/PDF_Ayikla.exe` dosyasını `PDF_Ayikla_USB` klasörüne kopyalayarak taşınabilir paketi güncelleyebilirsiniz.

## Kaynak yapısı

```text
PDF_Ayikla_USB/          Hazır taşınabilir paket
PDF_Ayikla_USB_BUILD/    Python kaynak kodu ve PyInstaller yapılandırması
```

## Lisans

PDF Ayıklayıcı 2, [MIT Lisansı](LICENSE) ile yayımlanmaktadır.

© 2026 ERDSoft.
