import random

while True:
    angka_rahasia = random.randint(1,20) #variabel integer Fungsi randint() selalu menghasilkan bilangan bulat (integer) dalam rentang yang ditentukan.
    percobaan = 0
    batas = 4
    print("\nTebak angka antara 1 sampai 20😼, kalo kamu benar aku punya hadiah 🎁 ") #kalimat pembuka
    print(f"Kamu hanya punya cuman sampe {batas} percobaan 🤯") #ini aturan main
    
    while percobaan < batas :
        tebakan = int(input("coba tebak, angka berapa sekarang 😭 : ")) #ketika game sudah di mulai
        percobaan +=1
        
        if percobaan == 1: # sistem poin berdasarkan percobaan
            poin = 100
        elif percobaan == 2:
            poin = 75
        elif percobaan == 3:
            poin = 50
        else:
            poin = 25

        if tebakan == angka_rahasia:
            print(f"kok kamu pintar 🤑, tebakanmu benar {angka_rahasia}") #ketika jawabannya benar
            print(f"nih hadiah nya buat kamu 🫦, plus kamu dapat {poin} poin 🎯 ") #ucapan hadiah
            
            #kesan akrab
            komentar = input(f"apa motivasimu bisa nebak angka {angka_rahasia} dengan tepat? 😁 : ") #untuk menarik agar pemain mengeluarkan motibasinya
            print(f"Wah, motivasimu ini: {komentar} memang top 👍") #kalimat memuji pemain dengan motivasi keren nya
            break
        elif tebakan < angka_rahasia:
            if percobaan == 1:
                print(f"tenang ini masih percobaan pertama, {tebakan} terlalu kecil 👶. kamu sudah kehilangan poin sebanyak {poin} 😾 ")
            elif percobaan == 2:
                print(f"ko masih salah kamu gak belajar dari sebelumnya, {tebakan} kurang besar 😅. sekarang hilang {poin} poin 😁 ")
            elif percobaan == 3:
                print(f"Aduh kamu, {tebakan} itu masih terlalu kecil, semangat! 💪. jumlah poin yang hilang {poin} 👶")
            else:
                print(f"Kasian banget kamu, {tebakan} tetap terlalu kecil 👺. kamu kehilangan poin terakhir {poin} 🤑")
        else:
            if percobaan == 1:
                print(f"wajar saja percobaan pertama, {tebakan} terlalu besar 🏔️. kehilangan poin terbesar {poin} ⏳")
            elif percobaan == 2:
                print(f"hah seorang kamu masih salah, {tebakan} itu kebesaran 😅. lagi lagi kamu kehilangan {poin} ini 💪")
            elif percobaan == 3:
                print(f"Aduh aku kira kamu pintar, {tebakan} masih terlalu besar, jangan menyerah! 💪. poin ini juga hangus {poin} 👺")
            else:
                print(f"Yang bener dong ahh, {tebakan} itu terlalu besar 😾. kamu tidak mendapatkan poin terkahir {poin} ✈️")
            
        if percobaan == batas:
            print(f"aduh kasian,kamu kehabisan percobaan. angka yang benar adalah eng ing eng {angka_rahasia} 😂") #menampilkan kesan lucu
            komentar = input(f"ada masalah apa sih, kok kamu bisa gagal dalam game ini. coba ceritain masalahnya ")
            print(f"owh ini masalah nya, {komentar}. solusi dari aku si semangat aja terus jangan menyerah, biar pengalaman mu banyak ")

    ulang = input("ingat keberuntungan sedang menunggu mu✈️, ayo main lagi()y/n): ").lower() #sekalian promosi
    if ulang != "y":
        print("artinya kamu menunda keberuntungan⏳") #biar pemain merasa tertantang di game selanjutnya
        break
        