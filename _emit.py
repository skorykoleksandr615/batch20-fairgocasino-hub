# -*- coding: utf-8 -*-
import json, os, re, hashlib
from pathlib import Path

HUB = Path(r"C:\AndroidStudioProjects\batch20-hubs\fairgocasino")
OFFER = "https://dscdscds913.online/td9KPjCJ?sub_id_1=fairgocasino"
BRAND = "Fair Go Casino"
DOMAIN = "fairgo.casino"
CTA = f'href="{OFFER}" rel="nofollow sponsored noopener" target="_blank"'

NAV = [
    ("/", "Home"), ("/fg-login.html", "Login"), ("/fg-join.html", "Register"),
    ("/fg-bonus.html", "Bonus"), ("/fg-slots.html", "Slots"), ("/fg-odds.html", "Odds"),
    ("/fg-crash.html", "Crash"), ("/fg-live.html", "Live"), ("/fg-app.html", "App"),
    ("/fg-pay.html", "Pay"), ("/fg-help.html", "Help"),
]

HEAD_COMMON = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keys}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="https://fairgo.casino/{canon}">
<link rel="alternate" hreflang="en" href="https://fairgo.casino/{canon}?lang=en">
<link rel="alternate" hreflang="de" href="https://fairgo.casino/{canon}?lang=de">
<link rel="alternate" hreflang="ru" href="https://fairgo.casino/{canon}?lang=ru">
<link rel="alternate" hreflang="uk" href="https://fairgo.casino/{canon}?lang=uk">
<link rel="alternate" hreflang="pl" href="https://fairgo.casino/{canon}?lang=pl">
<link rel="alternate" hreflang="es" href="https://fairgo.casino/{canon}?lang=es">
<link rel="alternate" hreflang="pt" href="https://fairgo.casino/{canon}?lang=pt">
<link rel="alternate" hreflang="fr" href="https://fairgo.casino/{canon}?lang=fr">
<link rel="alternate" hreflang="it" href="https://fairgo.casino/{canon}?lang=it">
<link rel="alternate" hreflang="tr" href="https://fairgo.casino/{canon}?lang=tr">
<link rel="alternate" hreflang="nl" href="https://fairgo.casino/{canon}?lang=nl">
<link rel="alternate" hreflang="x-default" href="https://fairgo.casino/{canon}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Fair Go Casino">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://fairgo.casino/{canon}">
<meta property="og:image" content="https://fairgo.casino/assets/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="https://fairgo.casino/assets/og.jpg">
<link rel="icon" href="/favicon.ico?v=fg1" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png?v=fg1">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png?v=fg1">
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png?v=fg1">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192x192.png?v=fg1">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png?v=fg1">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Karla:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/styles.css?v=fg1">
<link rel="stylesheet" href="/css/i18n.css?v=fg1">
</head>
'''

def header(active):
    links = []
    for href, label in NAV:
        cls = "nav-link is-active" if href == active else "nav-link"
        links.append(f'<a class="{cls}" href="{href}">{label}</a>')
    return f'''<body class="page">
