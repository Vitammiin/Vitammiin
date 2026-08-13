#!/usr/bin/env python3
"""Генератор SVG-карточек профиля GitHub — Apple-стиль, чёрный фон, неоновая бирюза."""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(OUT, exist_ok=True)

FONT = "'SF Pro Display','SF Pro Text',-apple-system,BlinkMacSystemFont,'Helvetica Neue',Inter,Arial,sans-serif"
MONO = "ui-monospace,'SF Mono','JetBrains Mono',Menlo,Consolas,monospace"

TEXT, TEXT2, TEXT3 = "#F5F5F7", "#A1A1A6", "#8E8E93"
NEON, NEON2, NEON3 = "#2DE8DC", "#00C2B8", "#7FF7EE"
CARD = "#0A0B0D"


def defs_common(pfx):
    """Общие градиенты/фильтры: неоновое свечение, hairline-рамки, стеклянный блик."""
    return f'''
    <linearGradient id="{pfx}-hair" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{NEON}" stop-opacity="0.34"/>
      <stop offset="45%" stop-color="#FFFFFF" stop-opacity="0.10"/>
      <stop offset="100%" stop-color="{NEON}" stop-opacity="0.07"/>
    </linearGradient>
    <linearGradient id="{pfx}-neon" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{NEON3}"/>
      <stop offset="100%" stop-color="{NEON2}"/>
    </linearGradient>
    <linearGradient id="{pfx}-title" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#C9CDD2"/>
    </linearGradient>
    <linearGradient id="{pfx}-rail" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{NEON}" stop-opacity="0"/>
      <stop offset="50%" stop-color="{NEON}" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="{NEON}" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="{pfx}-halo" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{NEON}" stop-opacity="0.30"/>
      <stop offset="60%" stop-color="{NEON2}" stop-opacity="0.07"/>
      <stop offset="100%" stop-color="{NEON2}" stop-opacity="0"/>
    </radialGradient>
    <filter id="{pfx}-glow" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="6" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="{pfx}-soft" x="-80%" y="-80%" width="260%" height="260%">
      <feGaussianBlur stdDeviation="14"/>
    </filter>'''


def shell(pfx, w, h, body, rx=26):
    """Чёрная панель с hairline-рамкой и верхней световой рейкой."""
    return f'''  <g clip-path="url(#{pfx}-clip)">
    <rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{rx}" fill="#000000"/>
{body}
    <rect x="1" y="1" width="{w-2}" height="1.2" fill="url(#{pfx}-rail)" opacity="0.75"/>
  </g>
  <rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{rx}" fill="none" stroke="url(#{pfx}-hair)" stroke-width="1.1"/>'''


