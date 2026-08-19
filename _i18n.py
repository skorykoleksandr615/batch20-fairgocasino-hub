# -*- coding: utf-8 -*-
"""Write complete 11-lang i18n-dict.js for Fair Go Casino."""
from pathlib import Path
import json

HUB = Path(r"C:\AndroidStudioProjects\batch20-hubs\fairgocasino")
LANGS = ["de", "ru", "uk", "pl", "es", "pt", "fr", "it", "tr", "nl"]

def t(*a):
    if len(a) != 10:
        raise ValueError(a)
    return dict(zip(LANGS, a))

P = {}

def add(en, *a):
    P[en] = t(*a)

# --- nav / chrome ---
add("Home", "Start", "Главная", "Головна", "Start", "Inicio", "Início", "Accueil", "Home", "Ana sayfa", "Home")
add("Login", "Login", "Вход", "Вхід", "Logowanie", "Acceso", "Login", "Connexion", "Accesso", "Giriş", "Login")
add("Register", "Registrieren", "Регистрация", "Реєстрація", "Rejestracja", "Registro", "Registo", "Inscription", "Registrazione", "Kayıt", "Registreren")
add("Bonus", "Bonus", "Бонус", "Бонус", "Bonus", "Bono", "Bónus", "Bonus", "Bonus", "Bonus", "Bonus")
add("Slots", "Slots", "Слоты", "Слоти", "Sloty", "Slots", "Slots", "Machines", "Slot", "Slotlar", "Slots")
add("Odds", "Quoten", "Кэфы", "Коеф", "Kursy", "Cuotas", "Odds", "Cotes", "Quote", "Oranlar", "Odds")
add("Crash", "Crash", "Краш", "Краш", "Crash", "Crash", "Crash", "Crash", "Crash", "Crash", "Crash")
add("Live", "Live", "Лайв", "Лайв", "Live", "En vivo", "Ao vivo", "Live", "Live", "Canlı", "Live")
add("App", "App", "Приложение", "Додаток", "Aplikacja", "App", "App", "App", "App", "Uygulama", "App")
add("Pay", "Zahlen", "Касса", "Каса", "Płatności", "Pagar", "Pagar", "Payer", "Paga", "Öde", "Betalen")
add("Help", "Hilfe", "Помощь", "Допомога", "Pomoc", "Ayuda", "Ajuda", "Aide", "Aiuto", "Yardım", "Hulp")
add("Official", "Offiziell", "Официально", "Офіційно", "Oficjalnie", "Oficial", "Oficial", "Officiel", "Ufficiale", "Resmi", "Officieel")
add("Play Now", "Jetzt spielen", "Играть", "Грати", "Graj teraz", "Jugar ahora", "Jogar agora", "Jouer", "Gioca ora", "Hemen oyna", "Speel nu")
add("Open menu", "Menü öffnen", "Открыть меню", "Відкрити меню", "Otwórz menu", "Abrir menú", "Abrir menu", "Ouvrir le menu", "Apri menu", "Menüyü aç", "Menu openen")
add("Language", "Sprache", "Язык", "Мова", "Język", "Idioma", "Idioma", "Langue", "Lingua", "Dil", "Taal")
add("Show more", "Mehr anzeigen", "Показать ещё", "Показати ще", "Pokaż więcej", "Ver más", "Ver mais", "Voir plus", "Mostra di più", "Daha fazla", "Meer tonen")
add("Place Bet", "Wette platzieren", "Поставить", "Поставити", "Postaw", "Apostar", "Apostar", "Parier", "Punta", "Bahis yap", "Wedden")
add("Login and Play", "Login und spielen", "Войти и играть", "Увійти і грати", "Zaloguj i graj", "Entrar y jugar", "Entrar e jogar", "Connexion et jeu", "Accedi e gioca", "Giriş yap ve oyna", "Inloggen en spelen")
add("Registration bonus", "Registrierungsbonus", "Бонус за регистрацию", "Бонус за реєстрацію", "Bonus za rejestrację", "Bono de registro", "Bónus de registo", "Bonus d'inscription", "Bonus registrazione", "Kayıt bonusu", "Registratiebonus")
add("View Odds", "Quoten ansehen", "Смотреть кэфы", "Дивитись коеф", "Zobacz kursy", "Ver cuotas", "Ver odds", "Voir les cotes", "Vedi quote", "Oranları gör", "Odds bekijken")
add("Open Login", "Login öffnen", "Открыть вход", "Відкрити вхід", "Otwórz logowanie", "Abrir acceso", "Abrir login", "Ouvrir connexion", "Apri accesso", "Girişi aç", "Login openen")
add("Open Register", "Registrierung öffnen", "Открыть регистрацию", "Відкрити реєстрацію", "Otwórz rejestrację", "Abrir registro", "Abrir registo", "Ouvrir l'inscription", "Apri registrazione", "Kaydı aç", "Registratie openen")
add("Open Bonus Path", "Bonuspfad öffnen", "Открыть путь бонуса", "Відкрити шлях бонусу", "Otwórz ścieżkę bonusu", "Abrir ruta de bono", "Abrir caminho do bónus", "Ouvrir le parcours bonus", "Apri percorso bonus", "Bonus yolunu aç", "Bonuspad openen")
add("Open Bonus", "Bonus öffnen", "Открыть бонус", "Відкрити бонус", "Otwórz bonus", "Abrir bono", "Abrir bónus", "Ouvrir le bonus", "Apri bonus", "Bonusu aç", "Bonus openen")
add("Open Slots", "Slots öffnen", "Открыть слоты", "Відкрити слоти", "Otwórz sloty", "Abrir slots", "Abrir slots", "Ouvrir les machines", "Apri slot", "Slotları aç", "Slots openen")
add("Open Crash", "Crash öffnen", "Открыть краш", "Відкрити краш", "Otwórz crash", "Abrir crash", "Abrir crash", "Ouvrir crash", "Apri crash", "Crash aç", "Crash openen")
add("Join Live", "Live beitreten", "В лайв", "У лайв", "Dołącz live", "Unirse en vivo", "Entrar ao vivo", "Rejoindre le live", "Entra live", "Canlıya katıl", "Live joinen")
add("Open Mobile Lobby", "Mobile Lobby öffnen", "Открыть мобильное лобби", "Відкрити мобільне лобі", "Otwórz mobilne lobby", "Abrir lobby móvil", "Abrir lobby móvel", "Ouvrir le lobby mobile", "Apri lobby mobile", "Mobil lobiyi aç", "Mobiele lobby openen")
add("Open Mobile", "Mobil öffnen", "Открыть мобилку", "Відкрити мобілку", "Otwórz mobile", "Abrir móvil", "Abrir móvel", "Ouvrir mobile", "Apri mobile", "Mobil aç", "Mobiel openen")
add("Go to Cashier", "Zur Kasse", "В кассу", "До каси", "Do kasy", "Ir a caja", "Ir à caixa", "Aller à la caisse", "Vai in cassa", "Kasaya git", "Naar kassa")
add("Open Cashier", "Kasse öffnen", "Открыть кассу", "Відкрити касу", "Otwórz kasę", "Abrir caja", "Abrir caixa", "Ouvrir la caisse", "Apri cassa", "Kasayı aç", "Kassa openen")
add("Open Help Path", "Hilfe öffnen", "Открыть помощь", "Відкрити допомогу", "Otwórz pomoc", "Abrir ayuda", "Abrir ajuda", "Ouvrir l'aide", "Apri aiuto", "Yardımı aç", "Hulp openen")
add("Open Support", "Support öffnen", "Открыть поддержку", "Відкрити підтримку", "Otwórz support", "Abrir soporte", "Abrir suporte", "Ouvrir le support", "Apri supporto", "Destek aç", "Support openen")
add("Bonus guide", "Bonus-Guide", "Гид по бонусу", "Гід по бонусу", "Przewodnik bonus", "Guía de bono", "Guia de bónus", "Guide bonus", "Guida bonus", "Bonus rehberi", "Bonusgids")
add("Login guide", "Login-Guide", "Гид входа", "Гід входу", "Przewodnik logowania", "Guía de acceso", "Guia de login", "Guide de connexion", "Guida accesso", "Giriş rehberi", "Logingids")
add("Sports Odds", "Sportquoten", "Спорт-кэфы", "Спорт-коеф", "Kursy sportowe", "Cuotas deportivas", "Odds desportivas", "Cotes sportives", "Quote sportive", "Spor oranları", "Sportodds")
add("Live Casino", "Live Casino", "Лайв-казино", "Лайв-казино", "Kasyno na żywo", "Casino en vivo", "Casino ao vivo", "Casino live", "Casino live", "Canlı casino", "Livecasino")
add("Top Slots", "Top-Slots", "Топ слоты", "Топ слоти", "Top sloty", "Top slots", "Top slots", "Top machines", "Top slot", "Top slotlar", "Top slots")
add("Welcome Bonus", "Willkommensbonus", "Приветственный бонус", "Вітальний бонус", "Bonus powitalny", "Bono de bienvenida", "Bónus de boas-vindas", "Bonus de bienvenue", "Bonus di benvenuto", "Hoş geldin bonusu", "Welkomstbonus")
add("Football", "Fußball", "Футбол", "Футбол", "Piłka nożna", "Fútbol", "Futebol", "Football", "Calcio", "Futbol", "Voetbal")
add("Basketball", "Basketball", "Баскетбол", "Баскетбол", "Koszykówka", "Baloncesto", "Basquetebol", "Basket-ball", "Pallacanestro", "Basketbol", "Basketbal")
add("Tennis", "Tennis", "Теннис", "Теніс", "Tenis", "Tenis", "Ténis", "Tennis", "Tennis", "Tenis", "Tennis")
add("Cricket", "Cricket", "Крикет", "Крикет", "Krykiet", "Críquet", "Críquete", "Cricket", "Cricket", "Kriket", "Cricket")
add("Rugby", "Rugby", "Регби", "Регбі", "Rugby", "Rugby", "Râguebi", "Rugby", "Rugby", "Ragbi", "Rugby")
add("AFL", "AFL", "AFL", "AFL", "AFL", "AFL", "AFL", "AFL", "AFL", "AFL", "AFL")
add("NRL", "NRL", "NRL", "NRL", "NRL", "NRL", "NRL", "NRL", "NRL", "NRL", "NRL")
add("Sports markets", "Sportmärkte", "Спортивные рынки", "Спортивні ринки", "Rynki sportowe", "Mercados deportivos", "Mercados desportivos", "Marchés sportifs", "Mercati sportivi", "Spor piyasaları", "Sportmarkten")
add("Quick links", "Schnelllinks", "Быстрые ссылки", "Швидкі посилання", "Szybkie linki", "Enlaces rápidos", "Ligações rápidas", "Liens rapides", "Link rapidi", "Hızlı bağlantılar", "Snelle links")
add("Top world providers", "Top-Weltanbieter", "Топ мировых провайдеров", "Топ світових провайдерів", "Top światowi dostawcy", "Top proveedores mundiales", "Top fornecedores mundiais", "Top fournisseurs mondiaux", "Top provider mondiali", "Dünya top sağlayıcıları", "Top wereldproviders")
add("Slot", "Slot", "Слот", "Слот", "Slot", "Slot", "Slot", "Machine", "Slot", "Slot", "Slot")
add("FAQ", "FAQ", "FAQ", "FAQ", "FAQ", "FAQ", "FAQ", "FAQ", "FAQ", "SSS", "FAQ")
add("Explore more", "Mehr entdecken", "Ещё разделы", "Ще розділи", "Zobacz więcej", "Explorar más", "Explorar mais", "Explorer plus", "Esplora altro", "Daha fazla keşfet", "Meer ontdekken")
add("Guide chapters", "Leitfaden-Kapitel", "Главы гида", "Розділи гіда", "Rozdziały przewodnika", "Capítulos de guía", "Capítulos do guia", "Chapitres du guide", "Capitoli guida", "Rehber bölümleri", "Gidshoofdstukken")
add("Practical steps for players.", "Praktische Schritte für Spieler.", "Практические шаги для игроков.", "Практичні кроки для гравців.", "Praktyczne kroki dla graczy.", "Pasos prácticos para jugadores.", "Passos práticos para jogadores.", "Étapes pratiques pour les joueurs.", "Passi pratici per i giocatori.", "Oyuncular için pratik adımlar.", "Praktische stappen voor spelers.")
add("Straight answers for login, bonus, odds, slots, crash and cashier.", "Klare Antworten zu Login, Bonus, Quoten, Slots, Crash und Kasse.", "Прямые ответы по входу, бонусу, кэфам, слотам, крашу и кассе.", "Прямі відповіді про вхід, бонус, коеф, слоти, краш і касу.", "Proste odpowiedzi o logowaniu, bonusie, kursach, slotach, crash i kasie.", "Respuestas claras sobre acceso, bono, cuotas, slots, crash y caja.", "Respostas diretas sobre login, bónus, odds, slots, crash e caixa.", "Réponses claires sur connexion, bonus, cotes, machines, crash et caisse.", "Risposte chiare su accesso, bonus, quote, slot, crash e cassa.", "Giriş, bonus, oran, slot, crash ve kasa için net cevaplar.", "Duidelijke antwoorden over login, bonus, odds, slots, crash en kassa.")
add("Primary", "Primär", "Основное", "Основне", "Główne", "Principal", "Principal", "Principal", "Principale", "Birincil", "Primair")
add("Footer", "Fußzeile", "Подвал", "Підвал", "Stopka", "Pie", "Rodapé", "Pied", "Piè", "Alt bilgi", "Voettekst")

