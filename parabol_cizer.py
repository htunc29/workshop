import matplotlib.pyplot as plt
import numpy as np

def parabol_ciz(a=1, b=0, c=0, x_min=-10, x_max=10):
    """
    Parabol çizen fonksiyon
    y = ax² + bx + c formülünü kullanır
    
    Parametreler:
    a: x²'nin katsayısı (varsayılan: 1)
    b: x'in katsayısı (varsayılan: 0)
    c: sabit terim (varsayılan: 0)
    x_min: x ekseni minimum değeri (varsayılan: -10)
    x_max: x ekseni maksimum değeri (varsayılan: 10)
    """
    
    # X değerleri oluştur
    x = np.linspace(x_min, x_max, 400)
    
    # Y değerlerini hesapla (y = ax² + bx + c)
    y = a * x**2 + b * x + c
    
    # Grafik oluştur
    plt.figure(figsize=(10, 8))
    plt.plot(x, y, 'b-', linewidth=2, label=f'y = {a}x² + {b}x + {c}')
    
    # Tepe noktasını işaretle (a ≠ 0 ise)
    if a != 0:
        tepe_x = -b / (2 * a)
        tepe_y = a * tepe_x**2 + b * tepe_x + c
        plt.plot(tepe_x, tepe_y, 'ro', markersize=8, label=f'Tepe Noktası ({tepe_x:.2f}, {tepe_y:.2f})')
    
    # Grafik ayarları
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title(f'Parabol: y = {a}x² + {b}x + {c}', fontsize=14)
    plt.legend()
    
    # Grafik göster
    plt.show()

def coklu_parabol_ciz():
    """
    Farklı parametrelerle birden fazla parabol çizer
    """
    x = np.linspace(-10, 10, 400)
    
    plt.figure(figsize=(12, 8))
    
    # Farklı parabol örnekleri
    paraboller = [
        (1, 0, 0, 'y = x²', 'blue'),
        (0.5, 0, 0, 'y = 0.5x²', 'red'),
        (-1, 0, 0, 'y = -x²', 'green'),
        (1, 2, 1, 'y = x² + 2x + 1', 'orange'),
        (2, -4, 2, 'y = 2x² - 4x + 2', 'purple')
    ]
    
    for a, b, c, label, color in paraboller:
        y = a * x**2 + b * x + c
        plt.plot(x, y, color=color, linewidth=2, label=label)
        
        # Tepe noktasını işaretle
        if a != 0:
            tepe_x = -b / (2 * a)
            tepe_y = a * tepe_x**2 + b * tepe_x + c
            plt.plot(tepe_x, tepe_y, 'o', color=color, markersize=6)
    
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title('Farklı Parabol Örnekleri', fontsize=14)
    plt.legend()
    plt.ylim(-20, 20)
    
    plt.show()

def interaktif_parabol():
    """
    Kullanıcıdan parametreler alarak parabol çizer
    """
    print("Parabol Çizici - İnteraktif Mod")
    print("y = ax² + bx + c formülü kullanılacak")
    print("-" * 40)
    
    try:
        a = float(input("a katsayısını girin (x²'nin katsayısı): "))
        b = float(input("b katsayısını girin (x'in katsayısı): "))
        c = float(input("c sabitini girin (sabit terim): "))
        
        x_min = float(input("X ekseni minimum değeri (varsayılan -10): ") or -10)
        x_max = float(input("X ekseni maksimum değeri (varsayılan 10): ") or 10)
        
        parabol_ciz(a, b, c, x_min, x_max)
        
    except ValueError:
        print("Hata: Lütfen geçerli sayılar girin!")

if __name__ == "__main__":
    print("Parabol Çizici Programı")
    print("1. Basit parabol (y = x²)")
    print("2. Özel parabol (kendi parametrelerinizle)")
    print("3. Çoklu parabol örnekleri")
    print("4. İnteraktif mod")
    
    try:
        secim = input("\nSeçiminizi yapın (1-4): ")
        
        if secim == "1":
            parabol_ciz()
        elif secim == "2":
            parabol_ciz(a=2, b=-4, c=1)  # Örnek: y = 2x² - 4x + 1
        elif secim == "3":
            coklu_parabol_ciz()
        elif secim == "4":
            interaktif_parabol()
        else:
            print("Geçersiz seçim! Basit parabol çiziliyor...")
            parabol_ciz()
            
    except KeyboardInterrupt:
        print("\nProgram sonlandırıldı!")