def wrap(pfx, w, h, defs, body, label, rx=26):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none" role="img" aria-label="{label}">
  <title>{label}</title>
  <defs>
    <clipPath id="{pfx}-clip"><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{rx}"/></clipPath>{defs_common(pfx)}{defs}
    <style>
      .t {{ font-family: {FONT}; }}
      .k {{ font-family: {MONO}; }}
{ANIM}
    </style>
  </defs>
{shell(pfx, w, h, body, rx)}
</svg>
'''


# Анимации: элемент виден по умолчанию, анимация лишь добавляет появление
ANIM = """      @keyframes rise { from { opacity:0; transform: translateY(10px); } to { opacity:1; transform: translateY(0); } }
      @keyframes breathe { 0%,100% { opacity:.55; } 50% { opacity:1; } }
      @keyframes float { 0%,100% { transform: translate(0,0); } 50% { transform: translate(22px,-12px); } }
      @keyframes float2 { 0%,100% { transform: translate(0,0); } 50% { transform: translate(-18px,14px); } }
      @keyframes spin { to { transform: rotate(360deg); } }
      @keyframes scan { 0% { transform: translateX(-320px); } 100% { transform: translateX(900px); } }
      .a1 { animation: rise .7s ease-out; }
      .a2 { animation: rise .9s ease-out; }
      .a3 { animation: rise 1.1s ease-out; }
      .a4 { animation: rise 1.3s ease-out; }
      .a5 { animation: rise 1.5s ease-out; }
      .pulse { animation: breathe 3s ease-in-out infinite; }
      .fl { animation: float 20s ease-in-out infinite; }
      .fl2 { animation: float2 24s ease-in-out infinite; }
      .scan { animation: scan 9s cubic-bezier(.4,0,.2,1) infinite; }
      @media (prefers-reduced-motion: reduce) { .a1,.a2,.a3,.a4,.a5,.pulse,.fl,.fl2,.scan { animation: none; } }"""


# ─────────────────────────────────────────────  HERO
def hero():
    pfx = "h"
    defs = f'''
    <radialGradient id="{pfx}-orb" cx="50%" cy="45%" r="55%">
      <stop offset="0%" stop-color="{NEON3}" stop-opacity="0.55"/>
      <stop offset="55%" stop-color="{NEON2}" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="{NEON2}" stop-opacity="0"/>
    </radialGradient>'''
    body = f'''    <ellipse class="fl" cx="140" cy="250" rx="380" ry="220" fill="url(#{pfx}-halo)"/>
    <ellipse class="fl2" cx="720" cy="40" rx="320" ry="200" fill="url(#{pfx}-halo)" opacity="0.7"/>
    <rect class="scan" x="0" y="0" width="320" height="280" fill="url(#{pfx}-rail)" opacity="0.045"/>

    <!-- monogram -->
    <g class="a1">
      <circle cx="726" cy="140" r="86" fill="url(#{pfx}-orb)" filter="url(#{pfx}-soft)" opacity="0.85"/>
      <circle class="pulse" cx="726" cy="140" r="58" fill="none" stroke="{NEON}" stroke-opacity="0.55" stroke-width="1" filter="url(#{pfx}-glow)"/>
      <circle cx="726" cy="140" r="44" fill="#05070A" stroke="#FFFFFF" stroke-opacity="0.10"/>
      <text class="t" x="726" y="155" text-anchor="middle" font-size="38" font-weight="600" fill="url(#{pfx}-neon)" letter-spacing="0.5">A</text>
    </g>

    <!-- copy -->
    <g class="a1">
      <circle class="pulse" cx="44" cy="52" r="3.5" fill="{NEON}" filter="url(#{pfx}-glow)"/>
      <text class="t" x="58" y="56" font-size="10.5" font-weight="600" fill="{NEON}" letter-spacing="3.4">AI SYSTEMS · APPLIED AI · PRODUCTS</text>
    </g>
    <text class="t a2" x="40" y="130" font-size="60" font-weight="600" fill="url(#{pfx}-title)" letter-spacing="-1.6">Avis</text>
    <text class="t a3" x="40" y="166" font-size="17" font-weight="400" fill="{TEXT2}" letter-spacing="-0.2">I design AI systems — and ship the products they run.</text>
    <text class="t a4" x="40" y="196" font-size="13.5" font-weight="400" fill="{TEXT3}" letter-spacing="-0.1">Founder &amp; engineer<tspan fill="#48484A">   ·   </tspan>VORCL<tspan fill="#48484A">   ·   </tspan>Awallet<tspan fill="#48484A">   ·   </tspan>PULSE<tspan fill="#48484A">   ·   </tspan>AION</text>

    <line x1="40" y1="222" x2="560" y2="222" stroke="#FFFFFF" stroke-opacity="0.08"/>
    <text class="k a5" x="40" y="250" font-size="11.5" fill="{TEXT2}" opacity="0.9">TypeScript<tspan fill="#48484A">  ·  </tspan>React<tspan fill="#48484A">  ·  </tspan>Node<tspan fill="#48484A">  ·  </tspan>Expo<tspan fill="#48484A">  ·  </tspan>Python<tspan fill="#48484A">  ·  </tspan>MCP</text>'''
    return wrap(pfx, 860, 280, defs, body, "Avis — AI systems engineer, founder of VORCL, Awallet, PULSE and AION")


# ─────────────────────────────────────────────  PRODUCTS
ICONS = {
    # кошелёк
    "wallet": "M13 15h18a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3H13a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3Zm0 0v-2a2 2 0 0 1 2-2h13M27 23h4",
    # пульс
    "pulse": "M9 22h7l3.5-8 5 16 4-11 2.5 3H38",
    # нейроузел
    "node": "M22 13.6v5M19.4 24.2 14.9 26.7M24.6 24.2 29.1 26.7M25.5 21.5a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0ZM24.4 11.4a2.4 2.4 0 1 1-4.8 0 2.4 2.4 0 0 1 4.8 0ZM14.8 29.2a2.4 2.4 0 1 1-4.8 0 2.4 2.4 0 0 1 4.8 0ZM34 29.2a2.4 2.4 0 1 1-4.8 0 2.4 2.4 0 0 1 4.8 0Z",
    # искра
    "spark": "M22 10c1.6 6.4 3.6 8.4 10 10-6.4 1.6-8.4 3.6-10 10-1.6-6.4-3.6-8.4-10-10 6.4-1.6 8.4-3.6 10-10Z",
    # терминал
    "cli": "M13 16l6 6-6 6m10 2h9",
}

PRODUCTS = [
    ("wallet", "Awallet", "awallet.life", "A quiet AI finance dashboard — wallets, budgets,",
     "savings goals, subscriptions, stocks and crypto.", ["iOS", "Android", "Web"]),
    ("pulse", "PULSE", "mycom.fit", "A private fitness operating system: training, recovery,",
     "nutrition and body signals in one adaptive plan.", ["Expo", "AI coach", "Health"]),
    ("node", "VORCL", "vorcl.net", "Applied-AI engineering company — design, train, integrate",
     "and deploy production AI systems for real processes.", ["Next.js", "10 locales", "Cabinet"]),
    ("spark", "AION", "aion.work", "A personal AI companion that unites every important",
     "area of your life in one place.", ["Assistant", "Multi-modal", "Memory"]),
]


def products():
    pfx = "p"
    cw, ch, gap = 388, 186, 20
    rows = []
    for i, (icon, name, domain, d1, d2, tags) in enumerate(PRODUCTS):
        x = 32 + (i % 2) * (cw + gap)
        y = 92 + (i // 2) * (ch + gap)
        tg = ""
        tx = x + 24
        for t in tags:
            w = len(t) * 6.6 + 20
            tg += (f'<rect x="{tx:.0f}" y="{y+140}" width="{w:.0f}" height="22" rx="11" fill="#101215" '
                   f'stroke="#FFFFFF" stroke-opacity="0.09"/>'
                   f'<text class="t" x="{tx+w/2:.0f}" y="{y+155}" text-anchor="middle" font-size="10.5" fill="{TEXT2}">{t}</text>')
            tx += w + 8
        rows.append(f'''    <g class="a{min(i+1,5)}">
      <rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="22" fill="{CARD}" stroke="#FFFFFF" stroke-opacity="0.09"/>
      <path d="M{x+22} {y+1.2}h{cw-44}" stroke="#FFFFFF" stroke-opacity="0.14"/>
      <circle cx="{x+46}" cy="{y+46}" r="30" fill="url(#{pfx}-halo)" filter="url(#{pfx}-soft)"/>
      <rect x="{x+24}" y="{y+24}" width="44" height="44" rx="13" fill="#0D1114" stroke="{NEON}" stroke-opacity="0.30"/>
      <g transform="translate({x+24},{y+24}) scale(0.92) translate(2,2)">
        <path d="{ICONS[icon]}" fill="none" stroke="url(#{pfx}-neon)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </g>
      <text class="t" x="{x+84}" y="{y+44}" font-size="19" font-weight="600" fill="{TEXT}" letter-spacing="-0.3">{name}</text>
      <text class="t" x="{x+84}" y="{y+62}" font-size="11.5" font-weight="500" fill="{NEON}" letter-spacing="0.2">{domain}</text>
      <text class="t" x="{x+24}" y="{y+100}" font-size="12.5" fill="{TEXT2}">{d1}</text>
      <text class="t" x="{x+24}" y="{y+119}" font-size="12.5" fill="{TEXT2}">{d2}</text>
      {tg}
    </g>''')
    h = 92 + 2 * ch + gap + 32
    body = f'''    <ellipse class="fl2" cx="820" cy="{h}" rx="360" ry="220" fill="url(#{pfx}-halo)" opacity="0.55"/>
    <text class="t" x="32" y="50" font-size="11" font-weight="600" fill="{NEON}" letter-spacing="3.4">PRODUCTS</text>
    <text class="t" x="828" y="50" text-anchor="end" font-size="11.5" fill="{TEXT3}">live · in production</text>
    <line x1="32" y1="68" x2="828" y2="68" stroke="#FFFFFF" stroke-opacity="0.08"/>