# badges
add("SLOTS", "SLOTS", "СЛОТЫ", "СЛОТИ", "SLOTY", "SLOTS", "SLOTS", "SLOTS", "SLOT", "SLOTLAR", "SLOTS")
add("ODDS", "QUOTEN", "КЭФЫ", "КОЕФ", "KURSY", "CUOTAS", "ODDS", "COTES", "QUOTE", "ORAN", "ODDS")
add("CRASH", "CRASH", "КРАШ", "КРАШ", "CRASH", "CRASH", "CRASH", "CRASH", "CRASH", "CRASH", "CRASH")
add("LIVE", "LIVE", "ЛАЙВ", "ЛАЙВ", "LIVE", "EN VIVO", "AO VIVO", "LIVE", "LIVE", "CANLI", "LIVE")
add("BONUS", "BONUS", "БОНУС", "БОНУС", "BONUS", "BONO", "BÓNUS", "BONUS", "BONUS", "BONUS", "BONUS")
add("PAY", "ZAHLEN", "КАССА", "КАСА", "PŁATNOŚĆ", "PAGAR", "PAGAR", "PAYER", "PAGA", "ÖDE", "BETALEN")
add("LOGIN", "LOGIN", "ВХОД", "ВХІД", "LOGIN", "ACCESO", "LOGIN", "LOGIN", "ACCESSO", "GİRİŞ", "LOGIN")
add("JOIN", "JOIN", "ВХОД", "ВХІД", "DOŁĄCZ", "ÚNETE", "JUNTE-SE", "REJOINDRE", "ISCRIVITI", "KATIL", "JOIN")
add("APP", "APP", "APP", "APP", "APP", "APP", "APP", "APP", "APP", "APP", "APP")
add("HELP", "HILFE", "ПОМОЩЬ", "ДОПОМОГА", "POMOC", "AYUDA", "AJUDA", "AIDE", "AIUTO", "YARDIM", "HULP")

