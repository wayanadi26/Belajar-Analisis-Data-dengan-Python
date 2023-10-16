# Laporan Proyek Machine Learning - I Wayan Adi Saputra

## Domain Proyek

### Domain : Lingkungan / Udara
### Latar belakang
Pencemaran udara dapat memiliki dampak serius terhadap kesehatan manusia, seperti penyakit pernapasan dan penyakit jantung. Oleh karena itu, pemahaman dan prediksi kualitas udara menjadi kunci dalam mengidentifikasi ancaman potensial dan mengambil langkah-langkah pencegahan yang tepat. Selain itu, perubahan iklim global telah mempengaruhi pola pencemaran udara, membuat analisis prediksi semakin penting dalam menghadapi perubahan lingkungan yang cepat. Teknologi sensor dan Internet of Things (IoT) telah membantu dalam pengumpulan data kualitas udara yang lebih akurat dan real-time, memungkinkan pemantauan dan respons yang lebih efektif terhadap pencemaran udara.
Prediksi kualitas udara juga memberikan manfaat kepada masyarakat dengan memberikan informasi yang tepat waktu dan akurat. Ini memungkinkan individu untuk mengambil tindakan preventif, seperti menghindari daerah dengan tingkat pencemaran tinggi saat kualitas udara sedang buruk. Dengan demikian, analisis prediksi kualitas udara bukan hanya alat penting dalam manajemen lingkungan, tetapi juga merupakan alat penting dalam melibatkan dan memberdayakan masyarakat untuk melindungi kesehatan mereka sendiri.

## Business Understanding
Proyek ini dibangun untuk membantu pemangku kepentingan dalam menangani permasalahan polusi udara:
1. Pemerintah, dengan adanya predictive analytics terkait kualitas udara maka pemerintah dapat memberikan solusi preventive untuk menanganinya.
2. Masyarakat, masyarakat dapat lebih mempersiapkan diri dengan baik apabila kualitas udara semakin memburuk.
   
### Problem Statements
1. Parameter apakah yang paling berkaitan dengan tingkat kualitas udara?
2. Bagaimana rata-rata pergerakan arah angin yang mempengaruhi kualitas udara?
3. Bagaimana model yang paling tepat untuk memprediksi kualitas udara?

### Goals
Adapun Goals dari proyek ini yaitu:
1. Mengetahui parameter yang paling berpengaruh terhadap kualitas udara, mengetahui arah pergerakan angin yang mempengaruhi kualitas udara, membuat model yang paling bagus untuk memprediksi kualitas udara.
2. Dapat memberikan saran tindakan preventive kepada pemerintah terkait bagaimana menangani permasalahan kualitas udara yang buruk.

Semua poin di atas harus diuraikan dengan jelas. Anda bebas menuliskan berapa pernyataan masalah dan juga goals yang diinginkan.

### Solution statements
1. Menganalisis data dengan melakukan univariate analysis dan multivariate analysis, membuat visualisasi, mengetahui kolerasi antar fitur dan mendeteksi outlier.
2. Menyiapkan data agar bisa digunakan dalam membangun model.
3. Melakukan hyperparameter tuning menggunakan grid search dan membangun model regresi yang dapat memprediksi bilangan kontinu. ALgoritma yang dipakai dalam proyek ini adalah Linear Regression, Decision Tree, dan Random Forest.

## Data Understanding
Dataset yang digunakan meruapakan dataset kualitas udara di kota Changping, sumber data yaitu: https://drive.google.com/file/d/1RhU3gJlkteaAQfyn9XOVAz7a5o1-etgr/view
Informasi dataset:
- Dataset berformat csv
- Dataset memiliki 35064 sample dengan 18 fitur.
- Dataset memiliki 11 fitur bertipe data float64, 5 fitur bertipe data int64, dan 2 fitur bertipe data object.
- Terdapat beberapa missing value dalam dataset. 
  ![image](https://github.com/wayanadi26/Belajar-Analisis-Data-dengan-Python/assets/88713651/e20e09c0-97fa-42be-ad25-d661a02ae169)

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