''' + "\n".join(rows)
    return wrap(pfx, 860, h, "", body, "Products: Awallet, PULSE, VORCL, AION")


# ─────────────────────────────────────────────  STACK
STACK = [
    ("AI &amp; Agents", ["Claude Code", "MCP servers", "Multi-agent orchestration", "LLM tooling"]),
    ("Web", ["React 19", "Next.js", "TypeScript", "Tailwind"]),
    ("Mobile", ["React Native", "Expo", "EAS"]),
    ("Data &amp; Infra", ["Node.js", "Fastify", "PostgreSQL", "MongoDB", "Redis", "Docker"]),
]


def stack():
    pfx = "s"
    rows, y = [], 100
    for i, (cat, items) in enumerate(STACK):
        chips, cx = "", 190
        for t in items:
            w = len(t) * 6.9 + 26
            chips += (f'<rect x="{cx:.0f}" y="{y-16}" width="{w:.0f}" height="26" rx="13" fill="#0B0D10" '
                      f'stroke="#FFFFFF" stroke-opacity="0.10"/>'
                      f'<text class="t" x="{cx+w/2:.0f}" y="{y+1}" text-anchor="middle" font-size="11.5" fill="{TEXT2}">{t}</text>')
            cx += w + 9
        rows.append(f'''    <g class="a{min(i+1,5)}">
      <circle class="pulse" cx="40" cy="{y-4}" r="2.5" fill="{NEON}"/>
      <text class="t" x="54" y="{y}" font-size="13.5" font-weight="500" fill="{TEXT}" letter-spacing="-0.2">{cat}</text>
      {chips}
    </g>''')
        y += 52
    h = y + 4
    body = f'''    <ellipse class="fl" cx="60" cy="40" rx="300" ry="180" fill="url(#{pfx}-halo)" opacity="0.5"/>
    <text class="t" x="40" y="50" font-size="11" font-weight="600" fill="{NEON}" letter-spacing="3.4">STACK</text>
    <text class="t" x="820" y="50" text-anchor="end" font-size="11.5" fill="{TEXT3}">daily drivers</text>
    <line x1="40" y1="68" x2="820" y2="68" stroke="#FFFFFF" stroke-opacity="0.08"/>
