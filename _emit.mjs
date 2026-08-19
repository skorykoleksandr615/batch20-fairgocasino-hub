import { writeFileSync } from "fs";
import { fileURLToPath } from "url";
import { dirname, join } from "path";
const HUB = dirname(fileURLToPath(import.meta.url));
const OFFER = "https://dscdscds913.online/td9KPjCJ?sub_id_1=fairgocasino";
const CTA = `href="${OFFER}" rel="nofollow sponsored noopener" target="_blank"`;
const NAV = [
  ["/", "Home"], ["/fg-login.html", "Login"], ["/fg-join.html", "Register"],
  ["/fg-bonus.html", "Bonus"], ["/fg-slots.html", "Slots"], ["/fg-odds.html", "Odds"],
  ["/fg-crash.html", "Crash"], ["/fg-live.html", "Live"], ["/fg-app.html", "App"],
  ["/fg-pay.html", "Pay"], ["/fg-help.html", "Help"],
];

function head(p) {
  const c = p.file;
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${p.title}</title>
<meta name="description" content="${p.desc}">
<meta name="keywords" content="${p.keys}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="https://fairgo.casino/${c}">
<link rel="alternate" hreflang="en" href="https://fairgo.casino/${c}?lang=en">
<link rel="alternate" hreflang="de" href="https://fairgo.casino/${c}?lang=de">
<link rel="alternate" hreflang="ru" href="https://fairgo.casino/${c}?lang=ru">
<link rel="alternate" hreflang="uk" href="https://fairgo.casino/${c}?lang=uk">
<link rel="alternate" hreflang="pl" href="https://fairgo.casino/${c}?lang=pl">
<link rel="alternate" hreflang="es" href="https://fairgo.casino/${c}?lang=es">
<link rel="alternate" hreflang="pt" href="https://fairgo.casino/${c}?lang=pt">
<link rel="alternate" hreflang="fr" href="https://fairgo.casino/${c}?lang=fr">
<link rel="alternate" hreflang="it" href="https://fairgo.casino/${c}?lang=it">
<link rel="alternate" hreflang="tr" href="https://fairgo.casino/${c}?lang=tr">
<link rel="alternate" hreflang="nl" href="https://fairgo.casino/${c}?lang=nl">
<link rel="alternate" hreflang="x-default" href="https://fairgo.casino/${c}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Fair Go Casino">
<meta property="og:title" content="${p.title}">
<meta property="og:description" content="${p.desc}">
<meta property="og:url" content="https://fairgo.casino/${c}">
<meta property="og:image" content="https://fairgo.casino/assets/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${p.title}">
<meta name="twitter:description" content="${p.desc}">
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
`;
}

function header(active) {
  const links = NAV.map(([href, label]) => {
    const cls = href === active ? "nav-link is-active" : "nav-link";
    return `<a class="${cls}" href="${href}">${label}</a>`;
  }).join("");
  return `<body class="page">
<header class="site-header" id="siteHeader">
<div class="wrap header-bar">
<a class="brand" href="/" aria-label="Fair Go Casino home">
<span class="brand-mark"><img src="/assets/brand/logo.png" alt="Fair Go Casino logo" width="48" height="48"></span>
<span class="brand-copy"><span class="brand-name">Fair Go Casino</span><span class="brand-tag">Official</span></span>
</a>
<button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="siteNav" type="button" aria-label="Open menu"><span></span><span></span><span></span></button>
<nav class="site-nav" id="siteNav" aria-label="Primary">${links}</nav>
<div class="header-actions">
<div class="lang-switch" id="langSwitch"><button type="button" class="lang-switch-btn" aria-haspopup="listbox" aria-expanded="false" aria-label="Language"><img class="lang-flag-img" src="https://flagcdn.com/w40/gb.png" width="22" height="16" alt="English flag" loading="lazy" decoding="async"><span class="lang-code">EN</span><span class="lang-name" data-i18n-skip="1">English</span></button><div class="lang-switch-panel" role="listbox"></div></div>
<a class="btn btn-accent header-cta" ${CTA}>Play Now</a>
</div>
</div>
</header>
`;
}

const FOOT = `<section class="cta-band"><div class="wrap cta-inner">
<h2>Ready for Fair Go Casino?</h2>
<p>Official path to lobby, slots, odds, crash and live tables.</p>
<div class="cta-row">
<a class="btn btn-accent" ${CTA}>Play Now</a>
<a class="btn btn-ghost" href="/fg-login.html">Login guide</a>
</div>
</div></section>
<footer class="site-footer">
<div class="wrap footer-grid">
<div>
<div class="footer-brand">Fair Go Casino</div>
<p class="mute">Hub for login, sports odds, slots, crash, live casino and cashier on fairgo.casino.</p>
<a class="btn btn-accent" ${CTA}>Play Now</a>
</div>
<nav class="foot-nav" aria-label="Footer">
<a href="/">Home</a><a href="/fg-login.html">Login</a><a href="/fg-join.html">Register</a><a href="/fg-bonus.html">Bonus</a><a href="/fg-slots.html">Slots</a><a href="/fg-odds.html">Odds</a><a href="/fg-crash.html">Crash</a><a href="/fg-live.html">Live</a><a href="/fg-app.html">App</a><a href="/fg-pay.html">Pay</a><a href="/fg-help.html">Help</a>
</nav>
</div>
<p class="wrap legal">18+ only. Gamble responsibly. fairgo.casino is an independent orientation hub and does not operate the Fair Go Casino wallet.</p>
</footer>
<script src="/js/i18n-dict.js"></script>
<script src="/js/i18n.js"></script>
<script src="/js/main.js"></script>
</body>
</html>
`;

const pages = JSON.parse(await import("fs").then(fs => fs.readFileSync(join(HUB, "_pages.json"), "utf8")));

for (const p of pages) {
  const ch = p.chapters.map(([n, t, a, b]) => `<article class="chapter"><div class="chapter-n">${n}</div><h3>${t}</h3><p>${a}</p><p>${b}</p></article>`).join("");
  const faqs = p.faqs.map(([q, a]) => `<details class="faq-item"><summary>${q}</summary><p>${a}</p></details>`).join("");
  const chips = NAV.filter(([h]) => h !== "/" && h !== p.active).map(([h, l]) => `<a class="chip" href="${h}">${l}</a>`).join("");
  const html = head(p) + header(p.active) + `<section class="page-hero"><div class="wrap"><div class="page-hero-shell">
<div class="page-hero-copy"><div class="eyebrow">${p.eyebrow}</div>
<h1>${p.h1}<span>${p.span}</span></h1>
<p class="lead">${p.lead}</p>
<div class="cta-row">
<a class="btn btn-accent" ${CTA}>${p.cta}</a>
<a class="btn btn-ghost" ${CTA}>${p.cta2}</a>
</div></div>
<div class="page-hero-visual reveal"><img class="hero-img" src="/assets/pages/${p.cover}" alt="${p.cover_alt}" width="1600" height="900" loading="eager"></div>
</div></div></section>
<div class="wrap"><a class="promo-fx reveal" ${CTA}>
<span class="promo-badge">${p.badge}</span>
<div class="promo-media"><img src="/assets/promo/${p.promo}" alt="Fair Go Casino promo" width="1600" height="900" loading="lazy"></div>
<div class="promo-copy"><span class="promo-kicker">${p.kicker}</span><div class="promo-title">${p.ptitle}</div><p class="promo-sub">${p.psub}</p></div>
<span class="promo-cta">${p.pcta}</span>
</a></div>
<section class="chapters wrap"><div class="section-head"><h2>Guide chapters</h2><p class="mute">Practical steps for players.</p></div><div class="chapter-grid">${ch}</div></section>
<section class="faq wrap" id="faq"><div class="section-head"><h2>FAQ</h2><p class="mute">Straight answers for login, bonus, odds, slots, crash and cashier.</p></div><div class="faq-list">${faqs}</div></section>
<section class="related wrap"><div class="section-head"><h2>Explore more</h2></div><div class="chip-row">${chips}</div></section>
` + FOOT;
  writeFileSync(join(HUB, p.file), html, "utf8");
  console.log("wrote", p.file);
}

writeFileSync(join(HUB, "404.html"), `<!DOCTYPE html>
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
<a class="btn btn-ghost" ${CTA}>Play Now</a>
</div>
</div></section>
</body>
</html>
`, "utf8");
console.log("wrote 404");
