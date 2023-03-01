import random
import math
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Fungsi untuk menghitung jarak antara dua titik
def jarak_euclidean(x, y):
    return math.sqrt(sum([(x[i] - y[i]) ** 2 for i in range(len(x))]))

# Fungsi untuk mencari sepasang titik terdekat dengan algoritma brute force
def brute_force(points):
    n = len(points)
    distance_terdekat = float('inf')
    pasangan_terdekat = None
    count = 0

    for i in range(n):
        for j in range(i+1, n):
            distance = jarak_euclidean(points[i], points[j])
            count += 1
            if distance < distance_terdekat:
                distance_terdekat = distance
                pasangan_terdekat = (points[i], points[j])

    return pasangan_terdekat, distance_terdekat, count

# Fungsi untuk mencari sepasang titik terdekat dengan algoritma divide and conquer
def divide_and_conquer(points):
    def dnc(points_sorted):
        n = len(points_sorted)

        if n <= 3:
            return brute_force(points_sorted)

        mid = n // 2                                           # mid adalah indeks titik tengah
        l_pair, l_distance, l_count = dnc(points_sorted[:mid])
        r_pair, r_distance, r_count = dnc(points_sorted[mid:])
        pasangan_terdekat = l_pair
        distance_terdekat = l_distance
        count = l_count + r_count

        if r_distance < l_distance:
            pasangan_terdekat = r_pair
            distance_terdekat = r_distance

        strip = []                                             # strip adalah daftar titik yang berada di sekitar garis tengah
        for i in range(n):
            if abs(points_sorted[i][0] - points_sorted[mid][0]) < distance_terdekat:
                strip.append(points_sorted[i])

        for i in range(len(strip)):
            for j in range(i+1, min(len(strip), i+7)):
                distance = jarak_euclidean(strip[i], strip[j])
                count += 1
                if distance < distance_terdekat:
                    distance_terdekat = distance
                    pasangan_terdekat = (strip[i], strip[j])

        return pasangan_terdekat, distance_terdekat, count

    points_sorted = sorted(points, key=lambda p: p[0])
    return dnc(points_sorted)

# Fungsi untuk membangkitkan titik secara acak
def acak_titik(n):
    points = []
    for i in range(n):
        x = random.randint(-1000, 1000)
        y = random.randint(-1000, 1000)
        z = random.randint(-1000, 1000)
        points.append((x, y, z))
    return points


# BONUS 1
# Fungsi untuk menggambar titik-titik dalam bidang 3D dan menandai sepasang titik terdekat
def plot_points(points, pasangan_terdekat=None):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    zs = [p[2] for p in points]
    ax.scatter(xs, ys, zs)
    if pasangan_terdekat:
        ax.scatter([pasangan_terdekat[0][0], pasangan_terdekat[1][0]], [pasangan_terdekat[0][1], pasangan_terdekat[1][1]], [pasangan_terdekat[0][2], pasangan_terdekat[1][2]], c='r') 
        ax.plot([pasangan_terdekat[0][0], pasangan_terdekat[1][0]], [pasangan_terdekat[0][1], pasangan_terdekat[1][1]], [pasangan_terdekat[0][2], pasangan_terdekat[1][2]], c='r')
    plt.show()


# Main program
def dimensi_tiga():
    n = int(input("Masukkan banyaknya titik: "))
    points = acak_titik(n)

# Algoritma brute force
    start_time = time.time()
    brute_result, brute_distance, brute_count = brute_force(points)
    brute_time = time.time() - start_time
    print("\nHasil Brute Force:")
    print("Sepasang titik terdekat:", brute_result)
    print("Jarak terdekat:", brute_distance)
    print("Banyaknya operasi perhitungan:", brute_count)
    print("Waktu riil (detik):", brute_time)


# Algoritma divide and conquer
    start_time = time.time()
    dnc_result, dnc_distance, dnc_count = divide_and_conquer(points)
    dnc_time = time.time() - start_time
    print("\nHasil Divide and Conquer:")
    print("Sepasang titik terdekat:", dnc_result)
    print("Jarak terdekat:", dnc_distance)
    print("Banyaknya operasi perhitungan:", dnc_count)
    print("Waktu riil (detik):", dnc_time)
    print("\n")

    if n <= 1000:
        plot_points(points, pasangan_terdekat=dnc_result)
        plt.show()