''' + "\n".join(rows)
    return wrap(pfx, 860, h, "", body, "Stack: AI and agents, web, mobile, data and infrastructure")


# ─────────────────────────────────────────────  HIGHLIGHTS
HL = [
    ("PRODUCTS SHIPPED", "4", "live products across finance, fitness,", "AI assistants and applied AI"),
    ("CONTRIBUTIONS", "5.2K+", "commits, reviews and pull requests", "in the last 12 months"),
    ("AGENT TOOLKIT", "20+", "specialized sub-agents published", "on npm as agent-vorcl-flow"),
]


def highlights():
    pfx = "g"
    cols, x = [], 40
    for i, (label, num, l1, l2) in enumerate(HL):
        cols.append(f'''    <g class="a{i+1}">
      <text class="t" x="{x}" y="52" font-size="10" font-weight="600" fill="{TEXT3}" letter-spacing="2.6">{label}</text>
      <text class="t" x="{x}" y="112" font-size="46" font-weight="600" fill="url(#{pfx}-neon)" letter-spacing="-1.6" filter="url(#{pfx}-glow)">{num}</text>
      <text class="t" x="{x}" y="140" font-size="12.5" fill="{TEXT2}">{l1}</text>
      <text class="t" x="{x}" y="158" font-size="12.5" fill="{TEXT2}">{l2}</text>
    </g>''')
        if i < 2:
            cols.append(f'    <line x1="{x+232}" y1="34" x2="{x+232}" y2="162" stroke="#FFFFFF" stroke-opacity="0.08"/>')
        x += 272
    body = f'''    <ellipse class="fl" cx="430" cy="200" rx="420" ry="150" fill="url(#{pfx}-halo)" opacity="0.45"/>
