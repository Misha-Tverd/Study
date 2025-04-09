# import requests

# API_KEY = "8b8362b872300e3c8f85e7875ad896dc"
# CATEGORY = "technology"  # Можна змінити на technology, science тощо
# LANG = "uk"  # Англійська 'en', українська 'uk' (GNews підтримує!)
# COUNTRY = "ua"  # Українські новини

# URL = f"https://gnews.io/api/v4/top-headlines?category={CATEGORY}&lang={LANG}&country={COUNTRY}&max=10&apikey={API_KEY}"

# response = requests.get(URL)
# data = response.json()



# articles = {'totalArticles': 29189, 
#             'articles': 
#                 [{'title': 'Експертка з ядерної енергетики пояснила, що залишиться від Запорізької АЕС після деокупації', 
#                   'description': 'Росіяни розграбували ЧАЕС, коли тікали звідти, так вони й вчинять, залишаючи ЗАЕС – найбільший ядерний об’єкт на європейському континенті', 
#                   'content': 'Росіяни розграбували ЧАЕС, коли тікали звідти, так вони й вчинять, залишаючи ЗАЕС – найбільший ядерний об’єкт на європейському континенті\nОкупанти вдадуться до мародерства під час відступу з Запорізької атомної електростанції. Про це заявила експертк... [1628 chars]', 'url': 'https://glavcom.ua/country/incidents/ekspertka-z-jadernoji-enerhetiki-pojasnila-shcho-zalishitsja-vid-zaporizkoji-aes-pislja-deokupatsiji-1047972.html', 'image': 'https://glavcom.ua/img/article/10479/72_main-v1741189567.webp', 'publishedAt': '2025-03-05T15:46:06Z', 'source': {'name': 'ГЛАВКОМ', 'url': 'https://glavcom.ua'}}, {'title': 'Мережа криптошахраїв, яка виманила 240 млн доларів у людей з усього світу, працювала також і з України', 'description': 'Розслідувачі з’ясували, що, ймовірно, керують цією структурою з Ізраїлю', 'content': 'Дві міжнародні мережі колл-центрів під виглядом інвестицій у криптовалюту упродовж чотирьох років, з 2021-го по 2025-й, виманили у понад 30 тисяч людей по всьому світу понад 275 мільйонів доларів. Одна з цих мереж працювала, у тому числі, з України т... [1965 chars]', 'url': 'https://www.radiosvoboda.org/a/news-skhemy-scam-empire-kryptoshakhrayi/33337315.html', 'image': 'https://gdb.rferl.org/a170e1f9-1a80-4e50-d2c4-08dd5af7d4b6_cx0_cy6_cw0_w1200_r1.jpg', 'publishedAt': '2025-03-05T14:17:15Z', 'source': {'name': 'Радіо Свобода', 'url': 'https://www.radiosvoboda.org'}}, {'title': 'Війська НАТО не готові до сучасної війни', 'description': 'Використання бойових дронів в Україні перевернуло усталені доктрини війни. Який досвід мають перейняти війська НАТО ᐅTSN.ua (новини 1+1).', 'content': 'Альянс має визнати перевагу безпілотних систем. 
# Вони дозволяють не тільки економити кошти, а й зберігають життя солдатів.\nЗбройні сили НАТО не готові вести сучасну війну з використанням великої кількості безпілотників.\nТаку думку висловив полковник В... [3196 chars]', 'url': 'https://tsn.ua/ato/viyska-nato-ne-gotovi-do-suchasnoyi-viyni-yak-droni-zminili-stari-doktrini-2780922.html', 'image': 'https://img.tsn.ua/cached/445/tsn-135859377404ec64163c97d964721c31/thumbs/1200x630/28/58/cf09b82d3f177b7099f5489810125828.png', 'publishedAt': '2025-03-05T14:12:43Z', 'source': {'name': 'ТСН', 'url': 'https://tsn.ua'}}, {'title': 'Український виробник бойових БпЛА створив найшвидший FPV-дрон в Україні', 'description': 'Український виробник бойових FPV-дронів "Дикі Шершні" представив новий безпілотник "Перевертень": він має можливість ...➜ читайте далі на Rubryka.com', 'content': 'Український виробник бойових БпЛА створив найшвидший FPV-дрон в Україні\nФото: Х / "Дикі шершні"\nУкраїнський виробник бойових FPV-дронів "Дикі Шершні" представив новий безпілотник "Перевертень": він має можливість розганятися до 200 кілометрів на годи... [1622 chars]', 'url': 'https://rubryka.com/2025/03/05/dron-pereverten/', 'image': 'https://rubryka.com/wp-content/uploads/ogimages/ua_734928_1741175044dron-pereverten.jpg', 'publishedAt': '2025-03-05T11:43:00Z', 'source': {'name': 'Рубрика', 'url': 'https://rubryka.com'}}, {'title': '2 криптовалюти, що можуть досягти $5 млрд капіталізації у березні', 'description': 'З поверненням ліквідності на ринок можна виділити дві криптовалюти, як такі, що можуть досягти ринкової капіталізації в $5 млрд', 'content': 'Біткоїн (BTC) відновився після розпродажу, спричиненого оголошенням Дональда Трампа про запровадження 25% тарифів на імпорт з Канади та Мексики до США. Цей спад знищив $460 млрд із загальної капіталізації крипторинку, спричинив ліквідацію $985 млн і ... [2990 chars]', 'url': 'https://psm7.com/uk/cryptocurrency/2-kryptovalyuty-shho-mozhut-dosyagty-5-mlrd-kapitalizacziyi-u-berezni.html', 'image': 'https://psm7.com/wp-content/uploads/2025/03/market_capitalization_image_1280x700-720x394.webp', 'publishedAt': '2025-03-05T11:40:00Z', 'source': {'name': 'PaySpace Magazine', 'url': 'https://psm7.com'}}, {'title': 'Суд відхилив вимогу Ілона Маска зупинити комерціалізацію OpenAI - деталі', 'description': 'Суд США відхилив вимогу Ілона Маска про негайне призупинення комерціалізації OpenAI. Остаточне рішення, за словами судді, буде ухвалене восени 2025 року.', 'content': 'Ілон Маск. Фото: Evelyn Hockstein/REUTERS\nУ вівторок, 4 березня, окружний суддя США відхилила прохання Ілона Маска про судову заборону, яка б негайно призупинила перетворення компанії OpenAI на комерційну організацію. Натомість заява Маска про заборо... [2771 chars]', 'url': 'https://novyny.live/tehnologii/ilon-mask-prograv-pershii-etap-sudu-proti-openai-shcho-vidomo-237932.html', 'image': 'https://novyny.live/cdn-cgi/imagedelivery/4_JwVYxosZqzJ7gIDJgTLA/0ae9d3f6-0d32-4485-abee-726334a82800/16x9', 'publishedAt': '2025-03-05T10:33:00Z', 'source': {'name': 'Новини Live', 'url': 'https://novyny.live'}}, {'title': 'iPhone 17 Pro проти iPhone 16 Pro: 4 основні причини для оновлення', 'description': 'iPhone 17 Pro проти iPhone 16 Pro: 4 основні причини для оновлення.Останні новини Смартфони на сайті - iTechua. Свіжа стрічка новин сьогодні.', 'content': 'Час читання: 2 хв.\nНезважаючи на новий 5-кратний телеоб’єктив та інтеграцію Apple Intelligence, iPhone 16 Pro став швидше еволюційним оновленням, ніж революційним. Це все ще один із кращих смартфонів на ринку, але власникам iPhone 15 Pro навряд чи ва... [1700 chars]', 'url': 'https://itechua.com/smartphones/278095', 'image': 'https://itechua.com/wp-content/uploads/2025/03/Screenshot_9.jpg', 'publishedAt': '2025-03-05T10:23:33Z', 'source': {'name': 'iTechua - новини, гаджети, технології', 'url': 'https://itechua.com'}}, {'title': 'Використовуйте Google Gemini на максимум - 5 функцій, які варто спробувати', 'description': 'Google Gemini — це потужний штучний інтелект, який може зробити ваше життя простішим. Чатбот допоможе знаходити потрібну інформацію, аналізувати зображення, підсумовувати відео з YouTube, планувати подорожі та взаємодіяти з додатками Google.', 'content': 'Google Gemini Live на екрані смартфона. Фото: скриншот/YouTube\nGoogle Gemini має потужні функції штучного інтелекту, які можуть значно покращити життя кожного користувача. Чатбот може надавати рекомендації щодо покупок, узагальнювати відео з YouTube ... [3629 chars]', 'url': 'https://novyny.live/tehnologii/piat-naikrashchikh-funktsii-google-gemini-iaki-vam-tochno-znadobliatsia-237910.html', 'image': 'https://novyny.live/cdn-cgi/imagedelivery/4_JwVYxosZqzJ7gIDJgTLA/b3e82c60-23e9-4e7b-642e-587371f89700/16x9', 'publishedAt': '2025-03-05T09:29:00Z', 'source': {'name': 'Новини Live', 'url': 'https://novyny.live'}}, {'title': 'Sony запустила програму бета-тестування PlayStation - з новими функціями PS5 та іграми для ПК і консолей', 'description': 'Sony пішла по стопах Xbox і Steam і\xa0відкрила реєстрацію на нову програму бета-тестування', 'content': 'Sony відкрила реєстрацію на нову програму бета-тестування для PlayStation / Depositphotos\nSony пішла по стопах Xbox і Steam і відкрила реєстрацію на нову програму бета-тестування PlayStation — вона доступна в усіх регіонах PlayStation Network (і для ... [1001 chars]', 'url': 'https://itc.ua/ua/novini/sony-zapustyla-programu-beta-testuvannya-playstation-z-novymy-funktsiyamy-ps5-ta-igramy-dlya-pk-i-konsolej/', 'image': 'https://itc.ua/wp-content/uploads/2025/03/Depositphotos_644437300_L.jpg', 'publishedAt': '2025-03-05T08:01:41Z', 'source': {'name': 'ITC', 'url': 'https://itc.ua'}}, {'title': 'Масована атака дронів, виступ Трампа у Конгресі: головне за ніч', 'description': '«Ви хочете, щоб це тривало ще 5 років?», – Трамп про війну Росії проти України', 'content': '«Ви хочете, щоб це тривало ще 5 років?», – Трамп про війну Росії проти України\nРосійська армія завдала удару по Одещині та Харкові, вибухи лунали і в Києві, Трамп виступив в залі Капітолію перед Конгресом США, Білий дім заперечив інформацію про підпи... [4218 chars]', 'url': 'https://glavcom.ua/country/incidents/masovana-ataka-droniv-vistup-trampa-u-konhresi-holovne-za-nich-1047852.html', 'image': 'https://glavcom.ua/img/article/10478/52_main-v1741148296.webp', 'publishedAt': '2025-03-05T04:18:00Z', 'source': {'name': 'ГЛАВКОМ', 'url': 'https://glavcom.ua'}}]}
# Експертка з ядерної енергетики пояснила, що залишиться від Запорізької АЕС після деокупації
# Росіяни розграбували ЧАЕС, коли тікали звідти, так вони й вчинять, залишаючи ЗАЕС – найбільший ядерний об’єкт на європейському континенті
# Росіяни розграбували ЧАЕС, коли тікали звідти, так вони й вчинять, залишаючи ЗАЕС – найбільший ядерний об’єкт на європейському континенті
# Окупанти вдадуться до мародерства під час відступу з Запорізької атомної електростанції. Про це заявила експертк... [1628 chars]
# https://glavcom.ua/country/incidents/ekspertka-z-jadernoji-enerhetiki-pojasnila-shcho-zalishitsja-vid-zaporizkoji-aes-pislja-deokupatsiji-1047972.html