# --- home unique ---
add("Casino first on the map", "Casino zuerst auf der Karte", "Казино первым на карте", "Казино першим на мапі", "Kasyno najpierw na mapie", "Casino primero en el mapa", "Casino primeiro no mapa", "Casino d'abord sur la carte", "Casino prima sulla mappa", "Haritada önce casino", "Casino eerst op de kaart")
add("{Brand} Login for Slots, Odds and Live Casino", "{Brand} Login für Slots, Quoten und Live Casino", "{Brand}: вход для слотов, кэфов и лайв-казино", "{Brand}: вхід для слотів, коеф і лайв-казино", "{Brand}: logowanie do slotów, kursów i live casino", "{Brand}: acceso a slots, cuotas y casino en vivo", "{Brand}: login para slots, odds e casino ao vivo", "{Brand} : connexion slots, cotes et casino live", "{Brand}: accesso a slot, quote e casino live", "{Brand}: slot, oran ve canlı casino girişi", "{Brand}: login voor slots, odds en livecasino")
add("Big Bass, Aviator and A-League after sign-in", "Big Bass, Aviator und A-League nach dem Login", "Big Bass, Aviator и A-League после входа", "Big Bass, Aviator і A-League після входу", "Big Bass, Aviator i A-League po logowaniu", "Big Bass, Aviator y A-League tras el acceso", "Big Bass, Aviator e A-League após o login", "Big Bass, Aviator et A-League après connexion", "Big Bass, Aviator e A-League dopo l'accesso", "Girişten sonra Big Bass, Aviator ve A-League", "Big Bass, Aviator en A-League na aanmelden")
add("Sign in to {Brand} for Big Bass Bonanza, Wolf Gold, Aviator crash, Crazy Time and A-League 1X2 in one lobby. Confirm you land on the live platform from {Domain}.",
    "Melden Sie sich bei {Brand} an für Big Bass Bonanza, Wolf Gold, Aviator-Crash, Crazy Time und A-League-1X2 in einer Lobby. Prüfen Sie, dass Sie von {Domain} auf der Live-Plattform landen.",
    "Войдите в {Brand} для Big Bass Bonanza, Wolf Gold, краша Aviator, Crazy Time и 1X2 A-League в одном лобби. Убедитесь, что с {Domain} вы на живой платформе.",
    "Увійдіть у {Brand} для Big Bass Bonanza, Wolf Gold, крашу Aviator, Crazy Time і 1X2 A-League в одному лобі. Переконайтесь, що з {Domain} ви на живій платформі.",
    "Zaloguj się do {Brand} po Big Bass Bonanza, Wolf Gold, crash Aviator, Crazy Time i 1X2 A-League w jednym lobby. Potwierdź, że z {Domain} lądujesz na żywej platformie.",
    "Entra en {Brand} para Big Bass Bonanza, Wolf Gold, crash Aviator, Crazy Time y 1X2 de A-League en un lobby. Confirma que desde {Domain} llegas a la plataforma en vivo.",
    "Entre na {Brand} para Big Bass Bonanza, Wolf Gold, crash Aviator, Crazy Time e 1X2 da A-League num só lobby. Confirme que de {Domain} chega à plataforma live.",
    "Connectez-vous à {Brand} pour Big Bass Bonanza, Wolf Gold, crash Aviator, Crazy Time et 1X2 A-League dans un lobby. Confirmez que {Domain} mène à la plateforme live.",
    "Accedi a {Brand} per Big Bass Bonanza, Wolf Gold, crash Aviator, Crazy Time e 1X2 A-League in una lobby. Conferma di arrivare sulla piattaforma live da {Domain}.",
    "{Brand}'e giriş yapın: Big Bass Bonanza, Wolf Gold, Aviator crash, Crazy Time ve A-League 1X2 tek lobide. {Domain}'den canlı platforma indiğinizi doğrulayın.",
    "Log in op {Brand} voor Big Bass Bonanza, Wolf Gold, Aviator-crash, Crazy Time en A-League 1X2 in één lobby. Bevestig dat je vanaf {Domain} op het live platform landt.")