''' + "\n".join(cols)
    return wrap(pfx, 860, 190, "", body, "Highlights: 4 products shipped, 5.2K+ contributions, 20+ sub-agents")


# ─────────────────────────────────────────────  BUTTONS
BTNS = [
    ("awallet", "Awallet", "awallet.life"),
    ("pulse", "PULSE", "mycom.fit"),
    ("vorcl", "VORCL", "vorcl.net"),
    ("aion", "AION", "aion.work"),
    ("npm", "agent-vorcl-flow", "npm package"),
    ("mail", "Email", "get in touch"),
]


def button(key, name, sub, i):
    pfx = f"b{i}"
    w, h = 268, 62
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none" role="img" aria-label="{name} — {sub}">
  <title>{name} — {sub}</title>
  <defs>
    <clipPath id="{pfx}-clip"><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="18"/></clipPath>{defs_common(pfx)}
    <style>
      .t {{ font-family: {FONT}; }}
      @keyframes breathe {{ 0%,100% {{ opacity:.5; }} 50% {{ opacity:1; }} }}
      @keyframes scan {{ 0% {{ transform: translateX(-140px); }} 100% {{ transform: translateX({w}px); }} }}
      .pulse {{ animation: breathe 3s ease-in-out infinite; }}
      .scan {{ animation: scan 6s cubic-bezier(.45,0,.25,1) infinite; }}
      @media (prefers-reduced-motion: reduce) {{ .pulse,.scan {{ animation: none; }} }}
    </style>
  </defs>
  <g clip-path="url(#{pfx}-clip)">
    <rect x="1" y="1" width="{w-2}" height="{h-2}" rx="18" fill="{CARD}"/>
    <ellipse cx="34" cy="31" rx="46" ry="34" fill="url(#{pfx}-halo)"/>
    <rect class="scan" x="0" y="0" width="140" height="{h}" fill="url(#{pfx}-rail)" opacity="0.07"/>
    <path d="M20 1.2h{w-40}" stroke="#FFFFFF" stroke-opacity="0.14"/>
    <circle class="pulse" cx="30" cy="31" r="4" fill="{NEON}" filter="url(#{pfx}-glow)"/>
    <text class="t" x="50" y="27" font-size="14.5" font-weight="600" fill="{TEXT}" letter-spacing="-0.2">{name}</text>
    <text class="t" x="50" y="45" font-size="11.5" fill="{TEXT3}">{sub}</text>
    <path d="M{w-38} 25 L{w-28} 25 L{w-28} 35 M{w-28} 25 L{w-40} 37" stroke="{NEON}" stroke-opacity="0.8" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <rect x="1" y="1" width="{w-2}" height="{h-2}" rx="18" fill="none" stroke="url(#{pfx}-hair)" stroke-width="1.1"/>
</svg>
'''


def write(name, content):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(content)
    print("✓", name, len(content), "bytes")


if __name__ == "__main__":
    for f in os.listdir(OUT):
        if f.endswith(".svg"):
            os.remove(os.path.join(OUT, f))
    write("hero.svg", hero())
    write("highlights.svg", highlights())
    write("products.svg", products())
    write("stack.svg", stack())
    for i, (key, name, sub) in enumerate(BTNS):
        write(f"btn-{key}.svg", button(key, name, sub, i))