<header class="site-header" id="siteHeader">
<div class="wrap header-bar">
<a class="brand" href="/" aria-label="Fair Go Casino home">
<span class="brand-mark"><img src="/assets/brand/logo.png" alt="Fair Go Casino logo" width="48" height="48"></span>
<span class="brand-copy"><span class="brand-name">Fair Go Casino</span><span class="brand-tag">Official</span></span>
</a>
<button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="siteNav" type="button" aria-label="Open menu"><span></span><span></span><span></span></button>
<nav class="site-nav" id="siteNav" aria-label="Primary">{''.join(links)}</nav>
<div class="header-actions">
<div class="lang-switch" id="langSwitch"><button type="button" class="lang-switch-btn" aria-haspopup="listbox" aria-expanded="false" aria-label="Language"><img class="lang-flag-img" src="https://flagcdn.com/w40/gb.png" width="22" height="16" alt="English flag" loading="lazy" decoding="async"><span class="lang-code">EN</span><span class="lang-name" data-i18n-skip="1">English</span></button><div class="lang-switch-panel" role="listbox"></div></div>
<a class="btn btn-accent header-cta" {CTA}>Play Now</a>
</div>
</div>
</header>
'''

FOOT = f'''<section class="cta-band"><div class="wrap cta-inner">
<h2>Ready for Fair Go Casino?</h2>
<p>Official path to lobby, slots, odds, crash and live tables.</p>
<div class="cta-row">
<a class="btn btn-accent" {CTA}>Play Now</a>
<a class="btn btn-ghost" href="/fg-login.html">Login guide</a>
</div>
</div></section>
<footer class="site-footer">
<div class="wrap footer-grid">
<div>
<div class="footer-brand">Fair Go Casino</div>
<p class="mute">Hub for login, sports odds, slots, crash, live casino and cashier on fairgo.casino.</p>
<a class="btn btn-accent" {CTA}>Play Now</a>
</div>
<nav class="foot-nav" aria-label="Footer">
<a href="/">Home</a>
<a href="/fg-login.html">Login</a>
<a href="/fg-join.html">Register</a>
<a href="/fg-bonus.html">Bonus</a>
<a href="/fg-slots.html">Slots</a>
<a href="/fg-odds.html">Odds</a>
<a href="/fg-crash.html">Crash</a>
<a href="/fg-live.html">Live</a>
<a href="/fg-app.html">App</a>
<a href="/fg-pay.html">Pay</a>
<a href="/fg-help.html">Help</a>
</nav>
</div>
<p class="wrap legal">18+ only. Gamble responsibly. fairgo.casino is an independent orientation hub and does not operate the Fair Go Casino wallet.</p>
</footer>
<script src="/js/i18n-dict.js"></script>
<script src=" /js/i18n.js".replace(" ","")></script>
<script src="/js/main.js"></script>
</body>
</html>
'''
# fix the ugly replace - write clean
FOOT = f'''<section class="cta-band"><div class="wrap cta-inner">
<h2>Ready for Fair Go Casino?</h2>
<p>Official path to lobby, slots, odds, crash and live tables.</p>
<div class="cta-row">
<a class="btn btn-accent" {CTA}>Play Now</a>
<a class="btn btn-ghost" href="/fg-login.html">Login guide</a>
</div>
</div></section>
<footer class="site-footer">
<div class="wrap footer-grid">
<div>
<div class="footer-brand">Fair Go Casino</div>
<p class="mute">Hub for login, sports odds, slots, crash, live casino and cashier on fairgo.casino.</p>
<a class="btn btn-accent" {CTA}>Play Now</a>
</div>
<nav class="foot-nav" aria-label="Footer">
<a href="/">Home</a>
<a href="/fg-login.html">Login</a>
<a href="/fg-join.html">Register</a>
<a href="/fg-bonus.html">Bonus</a>
<a href="/fg-slots.html">Slots</a>
<a href="/fg-odds.html">Odds</a>
<a href="/fg-crash.html">Crash</a>
<a href="/fg-live.html">Live</a>
<a href="/fg-app.html">App</a>
<a href="/fg-pay.html">Pay</a>
<a href="/fg-help.html">Help</a>
</nav>
</div>
<p class="wrap legal">18+ only. Gamble responsibly. fairgo.casino is an independent orientation hub and does not operate the Fair Go Casino wallet.</p>
</footer>
<script src="/js/i18n-dict.js"></script>
<script src="/js/i18n.js"></script>
<script src="/js/main.js"></script>
</body>
</html>
'''

PAGES = [
 dict(
  file="fg-login.html", active="/fg-login.html",
  title="Fair Go Casino Login Guide | fairgo.casino",
  desc="Sign in to Fair Go Casino from fairgo.casino. Recovery tips, 2FA habits and lobby checks. No fake forms. 18+.",
  keys="Fair Go Casino login, Fair Go Casino sign in, fairgo.casino",
  eyebrow="Login",
  h1="Fair Go Casino Login",
  span="Official sign-in path via fairgo.casino",
  lead="Reach Fair Go Casino login from fairgo.casino without hopping mirrors. Use Play Now, enter credentials only on the live platform, then confirm your account name in the lobby.",
  cta="Open Login", cta2="Play Now",
  cover="fg-login.jpg", cover_alt="Fair Go Casino login cover",
  promo="promo-login.jpg", badge="LOGIN",
  kicker="Fair Go Casino sign-in gate",
  ptitle="Open the live lobby — never type a password here",
  psub="Credentials belong only on the live Fair Go Casino site.",
  pcta="Open Login",
  chapters=[
   ("01","Fair Go Casino login basics","Use fairgo.casino to reach the live Fair Go Casino lobby without hunting random mirrors.","Open Play Now, land on Fair Go Casino, then keep one bookmark for return visits."),
   ("02","Account readiness","Finish profile details early so KYC does not stall cashouts later.","Use a password manager and enable 2FA when the platform offers it."),
   ("03","Session discipline","Set a bankroll and a stop time before you open slots or A-League boards.","Close the session when either limit hits — do not chase."),
   ("04","Product path","Login sits alongside slots, Aviator, live tables and sports odds inside one Fair Go Casino account.","Jump from this hub with Play Now only — no fake forms here."),
   ("05","Mobile vs desktop","One login works on phone and desktop browsers for Fair Go Casino.","Prefer a private device and a stable connection for cashier steps."),
   ("06","Payments awareness","Deposit with methods you also control for withdrawals.","Keep billing name aligned with your Fair Go Casino profile."),
   ("07","Support habits","Save transaction IDs and screenshots before contacting support.","Use in-platform help after login for account-specific issues."),
   ("08","Session limits","Set deposit caps and cool-offs inside Fair Go Casino if you need tighter control.","Stop when play stops feeling recreational."),
   ("09","Return path","Bookmark fairgo.casino so you always re-enter Fair Go Casino from a known URL.","Recheck the address bar after redirects before entering credentials."),
  ],
  faqs=[
   ("How do I open Fair Go Casino from fairgo.casino?","Tap Play Now on fairgo.casino, follow through to the live Fair Go Casino site, then complete login or registration there."),
   ("Does fairgo.casino replace the Fair Go Casino lobby?","No. fairgo.casino is a guide for login, bonus path, odds, slots, crash, live casino and cashier. Real games run on Fair Go Casino after you continue."),
   ("What is covered about login?","This page explains practical login steps for Fair Go Casino players: safe entry, product location, session limits and where to continue via Play Now."),
   ("Are there fake login forms here?","No. Never enter passwords on the hub. Credentials belong only on the live Fair Go Casino site after you leave this page."),
   ("Where do I manage limits on Fair Go Casino?","Use deposit limits, reality checks and cool-offs inside the logged-in Fair Go Casino account tools."),
  ],
 ),
 dict(
  file="fg-join.html", active="/fg-join.html",
  title="Fair Go Casino Register | fairgo.casino",
  desc="Create a Fair Go Casino account from fairgo.casino. One profile for slots, A-League odds and live tables. 18+.",
  keys="Fair Go Casino register, Fair Go Casino sign up, fairgo.casino",
  eyebrow="Register",
  h1="Fair Go Casino Register",
  span="Create one account via fairgo.casino",
  lead="Register on Fair Go Casino with correct personal details, then open the welcome path only after you land on the live site. This hub has no signup form.",
  cta="Open Register", cta2="Play Now",
  cover="fg-join.jpg", cover_alt="Fair Go Casino register cover",
  promo="promo-bonus.jpg", badge="JOIN",
  kicker="Fair Go Casino join desk",
  ptitle="One profile for slots, odds and live tables",
  psub="Use real details so KYC and withdrawals stay aligned later.",
  pcta="Open Register",
  chapters=[
   ("01","Why register from fairgo.casino","Start from a known URL so you do not land on a random copy.","Play Now opens the live Fair Go Casino join flow."),
   ("02","Details that match later","Name, date of birth and address should match your payment methods.","Mismatches slow KYC and first cashouts."),
   ("03","Password hygiene","Use a unique password and a manager.","Enable 2FA if Fair Go Casino offers it after signup."),
   ("04","Welcome path after join","Open Promotions only on the live site.","Read wagering before you opt in — this hub never invents percentages."),
   ("05","Sports and casino in one","A-League boards and Big Bass sit in the same account.","You do not need a second registration for live tables."),
   ("06","Country and product availability","Confirm Fair Go Casino is offered in your region on the live site.","If a product is missing, skip it — do not hunt unofficial apps."),
   ("07","Email and phone checks","Complete verification emails so recovery works.","Keep the inbox you registered with."),
   ("08","Bankroll before first deposit","Decide a weekly limit before you fund.","Registration is not a reason to over-deposit."),
   ("09","Return bookmark","Save fairgo.casino after you join.","Re-check the address bar every time you sign in."),
  ],
  faqs=[
   ("How do I register for Fair Go Casino?","Tap Play Now on fairgo.casino, complete the live Fair Go Casino form, then confirm the lobby shows your name."),
   ("Does this hub store my signup data?","No. fairgo.casino never hosts a registration form. All details stay on the live Fair Go Casino site."),
   ("Can I use one account for slots and A-League?","Yes. One Fair Go Casino profile covers slots, crash, live casino and sports odds."),
   ("When should I complete KYC?","As soon as the live site asks. Early KYC keeps later withdrawals moving."),
   ("What if I already have an account?","Use the login guide and Play Now. Do not create a second profile."),
  ],
 ),
 dict(
  file="fg-bonus.html", active="/fg-bonus.html",
  title="Fair Go Casino Bonus Guide | fairgo.casino",
  desc="Read Fair Go Casino wagering, eligible slots and sports before you opt in. No invented percentages. 18+.",
  keys="Fair Go Casino bonus, Fair Go Casino welcome offer, fairgo.casino",
  eyebrow="Bonus",
  h1="Fair Go Casino Bonus",
  span="Welcome path after registration on fairgo.casino",
  lead="Open the Fair Go Casino welcome offer only in the live Promotions panel. Check wagering, eligible slots versus sports, max bet and expiry before you opt in.",
  cta="Open Bonus Path", cta2="Play Now",
  cover="fg-bonus.jpg", cover_alt="Fair Go Casino bonus cover",
  promo="promo-bonus.jpg", badge="BONUS",
  kicker="Fair Go Casino welcome path",
  ptitle="Read wagering before you opt in",
  psub="Eligible sports and slots are listed in the live terms after registration.",
  pcta="Open Bonus",
  chapters=[
   ("01","Find the live offer","Register or log in, then open Promotions on Fair Go Casino.","Ignore ads that invent percentages — only the lobby terms count."),
   ("02","Wagering first","Read how many times bonus or deposit must turn over.","Note which games contribute and which sit at zero."),
   ("03","Slots versus sports","Big Bass and Wolf Gold may clear faster than A-League 1X2.","Crash and live tables often contribute less — check the table."),
   ("04","Max bet while clearing","Stay under the listed max stake or the offer can void.","Set a unit size before the first spin or slip."),
   ("05","Expiry windows","Welcome paths expire. Write the date down.","Unused bonus after expiry is usually removed."),
   ("06","Opt-in choice","If terms do not fit your bankroll, skip the promo.","Cash-only play is always allowed."),
   ("07","KYC and bonus cashouts","Finish verification early so a cleared bonus can leave.","Mismatched names stall both bonus and cash withdrawals."),
   ("08","Sticky versus withdrawable","Some offers stay locked until wagering ends.","Read whether winnings become cash or stay bonus."),
   ("09","Return to this guide","Use fairgo.casino as the bookmark, then re-open Promotions.","Re-read terms if a new offer replaces the welcome path."),
  ],
  faqs=[
   ("Does fairgo.casino list bonus percentages?","No. This hub never invents amounts. Exact packages live only in Fair Go Casino Promotions."),
   ("Which games usually clear a welcome offer?","Often selected slots. Sports, crash and live can contribute less. Read the live weighting table."),
   ("Can I opt out?","Yes. If wagering does not fit your plan, skip the offer and play cash-only."),
   ("When should I do KYC for a bonus?","As soon as the cashier or support asks — before you try to withdraw cleared funds."),
   ("Where do I claim?","Only on the live Fair Go Casino site after Play Now from fairgo.casino."),
  ],
 ),
 dict(
  file="fg-slots.html", active="/fg-slots.html",
  title="Fair Go Casino Slots — Big Bass, Wolf Gold | fairgo.casino",
  desc="Search Big Bass Bonanza, Wolf Gold, Great Rhino Megaways and The Dog House after Fair Go Casino login. 18+.",
  keys="Fair Go Casino slots, Big Bass Bonanza, Wolf Gold, The Dog House, fairgo.casino",
  eyebrow="Slots",
  h1="Fair Go Casino Slots",
  span="Big Bass, Wolf Gold and more after login",
  lead="Search real top titles in the Fair Go Casino catalog: Big Bass Bonanza, Wolf Gold, Great Rhino Megaways, Buffalo King, The Dog House and Wild West Gold. Set a spin budget first.",
  cta="Open Slots", cta2="Play Now",
  cover="fg-slots.jpg", cover_alt="Fair Go Casino slots cover",
  promo="promo-slots.jpg", badge="SLOTS",
  kicker="Fair Go Casino reel floor",
  ptitle="Spin Big Bass and Wolf Gold after login",
  psub="Search the real titles listed on this hub, set a spin budget, then open Fair Go Casino.",
  pcta="Spin on Fair Go Casino",
  chapters=[
   ("01","Search after login","Open the Fair Go Casino lobby and type the exact title.","Do not trust cloned names on unofficial sites."),
   ("02","Big Bass Bonanza","A fishing slot with collect features.","Set a spin size you can repeat for a full session."),
   ("03","Wolf Gold and Buffalo King","Desert and plains titles with different volatility.","Read paytable notes before you raise the stake."),
   ("04","Great Rhino Megaways","More ways means swingier sessions.","Cap the number of spins before you start."),
   ("05","The Dog House and Wild West Gold","Both are popular Pragmatic-style searches.","Keep one title per session if you tilt easily."),
   ("06","Providers on the strip","Pragmatic Play, NetEnt, Play'n GO and Hacksaw sit on the home strip.","Tap a studio chip only to reach the live offer."),
   ("07","Bonus weighting","Confirm the slot still contributes if you play with a welcome offer.","Some titles sit at reduced or zero weight."),
   ("08","Session stop","Pick a loss cap and a time cap.","Leave when either hits — do not chase a bonus round."),
   ("09","Mobile reels","The same catalog opens in a phone browser.","Prefer Wi-Fi or a stable connection for long sessions."),
  ],
  faqs=[
   ("Which slots should I search first on Fair Go Casino?","Start with Big Bass Bonanza, Wolf Gold, Great Rhino Megaways, Buffalo King, The Dog House and Wild West Gold."),
   ("Are these titles real?","Yes. They are widely known studio games, not invented names for this hub."),
   ("Do I play slots on fairgo.casino?","No. This hub only orients you. Real spins run after Play Now on Fair Go Casino."),
   ("How do I set a spin budget?","Decide a session amount before the first spin and stop when it is gone."),
   ("Where are the studios?","The home providers strip lists Pragmatic Play, Evolution, NetEnt and more — each chip opens the offer."),
  ],
 ),
 dict(
  file="fg-odds.html", active="/fg-odds.html",
  title="Fair Go Casino Odds — A-League, AFL, NRL | fairgo.casino",
  desc="Compare Fair Go Casino 1X2 samples for A-League, AFL, NRL, Premier League and Champions League. 18+.",
  keys="Fair Go Casino odds, A-League odds, AFL, NRL, fairgo.casino",
  eyebrow="Odds",
  h1="Fair Go Casino Odds",
  span="A-League, AFL and NRL boards after login",
  lead="Use the sample 1X2 board on fairgo.casino, then lock the slip inside Fair Go Casino. Compare prices, set a unit size and avoid chasing live swings.",
  cta="View Odds", cta2="Play Now",
  cover="fg-odds.jpg", cover_alt="Fair Go Casino odds cover",
  promo="promo-odds.jpg", badge="ODDS",
  kicker="Fair Go Casino match board",
  ptitle="Lock A-League 1X2 before kick-off",
  psub="Compare sample prices here, then place the slip inside Fair Go Casino.",
  pcta="Bet on Fair Go Casino",
  chapters=[
   ("01","Sample versus live book","Numbers on this hub are orientation samples.","Open Fair Go Casino for current 1X2, lines and in-play."),
   ("02","A-League first","Sydney FC and Melbourne City boards sit on the home grid.","Check team news before you lock a short price."),
   ("03","AFL and NRL","Two-way prices often replace a draw column.","Keep a smaller unit on derby nights."),
   ("04","Premier League and Champions League","European nights sit next to local codes.","Do not stack correlated slips just because both look short."),
   ("05","Bankroll units","1–2 percent of the sports roll per slip is a common cap.","Raise size only after a written plan, not after a win."),
   ("06","Live markets","In-play totals move fast.","If the stream lags, skip the click."),
   ("07","Bonus and odds","Min odds and sports weighting live in Promotions.","A welcome offer can exclude some leagues — read it."),
   ("08","Cash-out discipline","Cash-out is a tool, not a default.","Decide the exit before kick-off when you can."),
   ("09","One account","Sports and casino share the Fair Go Casino wallet.","Do not raid the sports bankroll to chase a slot bonus."),
  ],
  faqs=[
   ("Are the 1X2 numbers on this hub live?","No. They are samples to show layout. Place bets only inside Fair Go Casino."),
   ("Which leagues are highlighted?","A-League, AFL, NRL plus Premier League and Champions League."),
   ("How do I open the sportsbook?","Tap Place Bet or Play Now from fairgo.casino and confirm the live Fair Go Casino book."),
   ("Can I bet and spin on one account?","Yes. One Fair Go Casino profile holds sports, slots, crash and live."),
   ("What is a sensible unit?","A small fixed percent of the sports bankroll, written before the first slip."),
  ],
 ),
 dict(
  file="fg-crash.html", active="/fg-crash.html",
  title="Fair Go Casino Crash — Aviator, JetX, Mines | fairgo.casino",
  desc="Play Aviator, JetX and Mines on Fair Go Casino with a cash-out plan. Set targets before takeoff. 18+.",
  keys="Fair Go Casino Aviator, JetX, Mines, crash, fairgo.casino",
  eyebrow="Crash",
  h1="Fair Go Casino Crash",
  span="Aviator, JetX and Mines after login",
  lead="Open Aviator, JetX or Mines on Fair Go Casino only after you set a cash-out target and a unit size. Discipline beats chasing a missed exit.",
  cta="Open Crash", cta2="Play Now",
  cover="fg-crash.jpg", cover_alt="Fair Go Casino crash cover",
  promo="promo-crash.jpg", badge="CRASH",
  kicker="Fair Go Casino climb rounds",
  ptitle="Aviator and JetX cash-out rules",
  psub="Set auto cash-out before the plane climbs. Never chase a missed exit.",
  pcta="Open Crash",
  chapters=[
   ("01","Decide the exit first","Write a cash-out number before the round lifts.","Auto cash-out exists so you do not freeze."),
   ("02","Aviator","A climb-and-cash format.","One unit per round unless your written plan says otherwise."),
   ("03","JetX","Similar rhythm, different studio skin.","Do not raise size after a late crash."),
   ("04","Mines","Pick a gem count and stick to it.","Greed on the last tile is how sessions blow up."),
   ("05","Lucky Jet, Spaceman, Aviatrix","Same family of multiplier rounds.","Treat them as one bankroll, not three fresh rolls."),
   ("06","Bonus weighting","Crash often contributes little to wagering.","Check Promotions before you clear an offer here."),
   ("07","Stop rules","A three-loss stop or a time cap both work.","Leave when either hits."),
   ("08","Mobile climb","Phone browsers run the same titles.","Avoid public Wi-Fi for cash sessions."),
   ("09","Return path","Bookmark fairgo.casino, then search Aviator in the lobby.","Recheck the URL before you stake."),
  ],
  faqs=[
   ("Which crash titles are listed?","Aviator, JetX, Mines, Lucky Jet, Spaceman and Aviatrix."),
   ("Should I chase a missed cash-out?","No. The next round is independent. Reset to the planned unit."),
   ("Do crash games clear bonuses?","Often at a low weight. Read the live Fair Go Casino table."),
   ("Can I set auto cash-out?","Yes on most climb titles. Set it before takeoff."),
   ("Where do I play?","Only after Play Now on the live Fair Go Casino platform."),
  ],
 ),
 dict(
  file="fg-live.html", active="/fg-live.html",
  title="Fair Go Casino Live — Crazy Time, Roulette | fairgo.casino",
  desc="Join Crazy Time, Lightning Roulette and Blackjack on Fair Go Casino after login. Keep a table budget. 18+.",
  keys="Fair Go Casino live casino, Crazy Time, Lightning Roulette, Blackjack, fairgo.casino",
  eyebrow="Live",
  h1="Fair Go Casino Live Casino",
  span="Crazy Time and Lightning Roulette after login",
  lead="Join Fair Go Casino live tables for Crazy Time, Lightning Roulette and Blackjack. Keep a table budget separate from sports slips and slot spins.",
  cta="Join Live", cta2="Play Now",
  cover="fg-live.jpg", cover_alt="Fair Go Casino live casino cover",
  promo="promo-live.jpg", badge="LIVE",
  kicker="Fair Go Casino studio floor",
  ptitle="Crazy Time and Lightning Roulette",
  psub="Join a live table after login. Keep a table budget separate from sports slips.",
  pcta="Join Live",
  chapters=[
   ("01","Seat after login","Open Fair Go Casino, then search the live lobby.","Confirm the dealer clock before you chip in."),
   ("02","Crazy Time","A game-show wheel with bonus rounds.","Cap the number of spins on the show."),
   ("03","Lightning Roulette","Multipliers hit selected numbers.","Do not chase a lightning miss with a bigger stack."),
   ("04","Blackjack","Basic strategy beats guesswork.","Leave after a set number of shoes."),
   ("05","Mega Wheel, Baccarat, Dream Catcher","Same wallet, different pace.","One table per session if you tilt."),
   ("06","Table limits","Read min and max before you sit.","A table above your unit size is a skip."),
   ("07","Bonus and live","Live often contributes little to wagering.","Clear offers on eligible slots when required."),
   ("08","Chat and privacy","Do not share personal data in chat.","Support tickets belong in the help centre."),
   ("09","Stop time","Set a clock when you sit down.","Walk when the clock ends, even mid-shoe."),
  ],
  faqs=[
   ("Which live titles are highlighted?","Crazy Time, Lightning Roulette, Blackjack, Mega Wheel, Baccarat and Dream Catcher."),
   ("Do I need a second account for live?","No. One Fair Go Casino login covers live, slots and sports."),
   ("Can I play live on a phone?","Yes. Use a stable connection and log out on shared devices."),
   ("Does live clear a welcome bonus?","Often at a reduced rate. Read the live weighting table."),
   ("Where do I join a table?","Tap Join Live or Play Now from fairgo.casino."),
  ],
 ),
 dict(
  file="fg-app.html", active="/fg-app.html",
  title="Fair Go Casino App and Mobile Lobby | fairgo.casino",
  desc="Use one Fair Go Casino account on phone or desktop from fairgo.casino. Stable connection, log out on shared devices. 18+.",
  keys="Fair Go Casino app, Fair Go Casino mobile, fairgo.casino",
  eyebrow="App",
  h1="Fair Go Casino App",
  span="Same lobby on phone and desktop",
  lead="Fair Go Casino runs as one account in a mobile or desktop browser. Prefer a stable connection, avoid shared phones, and log out after cashier steps.",
  cta="Open Mobile Lobby", cta2="Play Now",
  cover="fg-app.jpg", cover_alt="Fair Go Casino mobile cover",
  promo="promo-app.jpg", badge="APP",
  kicker="Fair Go Casino in your pocket",
  ptitle="One login on phone and desktop",
  psub="No extra app store hunt required — open the live lobby from fairgo.casino.",
  pcta="Open Mobile",
  chapters=[
   ("01","Browser first","Open Play Now from fairgo.casino on your phone.","Add a home-screen shortcut only after you confirm the URL."),
   ("02","One wallet","Slots, Aviator and A-League share the same balance.","Do not create a second mobile profile."),
   ("03","Connection","Prefer Wi-Fi or a strong mobile signal for live tables.","A drop mid-spin is why you keep screenshots."),
   ("04","Shared devices","Never stay logged in on a borrowed phone.","Log out after every cash session."),
   ("05","Notifications","If the live site offers alerts, keep them useful.","Do not let push pings chase you back into a loss."),
   ("06","Biometrics","Phone unlock is not a Fair Go Casino password.","Still use a unique account password."),
   ("07","Updates","Reload the lobby if a game stalls.","Clear cache only if support asks."),
   ("08","Cashier on mobile","Finish KYC on a large screen if uploads fail.","Use the same payment method you control."),
   ("09","Bookmark","Keep fairgo.casino as the re-entry point.","Recheck the address bar after every redirect."),
  ],
  faqs=[
   ("Is there a separate Fair Go Casino app?","Use the live mobile lobby from fairgo.casino. Follow only official install prompts on the live site."),
   ("Does mobile use a different account?","No. One Fair Go Casino profile works on phone and desktop."),
   ("Can I deposit on a phone?","Yes, via the live cashier after login. Complete KYC if asked."),
   ("What if a game freezes?","Wait for the round to settle, screenshot, then contact in-platform support."),
   ("Should I use public Wi-Fi?","Avoid it for cashier and cash sessions."),
  ],
 ),
 dict(
  file="fg-pay.html", active="/fg-pay.html",
  title="Fair Go Casino Payments and Cashier | fairgo.casino",
  desc="Deposit and withdraw on Fair Go Casino with methods you control. Finish KYC early. 18+.",
  keys="Fair Go Casino deposit, Fair Go Casino withdraw, cashier, fairgo.casino",
  eyebrow="Pay",
  h1="Fair Go Casino Payments",
  span="Cashier after login from fairgo.casino",
  lead="Fund Fair Go Casino through the live cashier after login. Use methods you also control for withdrawals and finish KYC early so cashouts are not stalled.",
  cta="Go to Cashier", cta2="Play Now",
  cover="fg-pay.jpg", cover_alt="Fair Go Casino cashier cover",
  promo="promo-pay.jpg", badge="PAY",
  kicker="Fair Go Casino cashier",
  ptitle="Deposit and withdraw in one profile",
  psub="Finish KYC early so cashouts are not stalled after a winning slip.",
  pcta="Open Cashier",
  chapters=[
   ("01","Open the live cashier","Play Now from fairgo.casino, then open Cashier.","This hub never hosts payment fields."),
   ("02","Method you control","Deposit with a rail you can also withdraw to.","Third-party wallets you do not own create delays."),
   ("03","Name match","Billing name must match the Fair Go Casino profile.","Mismatches trigger extra checks."),
   ("04","KYC early","Upload IDs when asked, not after a big win.","Clear photos speed review."),
   ("05","Limits","Set deposit caps inside account tools.","A weekly cap beats an impulse top-up."),
   ("06","Bonus and cashier","Some offers require a min deposit.","Read that number in Promotions, not in ads."),
   ("07","Withdraw path","Use the same method when the cashier allows.","Pending bets or wagering can hold a cashout."),
   ("08","Fees and time","The live cashier lists times and fees.","This hub does not invent processing hours."),
   ("09","Support tickets","Save the transaction ID before you chat.","In-platform help after login is the right desk."),
  ],
  faqs=[
   ("Does fairgo.casino take deposits?","No. Only the live Fair Go Casino cashier after Play Now."),
   ("When should I complete KYC?","As soon as the platform asks — ideally before the first large withdraw."),
   ("Can I withdraw to a different name?","Usually no. Keep billing and profile names aligned."),
   ("Why is a cashout pending?","Open bets, unfinished wagering or a KYC check are common holds."),
   ("Where do I see methods?","Inside the live Fair Go Casino cashier after login."),
  ],
 ),
 dict(
  file="fg-help.html", active="/fg-help.html",
  title="Fair Go Casino Help and Support | fairgo.casino",
  desc="Fair Go Casino support path from fairgo.casino. Limits, recovery and cashier tickets. 18+.",
  keys="Fair Go Casino help, Fair Go Casino support, fairgo.casino",
  eyebrow="Help",
  h1="Fair Go Casino Help",
  span="Support path after login on fairgo.casino",
  lead="Use Fair Go Casino in-platform help for account, cashier and game-round questions. This hub explains how to prepare a ticket — it does not reset passwords.",
  cta="Open Help Path", cta2="Play Now",
  cover="fg-help.jpg", cover_alt="Fair Go Casino help cover",
  promo="promo-pay.jpg", badge="HELP",
  kicker="Fair Go Casino support floor",
  ptitle="Prepare the ticket before you chat",
  psub="Save IDs, timestamps and screenshots. Credentials stay on the live site.",
  pcta="Open Support",
  chapters=[
   ("01","Right desk","Account issues go to Fair Go Casino support after login.","fairgo.casino cannot reset your password."),
   ("02","Recovery","Use official forgot-password on the live site.","Never send passwords to chat or email copies."),
   ("03","Game rounds","Screenshot the round ID if a spin or crash stalls.","Wait for settlement before you re-bet."),
   ("04","Cashier tickets","Include method, amount, time and transaction ID.","KYC status matters — finish it first."),
   ("05","Limits and cool-off","Ask support or open responsible-play tools for caps.","Use them before a tilt session, not after."),
   ("06","Bonus disputes","Quote the Promotions text you accepted.","This hub is not a terms substitute."),
   ("07","Device notes","Mention browser and phone model.","It shortens live-table investigations."),
   ("08","18+ and control","If play stops feeling recreational, use cool-off.","External help lines sit in the live footer."),
   ("09","Return bookmark","Re-enter via fairgo.casino.","Recheck the URL before you type credentials again."),
  ],
  faqs=[
   ("Can fairgo.casino reset my password?","No. Use Fair Go Casino recovery on the live site only."),
   ("What should I attach to a ticket?","Timestamps, transaction IDs, round IDs and screenshots."),
   ("Where are deposit limits?","Inside logged-in Fair Go Casino account or responsible-play tools."),
   ("Who operates the wallet?","Fair Go Casino on the live platform. This hub does not hold funds."),
   ("How do I get back to the lobby?","Play Now from fairgo.casino, then confirm the address bar."),
  ],
 ),
]

def chapters_html(chs):
    parts = ['<section class="chapters wrap"><div class="section-head"><h2>Guide chapters</h2><p class="mute">Practical steps for players.</p></div><div class="chapter-grid">']
    for n, t, a, b in chs:
        parts.append(f'<article class="chapter"><div class="chapter-n">{n}</div><h3>{t}</h3><p>{a}</p><p>{b}</p></article>')
    parts.append("</div></section>")
    return "".join(parts)

def faq_html(faqs):
    parts = ['<section class="faq wrap" id="faq"><div class="section-head"><h2>FAQ</h2><p class="mute">Straight answers for login, bonus, odds, slots, crash and cashier.</p></div><div class="faq-list">']
    for q, a in faqs:
        parts.append(f'<details class="faq-item"><summary>{q}</summary><p>{a}</p></details>')
    parts.append("</div></section>")
    return "".join(parts)

def related(skip):
    chips = []
    for href, label in NAV:
        if href == "/" or href == skip:
            continue
        chips.append(f'<a class="chip" href="{href}">{label}</a>')
    return f'<section class="related wrap"><div class="section-head"><h2>Explore more</h2></div><div class="chip-row">{"".join(chips)}</div></section>'

def write_page(p):
    html = HEAD_COMMON.format(
        title=p["title"], desc=p["desc"], keys=p["keys"], canon=p["file"]
    )
    html += header(p["active"])
    html += f'''<section class="page-hero"><div class="wrap"><div class="page-hero-shell">
