import tkinter as tk
from tkinter import filedialog, messagebox
import pygame
import os

class MuzikCalarArayuz:
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("Otomatik Müzik Çalar - Mühendislik Portfolyosu")
        self.pencere.geometry("400x300")

        # Pygame ve Mixer Başlatma (Donanım Başlatma Mantığı)
        pygame.init()
        pygame.mixer.init()

        # Değişkenler
        self.sarki_listesi = []
        self.su_an_calan_indeks = 0

        # Arayüz Elemanları
        self.etiket = tk.Label(pencere, text="Müzik Klasörü Seçilmedi", wraplength=350)
        self.etiket.pack(pady=20)

        self.sec_buton = tk.Button(pencere, text="Klasör Seç", command=self.klasor_sec)
        self.sec_buton.pack(pady=10)

        self.baslat_buton = tk.Button(pencere, text="Oynatmayı Başlat", command=self.oynat, state=tk.DISABLED)
        self.baslat_buton.pack(pady=10)

        self.durum_etiketi = tk.Label(pencere, text="Durum: Bekleniyor...", fg="blue")
        self.durum_etiketi.pack(pady=20)

    def klasor_sec(self):
        dizin = filedialog.askdirectory()
        if dizin:
            self.sarki_listesi = [os.path.join(dizin, f) for f in os.listdir(dizin) if f.endswith('.mp3')]
            self.sarki_listesi.sort() # 001.mp3, 002.mp3 sıralaması [cite: 22]
            
            if self.sarki_listesi:
                self.etiket.config(text=f"Seçilen Klasör: {dizin}\n{len(self.sarki_listesi)} şarkı bulundu.")
                self.baslat_buton.config(state=tk.NORMAL)
            else:
                messagebox.showwarning("Hata", "Klasörde MP3 dosyası bulunamadı!")

    def oynat(self):
        if self.sarki_listesi:
            sarki = self.sarki_listesi[self.su_an_calan_indeks]
            pygame.mixer.music.load(sarki)
            pygame.mixer.music.play()
            
            sarki_adi = os.path.basename(sarki)
            self.durum_etiketi.config(text=f"Şu an çalıyor: {sarki_adi}", fg="green")
            
            # Otomatik geçiş için kontrol mekanizması (Akış Şeması Mantığı) [cite: 53-59]
            self.pencere.after(1000, self.kontrol_et)

    def kontrol_et(self):
        if not pygame.mixer.music.get_busy():
            self.su_an_calan_indeks += 1
            if self.su_an_calan_indeks < len(self.sarki_listesi):
                self.oynat()
            else:
                self.durum_etiketi.config(text="Tüm liste tamamlandı.", fg="black")
                messagebox.showinfo("Tamamlandı", "Müzik listesi başarıyla çalındı.") [cite: 62]
        else:
            self.pencere.after(1000, self.kontrol_et)

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = MuzikCalarArayuz(root)
    root.mainloop()