import src.tucil2 as tucil2 
import bonus2

def main():
    while True:
        print("=============================================================================================")
        print("========== Mencari Pasangan Titik Terdekat 3D dengan Algoritma Divide and Conquer ===========")
        print("=============================================================================================")
        print("1. Dimensi Tiga")
        print("2. Dimensi Banyak")
        print("3. Keluar")
        pilihan = int(input("Masukan Pilihan =  "))
        if pilihan == 1:
            tucil2.dimensi_tiga()
        elif pilihan == 2:
            bonus2.Rn()
        elif pilihan == 3:
            print("Byee\n")
            break
        else:
            print("Pilihan yang bener!!!\n")

main()