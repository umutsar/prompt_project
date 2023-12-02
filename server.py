import time
from random import randint
 
def write_slow(cevap):
    for harf in cevap:
        print(harf, end='', flush=True)
        time.sleep(0.02)  # Her harf arasında 0.1 saniye bekletiyoruz.
    print()  # Cevabın tamamlandığını göstermek için yeni bir satıra geçiyoruz.

def take_to_list():
    with open('./veda_user.txt', 'r') as veda_bot_txt:
        veda_bot_satirlar = veda_bot_txt.readlines()
        fixed_veda_bot = [satir.strip() for satir in veda_bot_satirlar]
        random_veda_message = fixed_veda_bot[randint(0, len(fixed_veda_bot) - 1)]
        return random_veda_message



def main():
    print("Bot: Merhaba! Benimle konuşabilirsiniz. Çıkış yapmak için 'görüşürüz' yazabilirsiniz.\n")

    while True:
        
        kullanici_girisi = input("Kullanıcı: ")

        if kullanici_girisi.lower() == 'exit':
            write_slow("Bot: Görüşmek üzere, iyi günler dilerim!")
            break

        cevap = take_to_list()
        write_slow("Bot: " + cevap + "\n")

if __name__ == "__main__":
    main()
