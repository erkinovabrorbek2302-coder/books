from django.http import HttpResponse
from .models import Post
from django.shortcuts import render, redirect

CSS = """
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', 'Georgia', serif; }

  /* ORQA FON: OQ VA KITOB VARAGLARI TUSHADI */
  body {
      background-color: #ffffff;
      min-height: 100vh;
      position: relative;
      overflow-x: hidden;
  }

  /* TEPADAN PASTGA TUSHUVCHI KITOB VARAGLARI (ANIMATSIYA) */
  .falling-book {
      position: absolute;
      top: -100px;
      color: #e0e0e0; /* Och kulrang shaffof varaqlar */
      font-size: 2.5rem;
      opacity: 0.6;
      animation: fall linear infinite;
      pointer-events: none; /* Tugmalarni bosishga xalaqit bermaydi */
      z-index: 0;
  }

  /* Har bir varaqning tushish tezligi va o'lchami har xil bo'lsin */
  .falling-book:nth-child(1) { left: 10%; animation-duration: 8s; animation-delay: 0s; font-size: 2rem; }
  .falling-book:nth-child(2) { left: 20%; animation-duration: 11s; animation-delay: 2s; font-size: 1.5rem; }
  .falling-book:nth-child(3) { left: 30%; animation-duration: 9s; animation-delay: 4s; font-size: 3rem; }
  .falling-book:nth-child(4) { left: 40%; animation-duration: 12s; animation-delay: 1s; font-size: 2.2rem; }
  .falling-book:nth-child(5) { left: 50%; animation-duration: 7s; animation-delay: 3s; font-size: 1.8rem; }
  .falling-book:nth-child(6) { left: 60%; animation-duration: 10s; animation-delay: 5s; font-size: 2.8rem; }
  .falling-book:nth-child(7) { left: 70%; animation-duration: 8.5s; animation-delay: 2.5s; font-size: 1.5rem; }
  .falling-book:nth-child(8) { left: 80%; animation-duration: 9.5s; animation-delay: 0.5s; font-size: 2rem; }
  .falling-book:nth-child(9) { left: 90%; animation-duration: 11.5s; animation-delay: 4.5s; font-size: 2.4rem; }

  @keyframes fall {
      0% { transform: translateY(-100px) rotate(0deg); opacity: 0.7; }
      100% { transform: translateY(110vh) rotate(360deg); opacity: 0; }
  }

  /* SAHIFA ELEMENTLARI (Fondan yuqorida turishi uchun z-index: 1) */
  h1 {
      font-size: 3.5rem;
      color: #2c3e50;
      text-align: center;
      padding: 40px 20px 10px;
      border-bottom: 3px solid #e74c3c;
      position: relative;
      z-index: 1;
      font-family: 'Georgia', serif;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.05);
  }

  h2 {
      text-align: center;
      color: #34495e;
      padding: 15px;
      font-size: 1.4rem;
      position: relative;
      z-index: 1;
      font-weight: 300;
  }

  /* TUGMALAR (ZAMONAVIY, CHIROYLI) */
  a {
      display: inline-block;
      color: #ffffff;
      text-decoration: none;
      padding: 15px 30px;
      margin: 10px 20px;
      border-radius: 50px;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); /* Chiroyli gradient */
      box-shadow: 0 4px 15px rgba(118, 75, 162, 0.4);
      transition: all 0.3s ease;
      font-size: 1.1rem;
      position: relative;
      z-index: 1;
      font-weight: 600;
      letter-spacing: 0.5px;
  }

  a:hover {
      transform: translateY(-5px);
      box-shadow: 0 8px 25px rgba(118, 75, 162, 0.6);
      background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
  }

  /* KONTEYNERLAR */
  .container {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 30px;
      width: 90%;
      max-width: 1200px;
      margin: 30px auto;
      padding: 0 20px;
      position: relative;
      z-index: 1;
  }

  .col { display: grid; grid-template-columns: 1fr; gap: 20px; justify-items: center; }

  /* SAHIFA TEPASIGA QAYTISH TUGMASI */
  #topBtn {
      display: none;
      position: fixed;
      bottom: 50px;
      right: 30px;
      background: #764ba2;
      color: white;
      border: none;
      padding: 15px 20px;
      border-radius: 50%;
      font-size: 1.5rem;
      cursor: pointer;
      transition: all 0.3s;
      z-index: 999;
      box-shadow: 0 4px 10px rgba(0,0,0,0.2);
  }
  #topBtn:hover { background: #667eea; transform: scale(1.1); }

  body { animation: fadeIn 0.8s ease; }
  @keyframes fadeIn { from { opacity: 0; transform: translateY(15px); } to { opacity: 1; transform: translateY(0); } }
</style>

<!-- TEPADAN PASTGA TUSHUVCHI KITOB VARAGLARI (HTML ELEMENTLARI) -->
<div class="falling-book">📖</div>
<div class="falling-book">📄</div>
<div class="falling-book">📖</div>
<div class="falling-book">📄</div>
<div class="falling-book">📚</div>
<div class="falling-book">📖</div>
<div class="falling-book">📄</div>
<div class="falling-book">📚</div>

<button id="topBtn" onclick="window.scrollTo({top:0,behavior:'smooth'})">↑</button>

<script>
  window.onscroll = function() {
    document.getElementById('topBtn').style.display = window.scrollY > 200 ? 'block' : 'none';
  };
</script>
"""

