# Laporan Proyek Machine Learning - I Wayan Adi Saputra

## Domain Proyek

### Domain : Lingkungan / Udara
### Latar belakang
Pencemaran udara adalah masalah serius yang telah membawa dampak konkret dan merugikan terhadap kesehatan manusia. Data statistik yang ada menggambarkan dampak yang mengkhawatirkan dari pencemaran udara terhadap masyarakat. Pencemaran udara telah dikaitkan dengan peningkatan insiden penyakit pernapasan seperti asma, bronkitis, dan bahkan kanker paru-paru. Di samping itu, penyakit jantung juga memiliki keterkaitan erat dengan kualitas udara yang buruk. Studi ilmiah telah menunjukkan bahwa orang yang terpapar polusi udara yang tinggi memiliki risiko yang lebih tinggi untuk mengembangkan penyakit jantung koroner, yang dapat mengakibatkan serangan jantung fatal.

Lebih dari itu, pencemaran udara juga memiliki dampak buruk pada kelompok rentan seperti anak-anak dan lansia. Anak-anak yang tinggal di daerah dengan tingkat pencemaran udara tinggi dapat mengalami gangguan pertumbuhan paru-paru, yang dapat berdampak seumur hidup pada kesehatan mereka. Sementara itu, lansia lebih rentan terhadap komplikasi penyakit pernapasan yang disebabkan oleh polusi udara.

Untuk mengatasi masalah serius ini, diperlukan upaya serius dalam pemantauan dan pengelolaan kualitas udara. Inilah di mana teknologi sensor dan Internet of Things (IoT) memainkan peran yang sangat penting. Teknologi sensor canggih dan jaringan IoT telah memungkinkan pengumpulan data kualitas udara yang lebih akurat dan real-time. Sensor-sensor ini tersebar luas di seluruh wilayah perkotaan, mengukur parameter seperti partikel PM2,5, oksida nitrogen, dan senyawa organik volatil.

Melalui jaringan IoT, data ini dikumpulkan secara terus-menerus dan dikirim ke pusat pemantauan. Ini memungkinkan para peneliti dan ahli lingkungan untuk memahami dengan lebih baik pola pencemaran udara, mengidentifikasi sumber polusi, dan merespons perubahan dengan cepat. Selain itu, data yang dihasilkan oleh teknologi sensor dan IoT ini juga memberikan informasi yang lebih akurat dan tepat waktu kepada masyarakat.

Masyarakat dapat mengakses data ini melalui aplikasi seluler atau situs web yang memungkinkan mereka untuk mengambil tindakan preventif. Misalnya, mereka dapat menghindari daerah dengan tingkat pencemaran tinggi saat kualitas udara sedang buruk, atau mereka dapat menggunakan masker penutup wajah untuk mengurangi risiko terpapar partikel berbahaya.

Dengan demikian, teknologi sensor dan IoT bukan hanya alat penting dalam pemantauan dan manajemen lingkungan yang lebih efektif, tetapi juga merupakan alat penting dalam melibatkan dan memberdayakan masyarakat untuk melindungi kesehatan mereka sendiri. Dengan data yang lebih akurat dan akses yang lebih mudah, individu dapat menjadi bagian dari solusi dalam mengurangi dampak negatif dari pencemaran udara terhadap kesehatan mereka dan lingkungan sekitar.

## Business Understanding
Proyek ini bertujuan untuk membantu pemangku kepentingan dalam menangani permasalahan polusi udara dengan pendekatan analitik:
- Pemerintah: Melalui analisis prediktif terkait kualitas udara, pemerintah dapat memberikan solusi preventif yang lebih efektif untuk mengatasi masalah polusi udara.
- Masyarakat: Dengan pemahaman yang lebih baik tentang kualitas udara dan perubahan yang mungkin terjadi, masyarakat dapat mempersiapkan diri dengan lebih baik saat kualitas udara memburuk.
### Problem Statements
- Parameter yang Berkaitan: Parameter apa yang paling kuat berhubungan dengan tingkat kualitas udara, dan bagaimana pengaruhnya terhadap polusi udara?
- Dampak Arah Angin: Bagaimana arah dan kecepatan angin mempengaruhi tingkat polusi udara?
- Pemilihan Model: Manakah model yang paling tepat untuk memprediksi kualitas udara?
### Goals
Tujuan dari proyek ini adalah:
- Menganalisis Faktor Utama: Mengidentifikasi parameter yang paling berpengaruh pada kualitas udara, mengevaluasi dampak pergerakan angin, dan membangun model prediksi yang akurat.
- Rekomendasi Preventif: Memberikan rekomendasi tindakan preventif kepada pemerintah berdasarkan hasil analisis, sehingga mereka dapat mengambil tindakan yang lebih efektif.

