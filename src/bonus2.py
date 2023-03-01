import matplotlib.pyplot as plt
import random
import numpy as np
import time
import src.tucil2 as tucil2


def Rn():
    # BONUS 2
    n = int(input("Masukkan jumlah titik : "))
    dimensi = int(input("Masukkan dimensi : "))
    points = np.array([[random.randint(-1000, 1000) for i in range(dimensi)] for j in range(n)])

    # cari sepasang titik terdekat dengan algoritma brute force
    start_time = time.time()
    brute_result, brute_distance, brute_count = tucil2.brute_force(points)
    brute_time = time.time() - start_time
    print("Hasil Brute Force:")
    print("Sepasang titik terdekat:", brute_result)
    print("Jarak terdekat:", brute_distance)
    print("Banyaknya operasi perhitungan:", brute_count)
    print("Waktu riil (detik):", brute_time)


# Algoritma divide and conquer
    start_time = time.time()
    dnc_result, dnc_distance, dnc_count = tucil2.divide_and_conquer(points)
    dnc_time = time.time() - start_time
    print("\nHasil Divide and Conquer:")
    print("Sepasang titik terdekat:", dnc_result)
    print("Jarak terdekat:", dnc_distance)
    print("Banyaknya operasi perhitungan:", dnc_count)
    print("Waktu riil (detik):", dnc_time)
    print("\n")

    plt.show()