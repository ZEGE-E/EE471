class MediaItem:
    # Kütüphane için temel sınıfım
    def __init__(self, title, author):
        self.title = title       # Gelen başlığı nesneye kaydediyorum
        self.author = author     # Yazarı/yönetmeni kaydediyorum
        self.is_available = True # Başlangıçta materyali müsait kabul ediyorum

    # Ödünç almak için
    def checkout(self):
        if self.is_available:    # Eğer materyal kütüphanedeyse
            self.is_available = False #birisi aldı güncelliyorum
            return "Successful checkout"
        else:
            return "Already out" # Biri zaten almışsa uyarı dönüyorum
        
    #geri getirme fonksiyonu
    def return_item(self):
        self.is_available = True # Tekrar rafta müsait duruma getiriyorum

    
    def __str__(self):
        if self.is_available:
            status = "Available" # Müsaitse Available yazsın
        else:
            status = "Checked Out" # Değilse Checked Out yazsın
            
        # İstenen formatta string döndürüyorum
        return f"{self.title} by {self.author} [{status}]"


class Book(MediaItem):  
    # Kitaplar için alt sınıf MediaItem'dan alıyorum
    def __init__(self, title, author, page_count):  
        super().__init__(title, author) # Başlık ve yazarı üst sınıfa yollayıp orada hallettiriyorum
        self.page_count = page_count    # sayfa sayısını kaydediyorum

    # Kitapları yazdırırken sayfa sayısını da göstermek için 
    def __str__(self):  
        # Durum kontrolü 
        status = "Available" if self.is_available else "Checked Out"
        #sayfa sayısını da ekleyip döndürüyorum
        return f"{self.title} by {self.author} ({self.page_count} pages) [{status}]"


class DVD(MediaItem):
    # DVD'ler için subclass
    def __init__(self, title, author, duration):
        super().__init__(title, author) 
        self.duration = duration        # süre bilgisini ekliyoruz

  
    def checkout(self):
        print("Handle with care: Do not scratch the disc.") #uyarı mesajı
        return super().checkout() # Asıl müsaitlik kontrolü ve ödünç alma işini üst sınıftaki fonksiyona yaptırıyorum
    
    

class LibraryCollection:
    
    def __init__(self): 
        self.items = [] # boş bir liste 

    #yeni eşya ekleme fonksiyonu
    def add_item(self, item):
        self.items.append(item) # Gelen materyali listemizin sonuna ekliyorum


    # Sadece rafta olanları getiren fonksiyon
    def list_available(self):
        available_titles = [] # Sadece isimleri tutacağımız geçici bir boş liste

        for item in self.items: # Kütüphanedeki tüm eşyaları tek tek geziyoruz
            
            if item.is_available: # Eğer gezdiğimiz eşya müsaitse
            
                available_titles.append(item.title) # İsmini geçici listemize ekliyoruz
                
        return available_titles # Döngü bitince bu müsait listeyi geri gönderiyoruz