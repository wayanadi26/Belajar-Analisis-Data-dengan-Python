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
Terdapat 2 fitur kategorik yang ada didalam dataset yaitu wd dan station, kedua fitur tersebut memiliki sebaran yang merata:
   ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/5c2518e2-0a82-490c-a06b-3fae647b8348)

## Data Preparation
Pada tahap ini saya melakukan loading data kemudian melakukan EDA dengan mengecek missing value, data duplicate, kemudian memperbaikinya, setelah itu melakukan Univariate analysis dengan membagi antara data numeric dengan data categoric.
### Data Loading
- Mengunduh dataset air quality kemudian disimpan ke Google Drive sebagai base directorynya
  ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/144ff674-7692-4ec5-b8ea-45e04b5def22)

### Exploratory Data Analysis (EDA)
- Mengecek informasi dataset
  ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/434815f7-7439-499f-92c7-9cf677611c60)
  Terdapat 11 kolom dengan tipe float64, 4 kolom int64, dan 2 kolom object
- Mengecek deskripsi data (mean, median, q1, q2, q3, std dan lain sebagianya
  ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/9774857c-4d69-4402-a08e-9394ddc5c17e)
- Cek duplicate data
  ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/72442243-fff9-4bc9-8f76-cd7c30e3dac4)
  Tidak ada data duplicate pada dataset
- Cek Missing Value
  ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/37fd9cc3-f04f-4482-bbda-91cdbefee7a7)
  Terlihat bahwa CO merupakan kolom dengan missing value paling banyak
- Memperbaiki missing data
  ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/97623979-686c-4460-86ce-29cb9bcda43f)
  Semua data sudah oke dan tidak ada missing value
- Drop kolom 'No' dan 'Station' karena kolom 'No' tidak relevan dengan dataset dan karena station yang dipake cuma satu station.
  ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/cde536d9-6bb9-412b-b872-98a35aeb8cf3)
- Univariate data (Memisahkan data numerical dengan data categorical)
  ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/97508cc1-a4d6-44ff-a980-2fbf749c4444)
- Cek categorical feature
  ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/3de3502c-5c55-43b6-99d1-fa0b70fdffe9)
  ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/f7e6f644-1041-4f18-ba65-4b36a4c2bf46)

- Cek Numerical features
  ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/5c480228-82a6-4ad3-8b81-1f58efc14dc3)
  ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/b092eb03-1f91-42b0-8681-bfc9b66bf927)

- Dilihat dari analisis visualisasi di atas, dapat disimpulkan bahwa wd, date, year, month, day, hour tidak berkorelasi dengan baik sehingga bisa di drop
  ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/66b6f0d1-2f6f-46df-9988-064ce01a67bc)

## Modeling
### Train Test Split
Sebelum melakukan proses modeling pertama kita harus membagi dataset menjadi dataset train dan dataset test dengan perbandoingan 80%:20%
![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/5e91ca28-9eb1-44e8-81e2-883006c9175b)

### Pemilihan model
1. Model pertama yang digunakan adalah Linear Regression
   ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/7b258094-bcb2-4201-ac57-17a540cb911d)
   Pada model ini akurasi train dan test sangat rendah karena hanya 68%
2. Decision Tree Regressor
   ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/ec58a215-f3d0-4070-98bd-132eb7ca21d5)
   - Model ini menghasilkan nilai prediksi yang lumayan bagus yakni diangka 82%
   - Setelah dilakukan fine tunning akusrasi model tidak terlalu memberikan perubahan yang signifikan
     ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/6410efc1-e006-4826-93e5-ec32a427fb1b)

3. Random Forest Regressor
   ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/bbe50eff-d1c1-4baf-a418-cb2f9ac01bdc)
   - Model ini menghasilkan nilai prediksi yang lumayan bagus yakni diangka 84%
   - Setelah dilakukan fine tunning akusrasi model tidak terlalu memberikan perubahan yang signifikan
     ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/fb2655e5-5326-4389-9b0c-6ea3496059af)
     
Dari ketiga model yang digunakan maka, model yang dipakai dalah model Random Forest Regressor.


## Evaluation
Metrik evaluasi yang digunakan pada proyek ini adalah akurasi dan mean squared error (MSE).
![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/48eedf24-9d0f-4d8c-9482-011887e920ef)

- Berikut hasil evaluasi pada proyek
  - Accuracy
    ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/00d11cd7-e309-4f20-b676-d2034dc99622)
  - MSE
    ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/dbf4e580-9291-496d-ab82-02536a938daf)

  
- Hasil evaluasi menunjukkan bahwa model dengan algoritma Random Forest memiliki akurasi yang lebih tinggi dan tingkat error yang lebih kecil dibandingkan algoritma lain dalam proyek ini. Ini menunjukkan bahwa Random Forest adalah pilihan yang efektif untuk memprediksi kualitas udara dengan tingkat ketepatan yang lebih baik, menjadikannya pilihan yang solid dalam proyek ini.
