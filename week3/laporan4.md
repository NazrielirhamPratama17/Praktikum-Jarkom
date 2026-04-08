# Modul 4 (DNS)
Domain Name System (DNS) merupakan komponen penting dalam infrastruktur internet yang berfungsi mengubah nama host menjadi alamat IP. Pada modul ini, fokus pembahasan akan diarahkan pada sisi klien DNS. Perlu dipahami bahwa peran klien dalam sistem DNS cukup sederhana, yaitu hanya mengirimkan permintaan ke server DNS lokal dan kemudian menerima jawaban yang diberikan.

## Modul 4.2 Nslookup
nslookup merupakan sebuah perintah atau alat yang digunakan untuk memperoleh serta menampilkan informasi yang berkaitan dengan Domain Name System (DNS). Tool ini dapat digunakan untuk mengetahui alamat IP dari suatu domain maupun sebaliknya, sehingga sangat membantu dalam proses pengecekan jaringan serta analisis atau troubleshooting koneksi.

## Langkah - Langkah percobaan
1. Jalankan Command Prompt (cmd) pada perangkat yang digunakan, kemudian masukkan perintah "nslookup www.mit.edu
" dan tekan ENTER. Perintah ini digunakan untuk mengetahui alamat IP dari domain tersebut.
<img width="720" height="564" alt="nslookup" src="https://github.com/user-attachments/assets/7fbc125f-f295-4ef4-8744-acdfa2bb108c" />



2. Buka Command Prompt (cmd), lalu ketik perintah "nslookup -type=NS mit.edu" dan tekan ENTER. Perintah ini digunakan untuk menampilkan daftar Name Server (NS) yang menangani domain tersebut.
![tampilan](../Praktikum-Jarkom/assets/image/nslookup%20type%20NS.png)

3. Buka Command Prompt (cmd), kemudian ketik perintah "nslookup www.aiit.or.kr
 bitsy.mit.edu" dan tekan ENTER. Perintah ini digunakan untuk meminta informasi alamat IP domain www.aiit.or.kr
 dengan menggunakan server DNS bitsy.mit.edu sebagai sumber pencarian.
![tampilan](../Praktikum-Jarkom/assets/image/nslookup%20aiit%20bitsy.png)

## Pertanyaan
1. Mencari IP server web di Asia  