<div class="page-hero-copy"><div class="eyebrow">{p["eyebrow"]}</div>
<h1>{p["h1"]}<span>{p["span"]}</span></h1>
<p class="lead">{p["lead"]}</p>
<div class="cta-row">
<a class="btn btn-accent" {CTA}>{p["cta"]}</a>
<a class="btn btn-ghost" {CTA}>{p["cta2"]}</a>
</div></div>
<div class="page-hero-visual reveal"><img class="hero-img" src="/assets/pages/{p["cover"]}" alt="{p["cover_alt"]}" width="1600" height="900" loading="eager"></div>
</div></div></section>
<div class="wrap"><a class="promo-fx reveal" {CTA}>
<span class="promo-badge">{p["badge"]}</span>
<div class="promo-media"><img src="/assets/promo/{p["promo"]}" alt="Fair Go Casino promo" width="1600" height="900" loading="lazy"></div>
<div class="promo-copy"><span class="promo-kicker">{p["kicker"]}</span><div class="promo-title">{p["ptitle"]}</div><p class="promo-sub">{p["psub"]}</p></div>
<span class="promo-cta">{p["pcta"]}</span>
</a></div>
'''
    html += chapters_html(p["chapters"])
    html += faq_html(p["faqs"])
    html += related(p["active"])
    html += FOOT
    (HUB / p["file"]).write_text(html, encoding="utf-8")

# --- 404 ---
def write_404():
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found | Fair Go Casino</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="https://fairgo.casino/">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="stylesheet" href="/css/styles.css">
</head>
<body class="page">
<header class="site-header" id="siteHeader">
<div class="wrap header-bar">
<a class="brand" href="/" aria-label="Fair Go Casino home">
<span class="brand-mark"><img src="/assets/brand/logo.png" alt="Fair Go Casino logo" width="48" height="48"></span>
<span class="brand-copy"><span class="brand-name">Fair Go Casino</span><span class="brand-tag">Official</span></span>
</a>
</div>
</header>
<section class="page-hero"><div class="wrap">
<h1>Page not found<span>This URL is not on fairgo.casino</span></h1>
<p class="lead">Use the menu to open Fair Go Casino login, odds, slots, crash or live casino.</p>
<div class="cta-row">
<a class="btn btn-accent" href="/">Home</a>
<a class="btn btn-ghost" href="''' + OFFER + '''" rel="nofollow sponsored noopener" target="_blank">Play Now</a>
</div>
</div></section>
</body>
</html>
'''
    (HUB / "404.html").write_text(html, encoding="utf-8")

for p in PAGES:
    write_page(p)
write_404()
print("pages written", len(PAGES) + 1)