add("Map split board", "Karten-Split-Board", "Доска с картой", "Дошка з мапою", "Tablica ze mapą", "Tablero del mapa", "Quadro do mapa", "Tableau carte", "Board mappa", "Harita panosu", "Kaartbord")
add("A-League · AFL · NRL · Premier League", "A-League · AFL · NRL · Premier League", "A-League · AFL · NRL · Premier League", "A-League · AFL · NRL · Premier League", "A-League · AFL · NRL · Premier League", "A-League · AFL · NRL · Premier League", "A-League · AFL · NRL · Premier League", "A-League · AFL · NRL · Premier League", "A-League · AFL · NRL · Premier League", "A-League · AFL · NRL · Premier League", "A-League · AFL · NRL · Premier League")
add("{Brand} reel floor", "{Brand} Walzen-Floor", "Зал барабанов {Brand}", "Зал барабанів {Brand}", "Sala bębnów {Brand}", "Piso de rodillos {Brand}", "Piso de rolos {Brand}", "Floor des rouleaux {Brand}", "Piano rulli {Brand}", "{Brand} makara katı", "{Brand} rollenvloer")
add("Spin Big Bass and Wolf Gold after login", "Big Bass und Wolf Gold nach Login drehen", "Крутите Big Bass и Wolf Gold после входа", "Крутіть Big Bass і Wolf Gold після входу", "Kręć Big Bass i Wolf Gold po logowaniu", "Gira Big Bass y Wolf Gold tras el login", "Gire Big Bass e Wolf Gold após o login", "Tournez Big Bass et Wolf Gold après connexion", "Gira Big Bass e Wolf Gold dopo il login", "Girişten sonra Big Bass ve Wolf Gold çevirin", "Draai Big Bass en Wolf Gold na login")
add("Search the real titles listed below, set a spin budget, then open {Brand}.", "Suchen Sie die echten Titel unten, setzen Sie ein Spin-Budget, dann öffnen Sie {Brand}.", "Ищите реальные тайтлы ниже, задайте бюджет спинов и откройте {Brand}.", "Шукайте реальні тайтли нижче, задайте бюджет спінів і відкрийте {Brand}.", "Szukaj prawdziwych tytułów poniżej, ustaw budżet spinów i otwórz {Brand}.", "Busca los títulos reales abajo, fija presupuesto de giros y abre {Brand}.", "Procure os títulos reais abaixo, defina orçamento de spins e abra a {Brand}.", "Cherchez les vrais titres ci-dessous, fixez un budget de spins, puis ouvrez {Brand}.", "Cerca i titoli veri sotto, imposta un budget spin e apri {Brand}.", "Aşağıdaki gerçek başlıkları arayın, spin bütçesi koyun, {Brand}'i açın.", "Zoek de echte titels hieronder, zet een spinbudget en open {Brand}.")
add("Search the real titles listed on this hub, set a spin budget, then open {Brand}.", "Suchen Sie die echten Titel auf diesem Hub, setzen Sie ein Spin-Budget, dann öffnen Sie {Brand}.", "Ищите реальные тайтлы на хабе, задайте бюджет спинов и откройте {Brand}.", "Шукайте реальні тайтли на хабі, задайте бюджет спінів і відкрийте {Brand}.", "Szukaj prawdziwych tytułów na hubie, ustaw budżet spinów i otwórz {Brand}.", "Busca los títulos reales en este hub, fija presupuesto de giros y abre {Brand}.", "Procure os títulos reais neste hub, defina orçamento de spins e abra a {Brand}.", "Cherchez les vrais titres sur ce hub, fixez un budget de spins, puis ouvrez {Brand}.", "Cerca i titoli veri su questo hub, imposta un budget spin e apri {Brand}.", "Bu hubdaki gerçek başlıkları arayın, spin bütçesi koyun, {Brand}'i açın.", "Zoek de echte titels op deze hub, zet een spinbudget en open {Brand}.")
add("Spin on {Brand}", "Auf {Brand} drehen", "Крутить в {Brand}", "Крутити в {Brand}", "Kręć w {Brand}", "Girar en {Brand}", "Girar na {Brand}", "Tourner sur {Brand}", "Gira su {Brand}", "{Brand}'te çevir", "Draai op {Brand}")
add("Top World Slots", "Welt-Top-Slots", "Топ мировых слотов", "Топ світових слотів", "Światowe top sloty", "Top slots mundiales", "Top slots mundiais", "Top machines mondiales", "Top slot mondiali", "Dünya top slotları", "Wereldwijde top slots")
add("Real top world titles to search after login. Volatility differs — set a spin budget first.", "Echte Welt-Top-Titel nach dem Login suchen. Volatilität unterscheidet sich — zuerst Spin-Budget setzen.", "Реальные мировые топ-тайтлы после входа. Волатильность разная — сначала бюджет на спины.", "Реальні світові топ-тайтли після входу. Волатильність різна — спочатку бюджет на спіни.", "Prawdziwe światowe top tytuły po logowaniu. Zmienność bywa różna — najpierw budżet na spiny.", "Títulos top mundiales reales tras el login. La volatilidad cambia: fija presupuesto de giros primero.", "Títulos top mundiais reais após o login. A volatilidade muda — defina orçamento de spins primeiro.", "Vrais titres top mondiaux après connexion. La volatilité change — fixez un budget de spins d'abord.", "Veri titoli top mondiali dopo il login. La volatilità cambia — imposta prima un budget spin.", "Girişten sonra gerçek dünya top başlıkları. Volatilite değişir — önce spin bütçesi koyun.", "Echte wereldwijde toptitels na login. Volatiliteit verschilt — zet eerst een spinbudget.")
add("{Brand} match board", "{Brand} Match-Board", "Матч-доска {Brand}", "Матч-дошка {Brand}", "Tablica meczowa {Brand}", "Tablero de partido {Brand}", "Quadro de jogo {Brand}", "Tableau de match {Brand}", "Board partita {Brand}", "{Brand} maç panosu", "{Brand} wedstrijdbord")
add("Lock A-League 1X2 before kick-off", "A-League-1X2 vor dem Anpfiff sichern", "Зафиксируйте 1X2 A-League до свистка", "Зафіксуйте 1X2 A-League до свистка", "Zablokuj 1X2 A-League przed gwizdkiem", "Cierra el 1X2 de A-League antes del silbato", "Trave o 1X2 da A-League antes do apito", "Verrouillez le 1X2 A-League avant le coup d'envoi", "Blocca l'1X2 A-League prima del fischio", "Başlamadan önce A-League 1X2 kilitleyin", "Zet A-League 1X2 vast vóór de aftrap")
add("Compare sample prices here, then place the slip inside {Brand}.", "Vergleichen Sie hier Sample-Kurse, dann den Schein in {Brand} platzieren.", "Сравните сэмпл-цены здесь, затем поставьте купон в {Brand}.", "Порівняйте семпл-ціни тут, потім поставте купон у {Brand}.", "Porównaj tu próbné ceny, potem złóż kupon w {Brand}.", "Compara precios de muestra aquí y coloca el boleto en {Brand}.", "Compare preços de amostra aqui e coloque o boletim na {Brand}.", "Comparez les prix d'échantillon ici, puis placez le coupon dans {Brand}.", "Confronta i prezzi di esempio qui, poi piazza lo slip su {Brand}.", "Örnek fiyatları burada karşılaştırın, kuponu {Brand}'te yatırın.", "Vergelijk hier voorbeeldprijzen en plaats de slip in {Brand}.")
add("Bet on {Brand}", "Auf {Brand} wetten", "Ставка в {Brand}", "Ставка в {Brand}", "Postaw w {Brand}", "Apostar en {Brand}", "Apostar na {Brand}", "Parier sur {Brand}", "Punta su {Brand}", "{Brand}'te bahis", "Wed op {Brand}")
add("Sample boards for A-League, AFL and NRL — open the live sportsbook for full markets.", "Sample-Boards für A-League, AFL und NRL — öffnen Sie das Live-Sportsbook für volle Märkte.", "Сэмпл-доски A-League, AFL и NRL — полный рынок в живом спортбуке.", "Семпл-дошки A-League, AFL і NRL — повний ринок у живому спортбуці.", "Próbne tablice A-League, AFL i NRL — pełne rynki w live sportsbooku.", "Tableros de muestra de A-League, AFL y NRL: abre el sportsbook en vivo para todos los mercados.", "Boards de amostra da A-League, AFL e NRL — abra o sportsbook ao vivo para mercados completos.", "Tableaux d'échantillon A-League, AFL et NRL — ouvrez le sportsbook live pour tous les marchés.", "Board di esempio A-League, AFL e NRL — apri lo sportsbook live per i mercati completi.", "A-League, AFL ve NRL örnek panoları — tam piyasalar için canlı sportsbook'u açın.", "Voorbeeldborden voor A-League, AFL en NRL — open de live sportsbook voor alle markten.")
add("{Brand} climb rounds", "{Brand} Steig-Runden", "Раунды набора {Brand}", "Раунди набору {Brand}", "Rundy wznoszenia {Brand}", "Rondas de subida {Brand}", "Rondas de subida {Brand}", "Manches de montée {Brand}", "Round di salita {Brand}", "{Brand} tırmanış turları", "{Brand} klimrondes")
add("Aviator and JetX cash-out rules", "Aviator- und JetX-Cash-out-Regeln", "Правила кэшаута Aviator и JetX", "Правила кешауту Aviator і JetX", "Zasady cash-out Aviator i JetX", "Reglas de cash-out de Aviator y JetX", "Regras de cash-out Aviator e JetX", "Règles de cash-out Aviator et JetX", "Regole di cash-out Aviator e JetX", "Aviator ve JetX cash-out kuralları", "Aviator- en JetX-cash-outregels")
add("Set auto cash-out before the plane climbs. Never chase a missed exit.", "Auto-Cash-out setzen, bevor das Flugzeug steigt. Nie einen verpassten Exit jagen.", "Задайте автокэшаут до набора. Никогда не догоняйте пропущенный выход.", "Задайте автокешаут до набору. Ніколи не женіться за пропущеним виходом.", "Ustaw auto cash-out zanim samolot wzniesie się. Nie gonić za pominiętym wyjściem.", "Fija el auto cash-out antes de que suba el avión. Nunca persigas una salida fallida.", "Defina o auto cash-out antes do avião subir. Nunca persiga uma saída falhada.", "Réglez l'auto cash-out avant la montée. Ne chassez jamais une sortie manquée.", "Imposta l'auto cash-out prima che l'aereo salga. Non inseguire mai un'uscita persa.", "Uçak tırmanmadan otomatik cash-out koyun. Kaçan çıkışı asla kovalamayın.", "Zet auto cash-out vóór het vliegtuig klimt. Jaag een gemiste exit nooit na.")
add("Aviator-style rounds, Mines grids and Plinko boards — decide the exit before you stake.", "Aviator-Runden, Mines-Gitter und Plinko-Boards — Exit vor dem Einsatz festlegen.", "Раунды в стиле Aviator, сетки Mines и доски Plinko — выход до ставки.", "Раунди в стилі Aviator, сітки Mines і дошки Plinko — вихід до ставки.", "Rundy w stylu Aviator, siatki Mines i tablice Plinko — ustal wyjście przed stawką.", "Rondas estilo Aviator, grids Mines y tableros Plinko: decide la salida antes de apostar.", "Rondas estilo Aviator, grelhas Mines e boards Plinko — decida a saída antes da aposta.", "Manches style Aviator, grilles Mines et plateaux Plinko — fixez la sortie avant la mise.", "Round stile Aviator, griglie Mines e board Plinko — decidi l'uscita prima della puntata.", "Aviator tarzı turlar, Mines ızgaraları ve Plinko — bahisten önce çıkışı kararlaştırın.", "Aviator-rondes, Mines-grids en Plinko-borden — kies de exit vóór je inzet.")
add("Crash Games", "Crash-Spiele", "Краш-игры", "Краш-ігри", "Gry crash", "Juegos crash", "Jogos crash", "Jeux crash", "Giochi crash", "Crash oyunları", "Crashspellen")
add("{Brand} studio floor", "{Brand} Studio-Floor", "Студийный зал {Brand}", "Студійний зал {Brand}", "Studio {Brand}", "Piso de estudio {Brand}", "Estúdio {Brand}", "Plateau studio {Brand}", "Studio {Brand}", "{Brand} stüdyo katı", "{Brand} studiovloer")
add("Crazy Time and Lightning Roulette", "Crazy Time und Lightning Roulette", "Crazy Time и Lightning Roulette", "Crazy Time і Lightning Roulette", "Crazy Time i Lightning Roulette", "Crazy Time y Lightning Roulette", "Crazy Time e Lightning Roulette", "Crazy Time et Lightning Roulette", "Crazy Time e Lightning Roulette", "Crazy Time ve Lightning Roulette", "Crazy Time en Lightning Roulette")
add("Join a live table after login. Keep a table budget separate from sports slips.", "Nach Login an einen Live-Tisch. Tisch-Budget getrennt von Sports-Scheinen halten.", "После входа сядьте за лайв-стол. Бюджет стола отдельно от спорт-купонов.", "Після входу сядьте за лайв-стіл. Бюджет столу окремо від спорт-купонів.", "Po logowaniu dołącz do stołu live. Budżet stołu oddziel od kuponów sportowych.", "Únete a una mesa en vivo tras el login. Separa el presupuesto de mesa de las apuestas deportivas.", "Junte-se a uma mesa ao vivo após o login. Separe o orçamento da mesa dos boletims desportivos.", "Rejoignez une table live après connexion. Séparez le budget table des coupons sport.", "Entra a un tavolo live dopo il login. Tieni il budget tavolo separato dagli slip sportivi.", "Girişten sonra canlı masaya katılın. Masa bütçesini spor kuponlarından ayırın.", "Ga na login aan een live tafel. Houd het tafelbudget los van sportsips.")
add("Dealer tables and game shows from Evolution-style studios — one {Brand} account.", "Dealer-Tische und Game-Shows aus Evolution-Studios — ein {Brand}-Konto.", "Столы дилеров и шоу из студий в стиле Evolution — один аккаунт {Brand}.", "Столи дилерів і шоу зі студій у стилі Evolution — один акаунт {Brand}.", "Stoły dealera i game show ze studiów typu Evolution — jedno konto {Brand}.", "Mesas de crupier y game shows de estudios estilo Evolution: una cuenta {Brand}.", "Mesas de dealer e game shows de estúdios estilo Evolution — uma conta {Brand}.", "Tables croupier et game shows de studios style Evolution — un compte {Brand}.", "Tavoli dealer e game show da studi stile Evolution — un account {Brand}.", "Evolution tarzı stüdyolardan dealer masaları ve şovlar — tek {Brand} hesap.", "Dealertafels en game shows uit Evolution-studio's — één {Brand}-account.")
add("{Brand} welcome path", "{Brand} Welcome-Pfad", "Welcome-путь {Brand}", "Welcome-шлях {Brand}", "Ścieżka welcome {Brand}", "Ruta welcome {Brand}", "Caminho welcome {Brand}", "Parcours welcome {Brand}", "Percorso welcome {Brand}", "{Brand} hoş geldin yolu", "{Brand} welkomstpad")
add("Read wagering before you opt in", "Wettanforderung vor dem Opt-in lesen", "Прочитайте вейджер до opt-in", "Прочитайте вейджер до opt-in", "Przeczytaj obrót przed opt-in", "Lee el wagering antes de optar", "Leia o wagering antes de aderir", "Lisez le wagering avant l'opt-in", "Leggi il wagering prima dell'opt-in", "Opt-in öncesi çevrimi okuyun", "Lees de inzet vóór je opt-in")
add("Eligible sports and slots are listed in the live terms after registration.", "Berechtigte Sportarten und Slots stehen nach der Registrierung in den Live-Bedingungen.", "Подходящие спорт и слоты — в живых условиях после регистрации.", "Підходящі спорт і слоти — у живих умовах після реєстрації.", "Uprawniony sport i sloty są w żywych regulaminach po rejestracji.", "Deportes y slots elegibles están en los términos en vivo tras el registro.", "Desporto e slots elegíveis estão nos termos live após o registo.", "Sports et machines éligibles figurent dans les conditions live après inscription.", "Sport e slot ammessi sono nei termini live dopo la registrazione.", "Uygun spor ve slotlar kayıt sonrası canlı şartlarda listelenir.", "Geschikte sport en slots staan na registratie in de live voorwaarden.")
add("Registration path and wagering basics — no invented percentages on this hub.", "Registrierungspfad und Wettanforderungs-Basics — keine erfundenen Prozente auf diesem Hub.", "Путь регистрации и база вейджера — без выдуманных процентов на хабе.", "Шлях реєстрації і база вейджеру — без вигаданих відсотків на хабі.", "Ścieżka rejestracji i podstawy obrotu — bez wymyślonych procentów na hubie.", "Ruta de registro y base de wagering: sin porcentajes inventados en este hub.", "Caminho de registo e bases de wagering — sem percentagens inventadas neste hub.", "Parcours d'inscription et bases de mise — aucun pourcentage inventé sur ce hub.", "Percorso registrazione e basi del wagering — nessuna percentuale inventata su questo hub.", "Kayıt yolu ve çevrim temelleri — bu hubda uydurma yüzde yok.", "Registratiepad en inzetbasics — geen verzonnen percentages op deze hub.")
add("Create the {Brand} account from {Domain}, then open the welcome offer only on the live site. Check wagering, min odds and eligible games before you deposit. Sports slips and slots may carry different contribution rates.",
    "Erstellen Sie das {Brand}-Konto von {Domain}, dann das Welcome-Angebot nur auf der Live-Site öffnen. Wettanforderung, Min-Quote und berechtigte Spiele vor der Einzahlung prüfen. Sportscheine und Slots können unterschiedlich beitragen.",
    "Создайте аккаунт {Brand} с {Domain}, затем откройте welcome только на живом сайте. Проверьте вейджер, мин. кэф и игры до депозита. Спорт и слоты могут давать разный вклад.",
    "Створіть акаунт {Brand} з {Domain}, потім відкрийте welcome лише на живому сайті. Перевірте вейджер, мін. коеф і ігри до депозиту. Спорт і слоти можуть давати різний внесок.",
    "Utwórz konto {Brand} z {Domain}, potem otwórz ofertę welcome tylko na żywej stronie. Sprawdź obrót, min kurs i gry przed wpłatą. Kupony sport i sloty mogą mieć inne wagi.",
    "Crea la cuenta {Brand} desde {Domain} y abre la oferta welcome solo en el sitio live. Revisa wagering, cuota mín. y juegos antes de depositar. Deportes y slots pueden aportar distinto.",
    "Crie a conta {Brand} a partir de {Domain} e abra a oferta welcome só no site live. Veja wagering, odd mín. e jogos antes de depositar. Desporto e slots podem contribuir diferente.",
    "Créez le compte {Brand} depuis {Domain}, puis ouvrez l'offre welcome uniquement sur le site live. Vérifiez mise, cote min et jeux avant de déposer. Sport et machines peuvent contribuer différemment.",
    "Crea l'account {Brand} da {Domain}, poi apri l'offerta welcome solo sul sito live. Controlla wagering, quota min e giochi prima del deposito. Sport e slot possono contribuire in modo diverso.",
    "{Domain}'den {Brand} hesabı oluşturun, hoş geldin teklifini yalnızca canlı sitede açın. Yatırmadan önce çevrim, min oran ve uygun oyunları kontrol edin. Spor ve slotların katkısı farklı olabilir.",
    "Maak het {Brand}-account vanaf {Domain} en open de welkomstoffer alleen op de live site. Check inzet, min. odds en spellen vóór je stort. Sport en slots kunnen anders bijdragen.")
