import numpy as np
import time
import matplotlib.pyplot as plt
import sounddevice as sd

def myConv(x, n, y, m):
    sonuc = np.zeros(n + m - 1) 
    for i in range(n):
        for j in range(m):
            sonuc[i + j] += x[i] * y[j]
    return sonuc

flag = 1
while(flag):
    n = int(input("x'in boyutu: "))
    m = int(input("y'nin boyutu: "))

    alinanDizi = input("x'i boşluklarla ayirarak girin: ")
    alinanListe = alinanDizi.split()
    x = np.array([int(sayi) for sayi in alinanListe])

    print("0 noktasinin indisini girin: ")
    x0 = int(input())

    alinanDizi = input("y'yi boşluklarla ayirarak girin: ")
    alinanListe = alinanDizi.split()
    y = np.array([int(sayi) for sayi in alinanListe])

    print("0 noktasinin indisini girin: ")
    y0 = int(input())

    print("x:", x)
    print("y:", y)


    start_time = time.perf_counter()
    sonuc = myConv(x, n, y, m)
    end_time = time.perf_counter()
    elapsed_time = (end_time - start_time)

    print("MyConv gecen zaman:", elapsed_time*1000000)

    # Convolution code
    start_time = time.perf_counter()
    sonuc2 = np.convolve(x, y, mode='full')
    end_time = time.perf_counter()
    elapsed_time1= (end_time - start_time)

    print("hazir fonksiyon gecen zaman:", elapsed_time1*1000000)

    # Vektörel gösterim
    print("Vektörel gösterim:")
    print("X[n]:", x)
    print("Y[m]:", y)
    print("Hazir konvolusyon fonksiyonu sonucu:", sonuc2)
    print("Benim sonucum:", sonuc)

    # Plotting
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 2, 1)
    plt.stem(range(-x0, -x0+len(x)), x)
    plt.title('X[n]')

    plt.subplot(2, 2, 2)
    plt.stem(range(-y0, -y0+len(y)), y)
    plt.title('Y[m]')
    if x0>y0:
        bas = x0
    else:
        bas = y0
    plt.subplot(2, 2, 3)
    plt.stem(range(-bas, -bas+len(sonuc2)), sonuc2)
    plt.title('Hazir fonksiyon sonucu')

    plt.subplot(2, 2, 4)
    plt.stem(range(-bas, -bas+len(sonuc)), sonuc)
    plt.title('MyConv sonucu')
    #grafik çizdirme
    plt.tight_layout()
    plt.show()
    print("baska veri setleri ile tekrar denemek ister misiniz (e/h)")
    devam = input()
    if devam == "h":
        flag = 0

def grafik(x, y, ses):
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 2, 1)
    plt.stem(range(0, len(ses)), ses)
    plt.title('kaydedilen ses')

    plt.subplot(2, 2, 3)
    plt.stem(range(0, len(x)), x)
    plt.title('MyConv sonucu')

    plt.subplot(2, 2, 4)
    plt.stem(range(0, len(y)), y)
    plt.title('Hazir fonksiyon sonucu')
    #grafik çizdirme
    plt.tight_layout()
    plt.show()

