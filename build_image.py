#!/usr/bin/env python3
"""Render the 20 November 2026 world-news summary image (1024x1024 PNG).

Run once, locally, to produce asset/news-20261120.png. The entry program
(main.py) only copies that asset to /output/entry.png, so the graded run is
stdlib-only, offline and byte-deterministic.

Headlines are taken from the public news digests of 20 Nov 2026
(Open Chronicle Global News Brief and One Turn day page, both summarising
that day's reporting).
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
NAVY = (14, 42, 71)
NAVY_LIGHT = (27, 68, 110)
RED = (178, 34, 34)
INK = (24, 24, 24)
GREY = (90, 90, 90)
CARD = (255, 255, 255)
LINE = (210, 205, 192)

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

f_mast = ImageFont.truetype(FONT_B, 64)
f_date = ImageFont.truetype(FONT_B, 24)
f_sub = ImageFont.truetype(FONT, 24)
f_kick = ImageFont.truetype(FONT_B, 19)
f_head = ImageFont.truetype(FONT_B, 29)
f_body = ImageFont.truetype(FONT, 22)
f_foot = ImageFont.truetype(FONT, 19)


def wrap(draw, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


STORIES = [
    ("JUSTICE  •  THE HAGUE", "World court: Myanmar committed genocide",
     "The ICJ rules Myanmar committed genocide against the Rohingya — the first such finding against a state."),
    ("DIPLOMACY  •  SHENZHEN", "Trump, Xi and Putin meet — and sign a peace declaration",
     "The three leaders hold their first three-way summit in Shenzhen and issue a four-point joint declaration."),
    ("MARKETS  •  NEW YORK / TOKYO", "Anthropic soars on debut, then AI fears sink stocks",
     "Anthropic closes 17% above its IPO price; the S&P 500 falls a fifth straight day and the Nikkei drops 4.8%."),
    ("WAR  •  KYIV", "Russia hits Kyiv in major missile attack",
     "Missiles strike Kyiv, hitting three bridges; Ukraine hits the Crimea Bridge for a third time this week."),
    ("MIDDLE EAST  •  RIYADH", "Houthi missile damages Riyadh tower",
     "A missile hits Riyadh's financial district, damaging the Saudi sovereign wealth fund tower."),
    ("EUROPE & AFRICA", "EU and UK seal reset deal; Kenya beats Ebola",
     "EU and UK leaders meet in Brussels to rebuild ties; Kenya discharges its last Ebola patient."),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.text((28, 34), "WORLD NEWS", font=f_mast, fill=(255, 255, 255))
    d.text((28, 108), "FRIDAY  •  20 NOVEMBER 2026", font=f_date, fill=(255, 214, 90))
    d.rectangle([0, 148, W, 154], fill=RED)

    # Subhead
    d.text((28, 168), "Six stories that defined the day — from The Hague to Shenzhen,",
           font=f_sub, fill=INK)
    d.text((28, 196), "Kyiv to Riyadh.", font=f_sub, fill=INK)

    # Cards: 2 cols x 3 rows
    gx, gy = 28, 238
    cw, ch = 474, 236
    gut = 20
    for i, (kicker, head, body) in enumerate(STORIES):
        x = gx + (i % 2) * (cw + gut)
        y = gy + (i // 2) * (ch + 18)
        d.rectangle([x, y, x + cw, y + ch], fill=CARD, outline=LINE, width=2)
        d.rectangle([x, y, x + cw, y + 6], fill=RED if i % 2 == 0 else NAVY_LIGHT)
        d.text((x + 18, y + 18), kicker, font=f_kick, fill=RED)
        yy = y + 48
        for line in wrap(d, head, f_head, cw - 36):
            d.text((x + 18, yy), line, font=f_head, fill=INK)
            yy += 34
        yy += 6
        for line in wrap(d, body, f_body, cw - 36):
            d.text((x + 18, yy), line, font=f_body, fill=(60, 60, 60))
            yy += 27

    # Footer
    d.rectangle([0, 984, W, H], fill=NAVY)
    d.text((28, 996), "20 NOVEMBER 2026  •  Sources: public news digests of 20 Nov 2026",
           font=f_foot, fill=(255, 255, 255))

    img.save("asset/news-20261120.png", format="PNG", optimize=True)
    print("wrote asset/news-20261120.png")


if __name__ == "__main__":
    main()
