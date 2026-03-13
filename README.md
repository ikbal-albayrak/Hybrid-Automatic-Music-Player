# Hybrid-Automatic-Music-Player
Hybrid Automatic Music Player (Arduino & Python)Bu proje, bir işletmenin (kafe, restoran vb.) müzik yayınını otomatize etmek için tasarlanmış, donanım ve yazılım katmanlarını birleştiren hibrit bir sistemdir . Sistem, bir kullanıcı arayüzü (GUI) üzerinden kontrol edilebildiği gibi, donanım tarafında bağımsız bir MP3 çalma modülü ile entegre çalışır .


Özellikler (Features)
Otomatik Oynatma: Belirlenen klasördeki müzikleri sırayla ve kesintisiz oynatır.Hibrit Kontrol: Hem Python tabanlı bir arayüz hem de Arduino tabanlı bir donanım kontrol mekanizması içerir .
Hata Yönetimi: Donanım bağlantısını otomatik kontrol ederek kullanıcıya geri bildirim sağlar.
Akıllı Sıralama: Müzik dosyalarını belirli bir isimlendirme formatına (örn: 001.mp3) göre sıralayarak okur.


Donanım Mimarisi (Hardware)
Sistemin donanım ayağı, Arduino Uno ve UART protokolü üzerinden haberleşen bileşenlerden oluşur.
Arduino UNO: Sistemin ana kontrol birimi.
DFPlayer Mini: MP3 dosyalarını işleyen ve hoparlöre aktaran ses modülü.
SD Kart: Müzik dosyalarının FAT32 formatında depolandığı alan.
Hoparlör: Ses çıkış birimi.


Yazılım Mimarisi (Software)
Yazılım tarafı, kullanıcı deneyimini ön plana çıkaran ve donanım mantığını simüle eden bir yapıya sahiptir.
GUI: Tkinter kütüphanesi ile geliştirilmiş kullanıcı dostu arayüz.
Medya Kontrolü: Pygame kütüphanesi ile asenkron şarkı geçişleri ve durum kontrolü.
OOP Yaklaşımı: Proje, modülerliği ve sürdürülebilirliği sağlamak için Nesne Yönelimli Programlama prensipleriyle kodlanmıştır.


Kurulum ve Bağımlılıklar
Arduino:SoftwareSerial ve DFRobotDFPlayerMini kütüphanelerini Arduino IDE'ye kurun.
Hardware klasöründeki .ino dosyasını Arduino Uno'nuza yükleyin .

Python:Bağımlılıkları tek seferde yüklemek için terminale şu komutu yazın: pip install -r requirements.txt


Sistem Akışı (System Flow)Sistem başlatıldığında sırasıyla şu adımları izler:
Donanım/Yazılım Başlatma: Kütüphaneler ve portlar hazır hale getirilir .
Dosya Kontrolü: Klasördeki veya SD karttaki müzikler taranır.
Sürekli Döngü: Müzik bittiğinde otomatik olarak bir sonraki parçaya geçiş yapılır.