### Key Metrics
Untuk mengukur kesuksesan proyek, akan digunakan beberapa metrik kunci, termasuk:
- Mean Absolute Error (MAE): Sebagai ukuran akurasi model dalam memprediksi kualitas udara.
- Korelasi Parameter: Untuk menilai sejauh mana parameter tertentu berkaitan dengan tingkat polusi udara.
- Visualisasi yang Informatif: Keberhasilan dalam menciptakan visualisasi yang informatif untuk pemangku kepentingan.
Dengan mengintegrasikan metrik ini, proyek ini akan dapat memberikan hasil yang lebih terukur dan fokus pada tujuan dan permasalahan yang diidentifikasi.

## Data Understanding
Dataset yang digunakan meruapakan dataset kualitas udara di kota Changping, sumber data yaitu: https://drive.google.com/file/d/1RhU3gJlkteaAQfyn9XOVAz7a5o1-etgr/view
Informasi dataset:
- Dataset berformat csv
- Dataset memiliki 35064 sample dengan 18 fitur.
- Dataset memiliki 11 fitur bertipe data float64, 5 fitur bertipe data int64, dan 2 fitur bertipe data object.

### Variabel-variabel pada dataset adalah sebagai berikut:
- No: Nomor urut dari sample data
- year: tahun sample data diambil
- month: bulan sample data diambil
- day : hari sample data diambil
- PM2.5: Konsentrasi PM2.5 (ug/m^3)
- PM10: Konsentrasi PM10 (ug/m^3)
- SO2: Konsentrasi SO2 (ug/m^3)
- NO2: Konsentrasi NO2 (ug/m^3)
- CO: Konsentrasi CO (ug/m^3)
- O3: Konsentrasi O3 (ug/m^3)
- TEMP: suhu (derajat Celsius)
- PRES: tekanan (hPa)
- DEWP: suhu titik embun (derajat Celsius)
- RAIN: curah hujan (mm)
- wd: arah angin
- WSPM: kecepatan angin (m/s)
- station: nama lokasi pemantauan kualitas udara

Dari semua variable yang ada, variable PM2.5 menjadi fitur yang akan di prediksi (y)
### Univariate Analisis
Univariate Analysis adalah menganalisis setiap fitur didalam data secara terpisah.
#### Analisis jumlah nilai unique pada setiap fitur kategorik
Terdapat 2 fitur kategorik yang ada didalam dataset yaitu wd dan station, fitur 'wd' ini memiliki sebaran yang cukup merata, Data yang tersebar berada diantara rentang 1000 sampai dengan 3000 sedangkan fitur 'station' (nama lokasi pemantauan kualitas udara), fitur ini hanya terdiri dari satu data nama lokasi yaitu Changping sebanyak 35064 data.

#### Analisis sebaran pada setiap fitur numerik
![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/be404a86-adcc-412b-a338-fce1c5ae6cb9)

Gambar 1: Analisis sebaran pada setiap fitur numerik

Analisis:
- Peningkatan Partikel udara sebanding dengan penurunan jumlah sampel. Hal ini dapat dilihat jelas dari histogram "PM2.5" yang grafiknya mengalami penurunan seiring dengan semakin banyaknya jumlah sampel (sumbu x).
- Rentang partikel cukup tinggi yaitu dari skala ratusan hingga sekitar 15 ribuan.
- Distribusi harga miring ke kanan (right-skewed). Hal ini akan berimplikasi pada model.

### Multivariate analysis
![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/f7127486-da8e-4885-856f-c946b4386f14)

Gambar 2: Analisis fitur kategori

Fitur 'wd' rata-rata partikel PM2.5 cenderung mirip, rentangnya berada diantara 45 sampai dengan 95. Kesimpulannya fitur kategorikal tidak terlalu mempengaruhi tingkat partikel diudara.

### Correlation Matrix
![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/056ffc65-0c4c-46ef-a723-6837f917bd11)

Gambar 3: Correlation Matrix

Analisis: Berdasarkan hasil visualisasi yang didapat dapat disimpulkan fitur yang berkolerasi tinggi dengan PM2.5 yaitu PM10, NO2, dan CO. Sedangkan wd, date, year, month, day, hour tidak berkorelasi dengan baik sehingga bisa di drop.


## Data Preparation
1. Train Test Split
   Train test split aja proses membagi data menjadi data train dan data test. Data latih akan digunakan untuk membangun model, sedangkan data uji akan digunakan untuk menguji performa model. Pada proyek ini dataset dibagi dengan perbandingan 80% untuk data training dan 20% untuk data testing.