def first_view(request):
    html = CSS + """
    <h1>📚 Kitoblar Dunyosi</h1>
    <h2>Asosiy bo'lim:</h2>

    <div class="container">
        <!-- CHAP TOMON -->
        <div class="col">
            <div><a class="book-link" href="/pages/O'tgan Kunlar"> O'tgan Kunlar  </a></div>
            <div><a class="book-link" href="/pages/Mehrobdan Chayon"> Mehrobdan Chayon  </a></div>
            <div><a class="book-link" href="/pages/Kecha va Kunduz"> Kecha va Kunduz  </a></div>
            <div><a class="book-link" href="/pages/Alkimyogar"> Alkimyogar  </a></div>
            <div><a class="book-link" href="/pages/Kichkina Shahzoda"> Kichkina Shahzoda  </a></div>
        </div>

        <!-- O'NG TOMON -->
        <div class="col">
            <div><a class="book-link" href="/pages/Urush va Tinchlik"> Urush va Tinchlik  </a></div>
            <div><a class="book-link" href="/pages/Jinoyat va Jazo"> Jinoyat va Jazo  </a></div>
            <div><a class="book-link" href="/pages/Anna Karenina"> Anna Karenina  </a></div>
            <div><a class="book-link" href="/pages/1984"> 1984  </a></div>
            <div><a class="book-link" href="/pages/Hayvonlar Fermasi"> Hayvonlar Fermasi  </a></div>
        </div>
    </div>
    """
    return HttpResponse(html)
