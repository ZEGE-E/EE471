from custom_classes import MediaItem


#book = MediaItem("Serenad", "Zülfü Livaneli")
#movie = MediaItem("Ejderhani Nasil Eğitirsin", "DreamWorks Animation")


from custom_classes import Book, DVD, LibraryCollection

my_library = LibraryCollection()


book1 = Book("Serenad", "Zülfü Livaneli", 328)
book2 = Book("Nutuk", "Mustafa Kemal Atatürk", 311)
dvd1 = DVD("Ejderhani Nasil Eğitirsin", "DreamWorks Animation", 148)


my_library.add_item(book1)
my_library.add_item(book2)
my_library.add_item(dvd1)


print("--- Başlangıçta Müsait Olanlar ---")
print(my_library.list_available())

print("\n--- Ödünç Alma İşlemleri ---")
print(book1.checkout())
print(dvd1.checkout())

print("\n--- Son Durumda Müsait Olanlar ---")
print(my_library.list_available())