2. Normalization
   Algoritma machine learning akan memiliki performa lebih baik dan bekerja lebih cepat jika dimodelkan dengan data seragam yang memiliki skala relatif sama. Salah satu teknik normalisasi yang digunakan pada proyek ini adalah Standarisasi dengan sklearn.preprocessing.StandardScaler.

### Mengatasi Missing Value
1. **Mengisi Missing Value dengan Rata-Rata (Mean Imputation)**:
   Dalam langkah pertama, kode ini mengisi missing value dalam kolom-kolom numerik dengan nilai rata-rata dari setiap kolom. Ini adalah teknik yang umum digunakan untuk mengatasi missing value dalam data numerik. Misalnya, jika memiliki data keuangan dan ada beberapa nilai yang hilang dalam kolom "Pendapatan", kemudian dapat menggantinya dengan rata-rata pendapatan dari seluruh data. Kemudian menghitung rata-rata untuk setiap kolom numerik dalam DataFrame dan menggantikan nilai-nilai yang hilang dengan rata-rata tersebut.

2. **Mengisi Missing Value dalam Kolom Objek (Object Columns) dengan "Unknown"**:
   Dalam langkah kedua, kode ini mengatasi missing value dalam kolom dengan tipe data objek (biasanya berisi data kategorikal) dengan menggantinya dengan string "Unknown". Ini adalah pendekatan yang umum digunakan untuk mengatasi missing value dalam kolom-kolom yang berisi kategori atau label, di mana menggantinya dengan "Unknown" dapat menjadi alternatif yang berguna.

Kombinasi dari kedua langkah ini memastikan bahwa data numerik diisi dengan nilai rata-rata yang masuk akal, sementara data objek (kategori) diisi dengan "Unknown" sebagai placeholder. Teknik ini membantu mempertahankan integritas data dan memungkinkan analisis lebih lanjut tanpa kehilangan informasi yang signifikan karena missing value.


## Modeling
### Pemilihan Model
Dalam pengembangan model untuk dataset ini, digunakan beberapa jenis algoritma regresi diantaranya:
1. Linear Regression
   Alasan Pemilihan: Linear Regression adalah model regresi yang sederhana dan mudah dipahami. Pemilihan model ini sebagai dasar atau pembanding awal untuk melihat sejauh mana performa model sederhana ini dalam memprediksi data.
   - Keunggulan:
      - Sederhana dan mudah diimplementasikan.
   - Kelemahan:
      - Terbatas dalam menangani hubungan yang kompleks dalam data.
      - Tidak efektif ketika hubungan antara variabel dependen dan independen tidak bersifat linier.

2. Decision Tree Regressor
   Alasan Pemilihan: Decision Tree Regressor adalah model non-linear yang dapat menangani hubungan yang lebih kompleks antara variabel dependen dan independen. Tujuan pemilihan model ini yaitu ingin melihat apakah model ini dapat memberikan prediksi yang lebih baik daripada Linear Regression.
   - Keunggulan:
      - Dapat menangani hubungan non-linear.
      - Mudah diinterpretasikan.
   - Kelemahan:
      - Rentan terhadap overfitting, terutama jika tidak diatur dengan baik.
      - Tidak stabil terhadap perubahan data kecil.

3. Random Forest Regressor
   Alasan Pemilihan: Random Forest Regressor adalah model ensemble yang dibangun di atas Decision Tree. Tujuan pemilihan model ini yaitu karena ensemble model cenderung mengurangi overfitting dan meningkatkan performa model regresi.
   - Keunggulan:
      - Dapat menangani hubungan non-linear.
      - Mengurangi overfitting dengan menggunakan banyak pohon keputusan.
      - Meningkatkan akurasi prediksi.
   - Kelemahan:
      - Kompleksitas model dan waktu pelatihan yang lebih lama.

### Fine-Tuning Model dan Parameter yang digunakan
Berikut adalah parameter-parameter yang biasanya diperlukan dalam fine-tuning untuk setiap algoritma yang telah disebutkan:
1. **Linear Regression**: Linear Regression adalah model yang cukup sederhana, dan parameter utamanya adalah koefisien (bobot) yang menentukan hubungan linier antara variabel independen dan dependen. Sehingga tidak memerlukan fine-tuning yang rumit untuk model ini.