def pages(request, page):
    if page == "O'tgan Kunlar":
        html = CSS + f"""
        <h1>{page}</h1>
<img src="https://backend.book.uz/user-api/img/img-file-5ae6f33d4f57dd353bcc444c84bb326f.jpg" height="600" width="500">
<p>
"O'tkan Kunlar" o‘zbek adabiyotidagi birinchi yirik romanlardan biridir.
Asar muallifi Abdulla Qodiriy hisoblanadi.
Roman 1920-yillarda yozilgan.
Asarda XIX asr oxiridagi Turkiston hayoti tasvirlangan.
Bosh qahramonlar Otabek va Kumushdir.
Otabek zamonaviy fikrlaydigan, bilimli yigit sifatida gavdalantirilgan.
Kumush esa aqlli, odobli va mehribon qiz sifatida tasvirlanadi.
Asarda sevgi, oila va jamiyat muammolari yoritilgan.
Roman o‘quvchilarni yaxshilik, halollik va vatanparvarlikka undaydi.
"O'tkan Kunlar" bugungi kunda ham eng ko‘p o‘qiladigan o‘zbek asarlaridan biridir.</p>
         <a href="/books/"> << back page </a><br><br>
         <a href="Mehrobdan Chayon"> << after page "Mehrobdan Chayon">>> </a>
        """
    elif page == "Mehrobdan Chayon":
        html = CSS + f"""
        <h1>{page}</h1>
<img src="https://backend.book.uz/user-api/img/img-file-dc54b4409d69abd2e1c000149a9c831d.jpg" height="600" width="500">
<p>"Mehrobdan Chayon" mashhur o‘zbek yozuvchisi Abdulla Qodiriy tomonidan yozilgan romandir.
Asar tarixiy va ijtimoiy mavzularni o‘z ichiga oladi.
Roman voqealari Qo‘qon xonligi davrida kechadi.
Bosh qahramon Anvar ismli bilimli va halol yigitdir.
Anvar adolat va haqiqat uchun kurashadi.
Asarda mansabparastlik va adolatsizlik qattiq tanqid qilinadi.
Ra'no obrazi ham asarning muhim qahramonlaridan biridir.
Roman orqali o‘sha davrdagi xalq hayoti va muammolari yoritilgan.
Asar o‘quvchini halollik, mardlik va vatanparvarlik ruhida tarbiyalaydi.
"Mehrobdan Chayon" o‘zbek adabiyotining eng qimmatli romanlaridan biri hisoblanadi.</p>
        <a href="/books/"> << main page </a><br><br>
        <a href="Kecha va Kunduz"> << after page "Kecha va Kunduz">>> </a>
        """
    elif page == "Kecha va Kunduz":
        html = CSS + f"""
                <h1>{page}</h1>
<img src="https://assets.asaxiy.uz/product/items/desktop/3e731bbc1abcad562742e6083c228ae72023052514252353291KpOEd1dtey.jpg.webp" height="600" width="500">
        <p>"Kecha va Kunduz" mashhur o‘zbek adibi Cho'lpon tomonidan yozilgan romandir.
Asar o‘zbek adabiyotining eng muhim romanlaridan biri hisoblanadi.
Unda XX asr boshlaridagi Turkiston hayoti tasvirlangan.
Roman orqali xalqning og‘ir turmushi va jamiyatdagi muammolar yoritiladi.
Asarda eski va yangi qarashlar o‘rtasidagi kurash aks ettirilgan.
Qahramonlarning taqdiri orqali davrning murakkab hayoti ko‘rsatiladi.
Muallif inson erkinligi va adolat masalalariga alohida e’tibor qaratgan.
Asar sodda va ta’sirchan tilda yozilgan.
"Kecha va Kunduz" o‘quvchini fikrlashga va xulosa chiqarishga undaydi.
Bu roman o‘zbek adabiyotining nodir durdonalaridan biri sanaladi.</p>
<a href="/books/"> << main page </a><br><br>
<a href="Alkimyogar"> << after page "Alkimyogar">>> </a>
"""
    elif page == "Alkimyogar":
        html = CSS + f"""
                        <h1>{page}</h1>
<img src="https://backend.book.uz/user-api/img/img-file-763edfd59cde36baa8f93af002f20e34.jpg" height="600" width="500">

                <p>"Alkimyogar" braziliyalik yozuvchi Paulo Coelho tomonidan yozilgan mashhur romandir.
Asarning bosh qahramoni Santyago ismli yosh cho‘pondir.
U tushida ko‘rgan xazinani topish uchun uzoq safarga chiqadi.
Sayohat davomida Santyago ko‘plab insonlar bilan uchrashadi.
U har bir uchrashuvdan muhim hayotiy saboqlar oladi.
Asarda insonning orzulariga ishonishi va ularga intilishi targ‘ib qilinadi.
Kitobda taqdir, baxt va o‘z imkoniyatlarini anglash mavzulari yoritilgan.
Muallif ramziy obrazlar orqali chuqur falsafiy fikrlarni bayon qiladi.
"Alkimyogar" dunyoning ko‘plab tillariga tarjima qilingan va millionlab nusxada sotilgan.
Bu asar o‘quvchini o‘z maqsadlari sari qat’iyat bilan harakat qilishga undaydi.</p>
        <a href="/books/"> << main page </a><br><br>
        <a href="Kichkina Shahzoda"> << after page "Kichkina Shahzoda">>> </a>
"""
    elif page == "Kichkina Shahzoda":
        html = CSS + f"""
        <h1>{page}</h1>
<img src="https://backend.book.uz/user-api/img/img-file-ca39b9e64de676b31178a67d9141b808.jpg" height="600" width="500">

    <p>"Kichkina Shahzoda" fransuz yozuvchisi Antoine de Saint-Exupéry tomonidan yozilgan mashhur asardir.
Kitob ilk bor 1943-yilda nashr etilgan.
Asarning bosh qahramoni Kichkina Shahzoda ismli bola hisoblanadi.
U o‘z sayyorasidan chiqib, turli sayyoralarga sayohat qiladi.
Sayohat davomida u turli xarakterdagi insonlar bilan uchrashadi.
Asarda do‘stlik, mehr-muhabbat va sadoqat mavzulari yoritilgan.
Tulki obrazi orqali muhim hayotiy saboqlar beriladi.
Kitob bolalar uchun yozilgandek tuyulsa-da, kattalar uchun ham chuqur ma’noga ega.
Asar dunyoning yuzlab tillariga tarjima qilingan.
"Kichkina Shahzoda" jahon adabiyotining eng sevimli va mashhur asarlaridan biri hisoblanadi.</p>
                <a href="/books/"> << main page </a><br><br>
                <a href="Urush va Tinchlik"> << after page "Urush va Tinchlik">>> </a>
"""
    elif page == "Urush va Tinchlik":
        html = CSS + f"""
            <h1>{page}</h1>
<img src="https://backend.book.uz/user-api/img/img-18b1aba12eefafd4f6f4e36a144acc2b.jpg" height="600" width="500">

        <p>"Urush va Tinchlik" rus yozuvchisi Leo Tolstoy tomonidan yozilgan mashhur romandir.
Asar 19-asr boshlaridagi Rossiya hayotini tasvirlaydi.
Unda Napoleon urushlari davridagi voqealar asosiy o‘rinda turadi.
Roman bir nechta aristokrat oilalarning hayoti orqali hikoya qilinadi.
Bosh qahramonlar orasida Andrey Bolkonskiy va Per Bezuxov bor.
Asarda urushning inson hayotiga ta’siri chuqur yoritilgan.
Shuningdek, tinchlik davridagi jamiyat hayoti ham tasvirlanadi.
Muallif falsafiy fikrlar orqali taqdir va erkinlik mavzusini ochib beradi.
Asar juda keng ko‘lamli va ko‘p personajli roman hisoblanadi.
"Urush va Tinchlik" jahon adabiyotining eng buyuk asarlaridan biri sanaladi.</p>
                    <a href="/books/"> << main page </a><br><br>
                    <a href="Jinoyat va Jazo"> << after page "Jinoyat va Jazo">>> </a>
"""
    elif page == "Jinoyat va Jazo":
        html = CSS + f"""
        <h1>{page}</h1>
<img src="https://imgv2-2-f.scribdassets.com/img/document/795862600/original/0b689c7104/1?v=1" height="600" width="500">

            <p>"Jinoyat va Jazo" rus yozuvchisi Fyodor Dostoyevskiy tomonidan yozilgan mashhur romandir.
Asar 1866-yilda nashr etilgan.
Bosh qahramon Rodion Raskolnikov ismli kambag‘al talabadir.
U o‘zining g‘oyalarini sinash uchun og‘ir jinoyat sodir etadi.
Jinoyatdan keyin u kuchli ruhiy azob va vijdon qiynog‘ini boshdan kechiradi.
Asarda inson psixologiyasi juda chuqur tahlil qilingan.
Muallif yaxshilik va yomonlik o‘rtasidagi kurashni ko‘rsatadi.
Roman davomida Raskolnikov asta-sekin o‘z xatosini anglaydi.
Asar jamiyat, axloq va e’tiqod mavzularini ham yoritadi.
"Jinoyat va Jazo" jahon adabiyotining eng muhim psixologik romanlaridan biridir.</p>
           <a href="/books/"> << main page </a><br><br>
           <a href="Anna Karenina"> << after page "Anna Karenina">>> </a>
"""
    elif page == "Anna Karenina":
        html = CSS + f"""
            <h1>{page}</h1>
<img src="https://www.thegreatbritishbookshop.co.uk/cdn/shop/files/9786256629660_1200x.jpg?v=1728561314" height="600" width="500">

    <p>"Anna Karenina" rus yozuvchisi Leo Tolstoy tomonidan yozilgan mashhur romandir.
Asar 1870-yillarda yozilgan va jahon adabiyotining klassikasi hisoblanadi.
Roman markazida Anna Karenina ismli ayolning hayoti turadi.
U sevgi va jamiyat qoidalari o‘rtasidagi murakkab tanlovga duch keladi.
Asarda Anna va Vronskiy o‘rtasidagi munosabatlar asosiy voqeani tashkil qiladi.
Parallel ravishda Levin obrazining hayoti ham tasvirlanadi.
Muallif oila, sevgi va axloqiy qadriyatlarni chuqur tahlil qiladi.
Roman jamiyatdagi ikkiyuzlamachilik va ijtimoiy bosimni ko‘rsatadi.
Asar psixologik va falsafiy jihatdan juda boy hisoblanadi.
"Anna Karenina" jahon adabiyotining eng buyuk romanlaridan biri sanaladi.</p>
          <a href="/books/"> << main page </a><br><br>
          <a href="1984"> << after page "1984">>> </a>
"""
    elif page == "1984":
        html = CSS + f"""
                    <h1>{page}</h1>
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3OIMH5ATH_V1hT3ut7kkqM2NgxHW_7bFbZA&s" height="600" width="500">

            <p>"1984" ingliz yozuvchisi George Orwell tomonidan yozilgan mashhur distopik romandir.
Asar 1949-yilda nashr etilgan.
Roman totalitar jamiyat tasviriga asoslangan.
Bosh qahramon Winston Smith ismli oddiy xodimdir.
U yashaydigan davlatda hukumat hamma narsani to‘liq nazorat qiladi.
Asarda “Katta Birodar” (Big Brother) obrazi orqali nazorat tizimi ko‘rsatiladi.
Insonlarning fikrlashi va erkinligi keskin cheklangan jamiyat tasvirlanadi.
Winston tizimga qarshi ichki isyon his qiladi.
Roman erkinlik, qo‘rquv va propaganda mavzularini chuqur ochib beradi.
"1984" bugungi kunda ham siyosiy va ijtimoiy jihatdan dolzarb asar hisoblanadi.</p>
        <a href="/books/"> << main page </a><br><br>
        <a href="Hayvonlar Fermasi"> << after page "Hayvonlar Fermasi">>> </a>
"""
    elif page == "Hayvonlar Fermasi":
        html = CSS + f"""
    <h1>{page}</h1>
<img src="https://data.daryo.uz/media/2019/07/3-51.jpg" height="600" width="500">

<p>"Hayvonlar Fermasi" ingliz yozuvchisi George Orwell tomonidan yozilgan mashhur allegorik qissadir.
Asar 1945-yilda nashr etilgan.
Hikoya fermadagi hayvonlarning insonlarga qarshi qo‘zg‘oloni bilan boshlanadi.
Hayvonlar adolatli jamiyat quramiz deb fermani egallab olishadi.
Boshida hamma teng va erkin yashaydi.
Keyinchalik cho‘chqalar hokimiyatni qo‘lga olib, boshqalarni boshqarishni boshlaydi.
Asarda hokimiyatning buzilishi va adolatsizlik asta-sekin kuchayib boradi.
Hikoya orqali siyosiy tuzumlar va diktatura tanqid qilinadi.
Mashhur ibora “Barcha hayvonlar teng, lekin ba’zilari tengroq” asarda muhim o‘rin tutadi.
"Hayvonlar Fermasi" jahon adabiyotida kuchli siyosiy ma’noga ega asarlardan biri hisoblanadi.</p>
            <a href="/books/"> << main page </a><br><br>
            <a href="O'tgan Kunlar"> << after page "O'tgan Kunlar">>> </a>
"""
    else:
        html = CSS + f"""
        <h1>{page}</h1>
        """
    return HttpResponse(html)