add("Claim on {Brand}", "Auf {Brand} beanspruchen", "Забрать в {Brand}", "Забрати в {Brand}", "Odbierz w {Brand}", "Reclamar en {Brand}", "Reclamar na {Brand}", "Réclamer sur {Brand}", "Richiedi su {Brand}", "{Brand}'te al", "Claim op {Brand}")
add("{Brand} cashier", "Kasse {Brand}", "Касса {Brand}", "Каса {Brand}", "Kasa {Brand}", "Caja {Brand}", "Caixa {Brand}", "Caisse {Brand}", "Cassa {Brand}", "{Brand} kasa", "{Brand} kassa")
add("Deposit and withdraw in one profile", "Ein- und Auszahlung in einem Profil", "Депозит и вывод в одном профиле", "Депозит і вивід в одному профілі", "Wpłata i wypłata w jednym profilu", "Deposita y retira en un perfil", "Deposite e levante num perfil", "Dépôt et retrait dans un profil", "Deposita e preleva in un profilo", "Tek profilde yatır ve çek", "Storten en opnemen in één profiel")
add("Finish KYC early so cashouts are not stalled after a winning slip.", "KYC früh erledigen, damit Auszahlungen nach einem Gewinnschein nicht stocken.", "Пройдите KYC заранее — вывод после выигрышного купона не встанет.", "Пройдіть KYC заздалегідь — вивід після виграшного купона не стане.", "Zrób KYC wcześnie, by wypłata po wygranym kuponie nie stanęła.", "Completa KYC pronto para que el retiro no se frene tras un boleto ganador.", "Conclua o KYC cedo para o levantamento não parar após um boletim vencedor.", "Terminez le KYC tôt pour que le retrait ne bloque pas après un coupon gagnant.", "Completa il KYC presto così il prelievo non si blocca dopo uno slip vincente.", "Kazanan kupondan sonra çekim takılmasın diye KYC'yi erken bitirin.", "Rond KYC vroeg af zodat opnames na een winnende slip niet stilvallen.")
add("{Brand} gate", "Tor {Brand}", "Вход {Brand}", "Вхід {Brand}", "Brama {Brand}", "Puerta {Brand}", "Portão {Brand}", "Porte {Brand}", "Varco {Brand}", "{Brand} kapısı", "{Brand} poort")
add("Sign in, then open the live lobby", "Anmelden, dann die Live-Lobby öffnen", "Войдите, затем откройте живое лобби", "Увійдіть, потім відкрийте живе лобі", "Zaloguj się, potem otwórz żywe lobby", "Entra y abre el lobby en vivo", "Entre e abra o lobby live", "Connectez-vous, puis ouvrez le lobby live", "Accedi, poi apri la lobby live", "Giriş yapın, sonra canlı lobiyi açın", "Log in en open de live lobby")
add("No password fields on this hub. Continue only on the live {Brand} site.", "Keine Passwortfelder auf diesem Hub. Nur auf der Live-{Brand}-Site fortfahren.", "На хабе нет полей пароля. Продолжайте только на живом сайте {Brand}.", "На хабі немає полів пароля. Продовжуйте лише на живому сайті {Brand}.", "Brak pól hasła na hubie. Kontynuuj tylko na żywej stronie {Brand}.", "Sin campos de contraseña en este hub. Sigue solo en el sitio live de {Brand}.", "Sem campos de palavra-passe neste hub. Continue só no site live da {Brand}.", "Aucun champ mot de passe sur ce hub. Continuez uniquement sur le site live {Brand}.", "Nessun campo password su questo hub. Continua solo sul sito live {Brand}.", "Bu hubda şifre alanı yok. Yalnızca canlı {Brand} sitesinde devam edin.", "Geen wachtwoordvelden op deze hub. Ga alleen verder op de live {Brand}-site.")
add("{Brand} on {Domain}", "{Brand} auf {Domain}", "{Brand} на {Domain}", "{Brand} на {Domain}", "{Brand} na {Domain}", "{Brand} en {Domain}", "{Brand} em {Domain}", "{Brand} sur {Domain}", "{Brand} su {Domain}", "{Domain} üzerinde {Brand}", "{Brand} op {Domain}")
add("{Brand} players use {Domain} to reach login, then open Big Bass Bonanza and A-League boards first. Wolf Gold, Aviator and Crazy Time stay in the same account. This hub does not host passwords or payment forms.",
    "{Brand}-Spieler nutzen {Domain} für den Login, dann zuerst Big Bass Bonanza und A-League-Boards. Wolf Gold, Aviator und Crazy Time bleiben im selben Konto. Dieser Hub hostet keine Passwörter oder Zahlungsformulare.",
    "Игроки {Brand} заходят через {Domain}, затем открывают Big Bass Bonanza и доски A-League. Wolf Gold, Aviator и Crazy Time — в том же аккаунте. Хаб не хранит пароли и платёжные формы.",
    "Гравці {Brand} заходять через {Domain}, потім відкривають Big Bass Bonanza і дошки A-League. Wolf Gold, Aviator і Crazy Time — в тому ж акаунті. Хаб не зберігає паролі й платіжні форми.",
    "Gracze {Brand} wchodzą przez {Domain}, potem otwierają Big Bass Bonanza i tablice A-League. Wolf Gold, Aviator i Crazy Time zostają w tym samym koncie. Hub nie trzyma haseł ani formularzy płatności.",
    "Los jugadores de {Brand} usan {Domain} para entrar y abren primero Big Bass Bonanza y tableros A-League. Wolf Gold, Aviator y Crazy Time quedan en la misma cuenta. Este hub no aloja contraseñas ni formularios de pago.",
    "Os jogadores da {Brand} usam {Domain} para entrar e abrem primeiro Big Bass Bonanza e boards A-League. Wolf Gold, Aviator e Crazy Time ficam na mesma conta. Este hub não aloja palavras-passe nem formulários de pagamento.",
    "Les joueurs {Brand} passent par {Domain} pour le login, puis ouvrent Big Bass Bonanza et les tableaux A-League. Wolf Gold, Aviator et Crazy Time restent dans le même compte. Ce hub n'héberge ni mots de passe ni formulaires de paiement.",
    "I giocatori {Brand} usano {Domain} per il login, poi aprono Big Bass Bonanza e i board A-League. Wolf Gold, Aviator e Crazy Time restano nello stesso account. Questo hub non ospita password né form di pagamento.",
    "{Brand} oyuncuları giriş için {Domain}'i kullanır, sonra önce Big Bass Bonanza ve A-League panolarını açar. Wolf Gold, Aviator ve Crazy Time aynı hesaptadır. Bu hub şifre veya ödeme formu barındırmaz.",
    "{Brand}-spelers gebruiken {Domain} om in te loggen en openen eerst Big Bass Bonanza en A-League-borden. Wolf Gold, Aviator en Crazy Time blijven in hetzelfde account. Deze hub host geen wachtwoorden of betaalformulieren.")