# if "articles" in data: 
#     for article in data["articles"]:
#         print(f"{article["title"]}")    
#         print(f"{article["description"]}")
#         print(f"{article["content"]}")    
#         print(f"{article["url"]}\n")

news_data = {
    "technology": [
        {
            "title": "OpenAI випустила GPT-5",
            "source": "TechCrunch",
            "url": "https://techcrunch.com/openai-gpt5",
            "content": "OpenAI анонсувала нову модель GPT-5 з покращеною продуктивністю та можливостями..."
        },
        {
            "title": "Новий прорив у квантових обчисленнях",
            "source": "Wired",
            "url": "https://wired.com/quantum-breakthrough",
            "content": "Вчені зробили важливий крок у розвитку квантових обчислень..."
        }
    ],
    "business": [
        {
            "title": "Біткоїн досяг $100,000",
            "source": "Forbes",
            "url": "https://forbes.com/bitcoin-100k",
            "content": "Курс біткоїна перевищив позначку в 100 тисяч доларів США..."
        }
    ],
    "science": [
        {
            "title": "Марсохід Perseverance знайшов сліди стародавнього життя",
            "source": "NASA",
            "url": "https://nasa.gov/perseverance-discovery",
            "content": "Нові дані з Марса вказують на можливу наявність органічних речовин..."
        }
    ]
}
def get_news(category):
    
        for article in news_data['technology']:
            print(f"{article['title']}")
            print(f"{article['content']}")
            print(f"{article['url']}\n")
            
print(get_news('news_data'))
print(get_news('news_data'))