2. **Decision Tree Regressor**: Decision Tree memiliki beberapa parameter penting, di antaranya:
   - `max_depth`: Ini adalah parameter yang mengatur kedalaman pohon. Sehingga dapat mengontrol kompleksitas model dengan mengatur nilai ini.
   - `min_samples_split`: Parameter ini menentukan jumlah sampel minimum yang diperlukan untuk membagi node dalam pohon.
   - `min_samples_leaf`: Parameter ini menentukan jumlah sampel minimum yang diperlukan untuk membentuk daun (leaf) dalam pohon.
   - `max_features`: Parameter ini mengatur jumlah fitur yang akan dipertimbangkan saat mencari pemisah terbaik.
     
   Setelah melakukan fine tunning didapatkan parameter terbaik yaitu:
   - `max_depth`: 7
   - `max_features`: 'auto'
   - `min_samples_leaf`: 10
   - `min_samples_split`: 2


3. **Random Forest Regressor**: Random Forest adalah ensemble model yang didasarkan pada Decision Trees, sehingga parameter Decision Tree juga berlaku di sini. Selain itu, ada beberapa parameter tambahan yang perlu dipertimbangkan:
   - `n_estimators`: Ini adalah jumlah pohon keputusan dalam ensemble.
   - `max_features`: Parameter ini mengatur jumlah fitur yang akan dipertimbangkan saat mencari pemisah terbaik dalam setiap pohon.
   - `bootstrap`: Jika diatur sebagai True, maka sampel bootstrap akan digunakan saat melatih setiap pohon.
  
   Setelah melakukan fine tunning didapatkan parameter terbaik yaitu:
   - `n_estimators`: 300
   -  `min_samples_split`: 5
   -  `min_samples_leaf`: 2
   -  `max_features`: 'auto'
   - `max_depth`: 5

Selama proses fine-tuning, nilai-nilai parameter ini dan memeriksa dampaknya pada kinerja model dapat dirubah. Perubahan dapat menggunakan metode cross-validation atau pengujian validasi untuk menentukan kombinasi parameter terbaik untuk setiap algoritma. Nilai-nilai optimal parameter akan bervariasi tergantung pada dataset dan masalah yang hadapi.

   

### Alasan Pemilihan Model
1. Linear Regression: Model ini mencoba untuk mencari hubungan linier antara variabel dependen dan independen. Ini melibatkan mencari koefisien regresi terbaik yang menggambarkan hubungan tersebut.

2. Decision Tree Regressor: Decision Tree adalah struktur pohon yang memecah data menjadi subset yang semakin kecil berdasarkan fitur-fitur yang ada. Tujuannya adalah untuk membagi data hingga mencapai daun pohon yang berisi nilai regresi.

3. Random Forest Regressor: Model ini adalah ensemble dari beberapa Decision Trees. Setiap pohon dalam ensemble memberikan prediksi, dan hasil akhirnya adalah rata-rata prediksi dari semua pohon. Ini mengurangi overfitting dan meningkatkan akurasi prediksi.

Dengan demikian, setelah pertimbangan lebih rinci ini, Random Forest Regressor dipilih sebagai model yang paling cocok untuk dataset ini, karena mampu menangani hubungan non-linear dan mengurangi risiko overfitting melalui ensemble dari Decision Trees. Meskipun tidak memberikan perubahan yang signifikan setelah fine-tuning, model ini memberikan performa yang paling baik dibandingkan dengan model lainnya.

## Evaluation
Metrik evaluasi yang digunakan pada proyek ini adalah akurasi dan mean squared error (MSE). Akurasi menentukan tingkat kemiripan antara hasil prediksi dengan nilai yang sebenarnya (y_test). Mean squared error (MSE) mengukur error dalam model statistik dengan cara menghitung rata-rata error dari kuadrat hasil aktual dikurang hasil prediksi.

![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/48eedf24-9d0f-4d8c-9482-011887e920ef)

- Berikut hasil evaluasi pada proyek
### Accuracy Model

   |   Model   |   Score   |
   |:---------:|:---------:|
   |    LR     |  0.677818 |
   |    DT     |  0.812010 |
   |    RF     |  0.822758 |

      

![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/55f64441-a1c1-4ce8-ad4f-4ab492b1ea3f)



### Mean Squared Error (MSE)
   | Model | MSE     |
   |-------|---------|
   | LR    | 0.384535|
   | DT    | 0.473679|
   | RF    | 0.436133|

   ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/dbf4e580-9291-496d-ab82-02536a938daf)

  
- Hasil evaluasi menunjukkan bahwa model dengan algoritma Random Forest memiliki akurasi yang lebih tinggi dan tingkat error yang lebih kecil dibandingkan algoritma lain dalam proyek ini. Ini menunjukkan bahwa Random Forest adalah pilihan yang efektif untuk memprediksi kualitas udara dengan tingkat ketepatan yang lebih baik, menjadikannya pilihan yang solid dalam proyek ini.