add("Set a bankroll before kick-off or the first spin. Prefer one bookmark for return visits and recheck the address bar after redirects.",
    "Bankroll vor Anpfiff oder erstem Spin setzen. Ein Lesezeichen für Rückkehr, Adressleiste nach Redirects prüfen.",
    "Задайте банкролл до свистка или первого спина. Одна закладка на возврат, проверяйте адресную строку после редиректов.",
    "Задайте банкрол до свистка або першого спіну. Одна закладка на повернення, перевіряйте адресний рядок після редиректів.",
    "Ustaw bankroll przed gwizdkiem lub pierwszym spinem. Jedna zakładka na powrót, sprawdzaj pasek adresu po przekierowaniach.",
    "Fija un bankroll antes del silbato o el primer giro. Un marcador para volver y revisa la barra de direcciones tras redirecciones.",
    "Defina um bankroll antes do apito ou do primeiro spin. Um marcador para voltar e reveja a barra de endereço após redirecionamentos.",
    "Fixez un bankroll avant le coup d'envoi ou le premier spin. Un favori pour revenir et revérifiez la barre d'adresse après les redirections.",
    "Imposta un bankroll prima del fischio o del primo spin. Un segnalibro per tornare e ricontrolla la barra degli indirizzi dopo i redirect.",
    "Başlama düdüğünden veya ilk spinden önce bankroll koyun. Dönüş için tek yer imi; yönlendirmelerden sonra adres çubuğunu kontrol edin.",
    "Zet een bankroll vóór de aftrap of de eerste spin. Eén bladwijzer voor terugkeer en check de adresbalk na redirects.")
add("What is {Domain} for {Brand}?", "Wofür ist {Domain} bei {Brand}?", "Зачем {Domain} для {Brand}?", "Навіщо {Domain} для {Brand}?", "Po co jest {Domain} dla {Brand}?", "¿Para qué es {Domain} en {Brand}?", "Para que serve {Domain} na {Brand}?", "À quoi sert {Domain} pour {Brand} ?", "A cosa serve {Domain} per {Brand}?", "{Brand} için {Domain} nedir?", "Waarvoor is {Domain} bij {Brand}?")
add("{Domain} is an orientation hub for {Brand} login, slots, A-League odds, Aviator crash, live casino and cashier. Tap Play Now and confirm you land on the live {Brand} platform.",
    "{Domain} ist ein Orientierungs-Hub für {Brand}-Login, Slots, A-League-Quoten, Aviator-Crash, Live Casino und Kasse. Tippen Sie Jetzt spielen und prüfen Sie die Live-{Brand}-Plattform.",
    "{Domain} — ориентир для входа {Brand}, слотов, кэфов A-League, краша Aviator, лайва и кассы. Нажмите Играть и убедитесь, что вы на живой платформе {Brand}.",
    "{Domain} — орієнтир для входу {Brand}, слотів, коеф A-League, крашу Aviator, лайву і каси. Натисніть Грати й переконайтесь, що ви на живій платформі {Brand}.",
    "{Domain} to hub orientacyjny do logowania {Brand}, slotów, kursów A-League, crash Aviator, live i kasy. Stuknij Graj teraz i potwierdź żywą platformę {Brand}.",
    "{Domain} es un hub de orientación para acceso {Brand}, slots, cuotas A-League, crash Aviator, en vivo y caja. Pulsa Jugar ahora y confirma la plataforma live de {Brand}.",
    "{Domain} é um hub de orientação para login {Brand}, slots, odds A-League, crash Aviator, ao vivo e caixa. Toque Jogar agora e confirme a plataforma live da {Brand}.",
    "{Domain} est un hub d'orientation pour login {Brand}, machines, cotes A-League, crash Aviator, live et caisse. Touchez Jouer et confirmez la plateforme live {Brand}.",
    "{Domain} è un hub di orientamento per login {Brand}, slot, quote A-League, crash Aviator, live e cassa. Tocca Gioca ora e conferma la piattaforma live {Brand}.",
    "{Domain}, {Brand} girişi, slot, A-League oranı, Aviator crash, canlı casino ve kasa için yönlendirme hub'ıdır. Hemen oyna'ya dokunup canlı {Brand} platformunu doğrulayın.",
    "{Domain} is een oriëntatiehub voor {Brand}-login, slots, A-League-odds, Aviator-crash, livecasino en kassa. Tik Speel nu en bevestig het live {Brand}-platform.")