print("Ses kaydina baslanilsin mi (evet icin e giriniz): ")
basla = input()
if basla == "e":
    
    orneklemeFrekansi = 8000
    #5 saniyelik ses kaydı
    print("5 saniyelik ses kaydi yapiliyor...")
    print("Start speaking.")
    recording = sd.rec(int(5 * orneklemeFrekansi), samplerate=orneklemeFrekansi, channels=1, dtype=np.int16)
    sd.wait()
    print("End of Recording.")

    # Kaydedilen ses verisi numpy dizisine kaydedilir
    ses5 = np.squeeze(recording)

    # Kaydedilen sesi dinleme
    print("Playing recorded audio...")
    sd.play(ses5, samplerate=orneklemeFrekansi)
    sd.wait()
    print("Playback finished.")

    print("10 saniyelik ses kaydina baslanilsin mi (evet icin e giriniz): ")
    basla2 = input()
    if basla2 == "e":

        #10 saniyelik ses kaydı
        print("10 saniyelik ses kaydi yapiliyor...")
        print("Start speaking.")
        recording = sd.rec(int(10 * orneklemeFrekansi), samplerate=orneklemeFrekansi, channels=1, dtype=np.int16)
        sd.wait()
        print("End of Recording.")

        # Kaydedilen ses verisi numpy dizisine kaydedilir
        ses10 = np.squeeze(recording)

        # Kaydedilen sesi dinleme
        print("Playing recorded audio...")
        sd.play(ses10, samplerate=orneklemeFrekansi)
        sd.wait()
        print("Playback finished.")

    

    def h(m):
        y = np.zeros(m*3000+1)
        for i in range(m+1):
            y[i*3000] = 2**(-i) * i
        y[0] = 1
        return y

    h3 = h(3)
    h4 = h(4)
    h5 = h(5)

    flag = 1
    while(flag):
        print("1) 5saniye icin m = 3:")
        print("2) 5saniye icin m = 4:")
        print("3) 5saniye icin m = 5:")
        print("4) 10saniye icin m = 3:")
        print("5) 10saniye icin m = 4:")
        print("6) 10saniye icin m = 5:")
        print("7) cikis")
        secim = int(input("Seciminizi yapin: "))
        if secim == 1:
            #m=3 icin 5 saniyelik ses
            start_time = time.perf_counter()
            hazirY53 = np.convolve(ses5, h3, mode='full')
            end_time = time.perf_counter()
            elapsed_time1 = (end_time - start_time)
            print("listening hazirY53")
            sd.play(hazirY53, samplerate=orneklemeFrekansi)
            sd.wait()

            start_time = time.perf_counter()
            myY53 = myConv(ses5, len(ses5), h3, len(h3))
            end_time = time.perf_counter()
            elapsed_time2 = (end_time - start_time)
            print("listening myY53")
            sd.play(myY53, samplerate=orneklemeFrekansi)
            sd.wait() 
            print("Hazir fonksiyon gecen zaman:", elapsed_time1*1000000)
            print("MyConv gecen zaman:", elapsed_time2*1000000)
            grafik(myY53, hazirY53, ses5) 
            
        elif secim == 2:
            #m=4 icin 5 saniyelik ses
            start_time = time.perf_counter()
            hazirY54 = np.convolve(ses5, h4, mode='full')
            end_time = time.perf_counter()
            elapsed_time1 = (end_time - start_time)
            print("listening hazirY54")
            sd.play(hazirY54, samplerate=orneklemeFrekansi)
            sd.wait()

            start_time = time.perf_counter()
            myY54 = myConv(ses5, len(ses5), h4, len(h4))
            end_time = time.perf_counter()
            elapsed_time2 = (end_time - start_time)
            print("listening myY54")
            sd.play(myY54, samplerate=orneklemeFrekansi)
            sd.wait()
            print("Hazir fonksiyon gecen zaman:", elapsed_time1*1000000)
            print("MyConv gecen zaman:", elapsed_time2*1000000)
            grafik(myY54, hazirY54, ses5)
        elif secim == 3:
            #m=5 icin 5 saniyelik ses
            start_time = time.perf_counter()
            hazirY55 = np.convolve(ses5, h5, mode='full')
            end_time = time.perf_counter()
            elapsed_time1 = (end_time - start_time)
            print("listening hazirY55")
            sd.play(hazirY55, samplerate=orneklemeFrekansi)
            sd.wait()

            start_time = time.perf_counter()
            myY55 = myConv(ses5, len(ses5), h5, len(h5))
            end_time = time.perf_counter()
            elapsed_time2 = (end_time - start_time)
            print("listening myY55")
            sd.play(myY55, samplerate=orneklemeFrekansi)
            sd.wait()
            print("Hazir fonksiyon gecen zaman:", elapsed_time1*1000000)
            print("MyConv gecen zaman:", elapsed_time2*1000000)
            grafik(myY55, hazirY55, ses5)
        elif secim == 4:
            #m=3 icin 10 saniyelik ses
            start_time = time.perf_counter()
            hazirY103 = np.convolve(ses10, h3, mode='full')
            end_time = time.perf_counter()
            elapsed_time1 = (end_time - start_time)
            print("listening hazirY103")
            sd.play(hazirY103, samplerate=orneklemeFrekansi)
            sd.wait()

            start_time = time.perf_counter()
            myY103 = myConv(ses10, len(ses10), h3, len(h3))
            end_time = time.perf_counter()
            elapsed_time2 = (end_time - start_time)
            print("listening myY103")
            sd.play(myY103, samplerate=orneklemeFrekansi)
            sd.wait()
            print("Hazir fonksiyon gecen zaman:", elapsed_time1*1000000)
            print("MyConv gecen zaman:", elapsed_time2*1000000)
            grafik(myY103, hazirY103, ses10)
        elif secim == 5:
            #m=4 icin 10 saniyelik ses
            start_time = time.perf_counter()
            hazirY104 = np.convolve(ses10, h4, mode='full')
            end_time = time.perf_counter()
            elapsed_time1 = (end_time - start_time)
            print("listening hazirY104")
            sd.play(hazirY104, samplerate=orneklemeFrekansi)
            sd.wait()

            start_time = time.perf_counter()
            myY104 = myConv(ses10, len(ses10), h4, len(h4))
            end_time = time.perf_counter()
            elapsed_time2 = (end_time - start_time)
            print("listening myY104")
            sd.play(myY104, samplerate=orneklemeFrekansi)
            sd.wait()
            print("Hazir fonksiyon gecen zaman:", elapsed_time1*1000000)
            print("MyConv gecen zaman:", elapsed_time2*1000000)
            grafik(myY104, hazirY104, ses10)
        elif secim == 6:
            #m=5 icin 10 saniyelik ses
            start_time = time.perf_counter()
            hazirY105 = np.convolve(ses10, h5, mode='full')
            end_time = time.perf_counter()
            elapsed_time1 = (end_time - start_time)
            print("listening hazirY105")
            sd.play(hazirY105, samplerate=orneklemeFrekansi)
            sd.wait()

            start_time = time.perf_counter()
            myY105 = myConv(ses10, len(ses10), h5, len(h5))
            end_time = time.perf_counter()
            elapsed_time2 = (end_time - start_time) 
            print("listening myY105")
            sd.play(myY105, samplerate=orneklemeFrekansi)
            sd.wait()
            print("Hazir fonksiyon gecen zaman:", elapsed_time1*1000000)
            print("MyConv gecen zaman:", elapsed_time2*1000000)
            grafik(myY105, hazirY105, ses10)
        elif secim == 7:
            flag = 0



 