add("How do I log in to {Brand}?", "Wie logge ich mich bei {Brand} ein?", "Как войти в {Brand}?", "Як увійти в {Brand}?", "Jak zalogować się do {Brand}?", "¿Cómo inicio sesión en {Brand}?", "Como entro na {Brand}?", "Comment me connecter à {Brand} ?", "Come accedo a {Brand}?", "{Brand}'e nasıl giriş yaparım?", "Hoe log ik in op {Brand}?")
add("Open Play Now from {Domain}, enter your registered email or username and password on the live site, complete any security check, then confirm your account name appears in the lobby.",
    "Öffnen Sie Jetzt spielen von {Domain}, geben Sie E-Mail oder Username und Passwort auf der Live-Site ein, bestehen Sie den Check und prüfen Sie den Kontonamen in der Lobby.",
    "Откройте Играть с {Domain}, введите email или логин и пароль на живом сайте, пройдите проверку и убедитесь, что имя аккаунта в лобби.",
    "Відкрийте Грати з {Domain}, введіть email або логін і пароль на живому сайті, пройдіть перевірку й переконайтесь, що ім'я акаунта в лобі.",
    "Otwórz Graj teraz z {Domain}, wpisz e-mail lub login i hasło na żywej stronie, przejdź kontrolę i potwierdź nazwę konta w lobby.",
    "Abre Jugar ahora desde {Domain}, introduce email o usuario y contraseña en el sitio live, pasa el control y confirma el nombre en el lobby.",
    "Abra Jogar agora a partir de {Domain}, introduza email ou username e palavra-passe no site live, passe a verificação e confirme o nome no lobby.",
    "Ouvrez Jouer depuis {Domain}, saisissez e-mail ou identifiant et mot de passe sur le site live, passez le contrôle et confirmez le nom dans le lobby.",
    "Apri Gioca ora da {Domain}, inserisci email o username e password sul sito live, supera il controllo e conferma il nome in lobby.",
    "{Domain}'den Hemen oyna'yı açın, canlı sitede e-posta veya kullanıcı adı ve şifreyi girin, güvenlik kontrolünü geçin ve lobide hesap adınızı görün.",
    "Open Speel nu vanaf {Domain}, voer e-mail of gebruikersnaam en wachtwoord in op de live site, doorloop de check en bevestig je accountnaam in de lobby.")
add("Where can I find {Brand} sports odds?", "Wo finde ich {Brand}-Sportquoten?", "Где кэфы {Brand}?", "Де коеф {Brand}?", "Gdzie są kursy {Brand}?", "¿Dónde están las cuotas de {Brand}?", "Onde estão as odds da {Brand}?", "Où sont les cotes {Brand} ?", "Dove trovo le quote {Brand}?", "{Brand} spor oranları nerede?", "Waar vind ik {Brand}-sportodds?")
add("Use the sports odds board on this hub, then continue to the live {Brand} sportsbook for 1X2 and in-play markets across A-League, AFL, NRL, Premier League and Champions League.",
    "Nutzen Sie das Sportquoten-Board auf diesem Hub, dann das Live-{Brand}-Sportsbook für 1X2 und In-Play in A-League, AFL, NRL, Premier League und Champions League.",
    "Откройте доску кэфов на хабе, затем живой спортбук {Brand} для 1X2 и ин-плея по A-League, AFL, NRL, Premier League и Лиге чемпионов.",
    "Відкрийте дошку коеф на хабі, потім живий спортбук {Brand} для 1X2 і ін-плею по A-League, AFL, NRL, Premier League і Лізі чемпіонів.",
    "Użyj tablicy kursów na hubie, potem live sportsbook {Brand} na 1X2 i in-play w A-League, AFL, NRL, Premier League i Lidze Mistrzów.",
    "Usa el tablero de cuotas del hub y sigue al sportsbook live de {Brand} para 1X2 e in-play en A-League, AFL, NRL, Premier League y Champions.",
    "Use o quadro de odds neste hub e continue no sportsbook live da {Brand} para 1X2 e in-play em A-League, AFL, NRL, Premier League e Champions.",
    "Utilisez le tableau des cotes du hub, puis le sportsbook live {Brand} pour 1X2 et in-play en A-League, AFL, NRL, Premier League et Ligue des champions.",
    "Usa il board quote sull'hub, poi lo sportsbook live {Brand} per 1X2 e in-play su A-League, AFL, NRL, Premier League e Champions League.",
    "Bu hubdaki spor oran panosunu kullanın, sonra A-League, AFL, NRL, Premier League ve Şampiyonlar Ligi için canlı {Brand} sportsbook'a geçin.",
    "Gebruik het sportoddsbord op deze hub en ga door naar het live {Brand}-sportsbook voor 1X2 en in-play in A-League, AFL, NRL, Premier League en Champions League.")
add("Does {Brand} offer slots and crash games?", "Bietet {Brand} Slots und Crash-Spiele?", "Есть ли в {Brand} слоты и краш?", "Чи є в {Brand} слоти й краш?", "Czy {Brand} ma sloty i crash?", "¿{Brand} ofrece slots y crash?", "A {Brand} tem slots e crash?", "{Brand} propose-t-il machines et crash ?", "{Brand} offre slot e crash?", "{Brand}'te slot ve crash var mı?", "Biedt {Brand} slots en crash?")
add("Yes. Big Bass Bonanza, Wolf Gold, The Dog House and Aviator-style crash titles are listed here so you can search them after login. Set a session budget before you play.",
    "Ja. Big Bass Bonanza, Wolf Gold, The Dog House und Aviator-Crash sind hier markiert, damit Sie sie nach Login suchen. Vor dem Spiel ein Session-Budget setzen.",
    "Да. Big Bass Bonanza, Wolf Gold, The Dog House и краш в стиле Aviator выделены — ищите их после входа. Задайте бюджет сессии до игры.",
    "Так. Big Bass Bonanza, Wolf Gold, The Dog House і краш у стилі Aviator виділені — шукайте їх після входу. Задайте бюджет сесії до гри.",
    "Tak. Big Bass Bonanza, Wolf Gold, The Dog House i crash w stylu Aviator są tu wyróżnione — szukaj ich po logowaniu. Ustaw budżet sesji przed grą.",
    "Sí. Big Bass Bonanza, Wolf Gold, The Dog House y crash estilo Aviator están listados para buscarlos tras el login. Fija presupuesto de sesión antes de jugar.",
    "Sim. Big Bass Bonanza, Wolf Gold, The Dog House e crash estilo Aviator estão listados para os procurar após o login. Defina orçamento de sessão antes de jogar.",
    "Oui. Big Bass Bonanza, Wolf Gold, The Dog House et crash style Aviator sont listés pour les chercher après connexion. Fixez un budget de session avant de jouer.",
    "Sì. Big Bass Bonanza, Wolf Gold, The Dog House e crash stile Aviator sono elencati per cercarli dopo il login. Imposta un budget di sessione prima di giocare.",
    "Evet. Big Bass Bonanza, Wolf Gold, The Dog House ve Aviator tarzı crash burada listelenir; girişten sonra arayın. Oynamadan önce seans bütçesi koyun.",
    "Ja. Big Bass Bonanza, Wolf Gold, The Dog House en Aviator-achtige crash staan hier zodat je ze na login zoekt. Zet een sessiebudget vóór je speelt.")
add("How do deposits and withdrawals work?", "Wie funktionieren Ein- und Auszahlungen?", "Как работают депозит и вывод?", "Як працюють депозит і вивід?", "Jak działają wpłaty i wypłaty?", "¿Cómo funcionan depósitos y retiros?", "Como funcionam depósitos e levantamentos?", "Comment marchent dépôts et retraits ?", "Come funzionano depositi e prelievi?", "Yatırma ve çekme nasıl çalışır?", "Hoe werken storten en opnemen?")
add("Fund via the cashier after login, complete KYC early if prompted, and use the same methods for withdrawals. Keep billing details consistent with your profile.",
    "Nach Login über die Kasse einzahlen, KYC früh erledigen und dieselben Methoden für Auszahlungen nutzen. Rechnungsdaten zum Profil passend halten.",
    "Пополняйте кассу после входа, рано пройдите KYC и выводите тем же методом. Платёжные данные должны совпадать с профилем.",
    "Поповнюйте касу після входу, рано пройдіть KYC і виводьте тим самим методом. Платіжні дані мають збігатися з профілем.",
    "Doładuj kasę po logowaniu, wcześnie zrób KYC i wypłacaj tą samą metodą. Dane billingowe muszą zgadzać się z profilem.",
    "Fondea por caja tras el login, completa KYC pronto y retira por el mismo método. Los datos de facturación deben coincidir con el perfil.",
    "Carregue a caixa após o login, conclua o KYC cedo e levante pelo mesmo método. Os dados de faturação devem coincidir com o perfil.",
    "Alimentez la caisse après connexion, terminez le KYC tôt et retirez par la même méthode. Les données de facturation doivent coller au profil.",
    "Carica la cassa dopo il login, completa il KYC presto e preleva con lo stesso metodo. I dati di fatturazione devono coincidere col profilo.",
    "Girişten sonra kasadan yatırın, istenirse KYC'yi erken bitirin ve çekimde aynı yöntemi kullanın. Fatura bilgileri profille uyumlu olsun.",
    "Stort via de kassa na login, rond KYC vroeg af en neem op via dezelfde methode. Factuurgegevens moeten bij je profiel passen.")
add("Is {Brand} available on mobile?", "Ist {Brand} mobil verfügbar?", "Есть ли {Brand} на мобильном?", "Чи є {Brand} на мобільному?", "Czy {Brand} działa na mobile?", "¿{Brand} está en móvil?", "A {Brand} está no telemóvel?", "{Brand} est-il dispo sur mobile ?", "{Brand} è disponibile su mobile?", "{Brand} mobilde var mı?", "Is {Brand} beschikbaar op mobiel?")
add("One account works on phone and desktop browsers. Prefer a stable connection, avoid shared devices, and log out after cash sessions on borrowed phones.",
    "Ein Konto gilt für Handy- und Desktop-Browser. Stabile Verbindung bevorzugen, geteilte Geräte meiden, nach Cash-Sessions auf fremden Handys abmelden.",
    "Один аккаунт на телефоне и ПК. Стабильная связь, не чужие устройства, выход после кэш-сессий на чужом телефоне.",
    "Один акаунт на телефоні й ПК. Стабільний зв'язок, не чужі пристрої, вихід після кеш-сесій на чужому телефоні.",
    "Jedno konto na telefonie i desktopie. Stabilne łącze, unikaj współdzielonych urządzeń, wyloguj się po sesji cash na pożyczonym telefonie.",
    "Una cuenta vale en móvil y escritorio. Conexión estable, evita dispositivos compartidos y cierra sesión en teléfonos prestados.",
    "Uma conta no telemóvel e no desktop. Ligação estável, evite dispositivos partilhados e termine sessão em telemóveis emprestados.",
    "Un compte sur mobile et ordinateur. Connexion stable, évitez les appareils partagés, déconnectez-vous sur un téléphone emprunté.",
    "Un account su telefono e desktop. Connessione stabile, evita device condivisi e fai logout sui telefoni in prestito.",
    "Tek hesap telefon ve masaüstünde çalışır. Kararlı bağlantı, paylaşılan cihazdan kaçının, ödünç telefonda nakit seans sonrası çıkış yapın.",
    "Eén account werkt op telefoon en desktop. Kies een stabiele verbinding, vermijd gedeelde devices en log uit na cashsessies op een geleende telefoon.")
add("Ready for {Brand}?", "Bereit für {Brand}?", "Готовы к {Brand}?", "Готові до {Brand}?", "Gotowy na {Brand}?", "¿Listo para {Brand}?", "Pronto para a {Brand}?", "Prêt pour {Brand} ?", "Pronto per {Brand}?", "{Brand}'e hazır mısınız?", "Klaar voor {Brand}?")
add("Official path to lobby, slots, odds, crash and live tables.", "Offizieller Weg zu Lobby, Slots, Quoten, Crash und Live-Tischen.", "Официальный путь в лобби, к слотам, кэфам, крашу и лайв-столам.", "Офіційний шлях у лобі, до слотів, коеф, крашу й лайв-столів.", "Oficjalna ścieżka do lobby, slotów, kursów, crash i stołów live.", "Ruta oficial a lobby, slots, cuotas, crash y mesas en vivo.", "Caminho oficial para lobby, slots, odds, crash e mesas ao vivo.", "Parcours officiel vers lobby, machines, cotes, crash et tables live.", "Percorso ufficiale verso lobby, slot, quote, crash e tavoli live.", "Lobi, slot, oran, crash ve canlı masalara resmi yol.", "Officieel pad naar lobby, slots, odds, crash en live-tafels.")
add("Hub for login, sports odds, slots, crash, live casino and cashier on {Domain}.", "Hub für Login, Sportquoten, Slots, Crash, Live Casino und Kasse auf {Domain}.", "Хаб входа, спорт-кэфов, слотов, краша, лайва и кассы на {Domain}.", "Хаб входу, спорт-коеф, слотів, крашу, лайву і каси на {Domain}.", "Hub logowania, kursów, slotów, crash, live i kasy na {Domain}.", "Hub de acceso, cuotas, slots, crash, en vivo y caja en {Domain}.", "Hub de login, odds, slots, crash, ao vivo e caixa em {Domain}.", "Hub de connexion, cotes, machines, crash, live et caisse sur {Domain}.", "Hub di accesso, quote, slot, crash, live e cassa su {Domain}.", "{Domain} üzerinde giriş, spor oranı, slot, crash, canlı casino ve kasa hub'ı.", "Hub voor login, sportodds, slots, crash, livecasino en kassa op {Domain}.")
add("18+ only. Gamble responsibly. {Domain} is an independent orientation hub and does not operate the {Brand} wallet.",
    "Nur 18+. Verantwortungsvoll spielen. {Domain} ist ein unabhängiger Orientierungs-Hub und betreibt nicht die {Brand}-Wallet.",
    "Только 18+. Играйте ответственно. {Domain} — независимый ориентир и не ведёт кошелёк {Brand}.",
    "Лише 18+. Грайте відповідально. {Domain} — незалежний орієнтир і не веде гаманець {Brand}.",
    "Tylko 18+. Graj odpowiedzialnie. {Domain} to niezależny hub i nie prowadzi portfela {Brand}.",
    "Solo 18+. Juega con responsabilidad. {Domain} es un hub independiente y no opera la cartera de {Brand}.",
    "Apenas 18+. Jogue com responsabilidade. {Domain} é um hub independente e não opera a carteira da {Brand}.",
    "18+ uniquement. Jouez de façon responsable. {Domain} est un hub indépendant et n'opère pas le portefeuille {Brand}.",
    "Solo 18+. Gioca in modo responsabile. {Domain} è un hub indipendente e non gestisce il wallet {Brand}.",
    "Yalnızca 18+. Sorumlu oynayın. {Domain} bağımsız bir yönlendirme hub'ıdır ve {Brand} cüzdanını işletmez.",
    "Alleen 18+. Speel verantwoord. {Domain} is een onafhankelijke hub en beheert de {Brand}-wallet niet.")

# write JS
meta = """  en:{name:"English",flag:"🇬🇧",code:"gb"},
  de:{name:"Deutsch",flag:"🇩🇪",code:"de"},
  ru:{name:"Русский",flag:"🇷🇺",code:"ru"},
  uk:{name:"Українська",flag:"🇺🇦",code:"ua"},
  pl:{name:"Polski",flag:"🇵🇱",code:"pl"},
  es:{name:"Español",flag:"🇪🇸",code:"es"},
  pt:{name:"Português",flag:"🇵🇹",code:"pt"},
  fr:{name:"Français",flag:"🇫🇷",code:"fr"},
  it:{name:"Italiano",flag:"🇮🇹",code:"it"},
  tr:{name:"Türkçe",flag:"🇹🇷",code:"tr"},
  nl:{name:"Nederlands",flag:"🇳🇱",code:"nl"}"""

lines = ['window.HUB_I18N_DICT = {', ' meta: {', meta, ' },', ' phrases: (function(){',
         '  function t(de,ru,uk,pl,es,pt,fr,it,tr,nl){return {de:de,ru:ru,uk:uk,pl:pl,es:es,pt:pt,fr:fr,it:it,tr:tr,nl:nl};}',
         '  return {']
for k, v in P.items():
    arr = [json.dumps(v[L], ensure_ascii=False) for L in LANGS]
    lines.append(f'{json.dumps(k, ensure_ascii=False)}: t({",".join(arr)}),')
lines.append('  };')
lines.append(' })()')
lines.append('};')
(HUB / "js" / "i18n-dict.js").write_text("\n".join(lines), encoding="utf-8")
print("i18n phrases", len(P))
