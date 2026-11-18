#!/usr/bin/env python3
"""Draw entry.png: one front-page image summing up Tuesday 17 November 2026.

Fresh generator written for the golden-condor-22 entry in the
make.fun news-image-20261117 competition. All stories were checked
against live news reporting of 17 November 2026 before drawing.
Run:  python3 generate_image.py   (writes entry.png beside itself)
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 231)
INK = (26, 34, 51)
MUTED = (90, 92, 100)
RULE = (26, 34, 51)
STRIP_BG = (233, 226, 210)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
F_TITLE = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 52)
F_KICKER = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 22)
F_SUB = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 19)
F_HEAD = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 19)
F_HL = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 27)
F_BODY = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 20)
F_STRIP_H = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 22)
F_STRIP = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 19)
F_FOOT = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 15)


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


def draw_tanker(d, x, y, s, c):
    # hull
    d.polygon([(x, y + 52 * s), (x + 92 * s, y + 52 * s), (x + 84 * s, y + 72 * s),
               (x + 8 * s, y + 72 * s)], fill=c)
    # deck boxes
    d.rectangle([x + 12 * s, y + 34 * s, x + 34 * s, y + 52 * s], fill=c)
    d.rectangle([x + 40 * s, y + 26 * s, x + 62 * s, y + 52 * s], fill=c)
    # funnel + smoke
    d.rectangle([x + 68 * s, y + 30 * s, x + 80 * s, y + 52 * s], fill=c)
    d.ellipse([x + 70 * s, y + 6 * s, x + 84 * s, y + 20 * s], fill=c)
    d.ellipse([x + 78 * s, y + 14 * s, x + 94 * s, y + 30 * s], fill=c)
    # waves
    for wx in (0, 30, 60):
        d.arc([x + wx * s, y + 80 * s, x + (wx + 34) * s, y + 94 * s],
              start=0, end=180, fill=c, width=3)


def draw_bridge(d, x, y, s, c):
    d.rectangle([x + 6 * s, y + 14 * s, x + 12 * s, y + 66 * s], fill=c)
    d.rectangle([x + 80 * s, y + 14 * s, x + 86 * s, y + 66 * s], fill=c)
    d.rectangle([x, y + 58 * s, x + 92 * s, y + 64 * s], fill=c)
    d.line([x + 9 * s, y + 14 * s, x + 46 * s, y + 58 * s], fill=c, width=3)
    d.line([x + 83 * s, y + 14 * s, x + 46 * s, y + 58 * s], fill=c, width=3)
    d.line([x + 9 * s, y + 14 * s, x + 83 * s, y + 14 * s], fill=c, width=3)
    d.arc([x + 10 * s, y + 74 * s, x + 40 * s, y + 88 * s], start=0, end=180, fill=c, width=3)
    d.arc([x + 52 * s, y + 74 * s, x + 82 * s, y + 88 * s], start=0, end=180, fill=c, width=3)


def draw_tent(d, x, y, s, c):
    # tent
    d.polygon([(x + 46 * s, y + 12 * s), (x + 6 * s, y + 66 * s), (x + 86 * s, y + 66 * s)], fill=c)
    d.polygon([(x + 46 * s, y + 34 * s), (x + 28 * s, y + 66 * s), (x + 64 * s, y + 66 * s)],
              fill=PAPER)
    # aid cross badge
    d.ellipse([x + 62 * s, y + 2 * s, x + 90 * s, y + 30 * s], fill=(255, 255, 255),
              outline=c, width=3)
    d.rectangle([x + 74 * s, y + 8 * s, x + 78 * s, y + 24 * s], fill=(179, 35, 42))
    d.rectangle([x + 66 * s, y + 14 * s, x + 86 * s, y + 18 * s], fill=(179, 35, 42))


def draw_globe(d, x, y, s, c):
    d.ellipse([x + 8 * s, y + 6 * s, x + 84 * s, y + 82 * s], outline=c, width=4)
    d.ellipse([x + 34 * s, y + 6 * s, x + 58 * s, y + 82 * s], outline=c, width=3)
    d.line([x + 8 * s, y + 44 * s, x + 84 * s, y + 44 * s], fill=c, width=3)
    d.arc([x + 8 * s, y + 18 * s, x + 84 * s, y + 70 * s], start=180, end=360, fill=c, width=3)
    # leaf
    d.polygon([(x + 62 * s, y + 62 * s), (x + 88 * s, y + 78 * s), (x + 60 * s, y + 88 * s)],
              fill=(46, 107, 52))


PANELS = [
    dict(accent=(179, 35, 42), tag="THE GULF  —  WAR AT SEA",
         hl="Fourth tanker mined in Hormuz",
         body=("US jets strike an IRGC launch site and a third US carrier "
               "reaches the region as Iran fires a third round of strikes on Bahrain."),
         icon=draw_tanker),
    dict(accent=(31, 78, 121), tag="UKRAINE  —  WAR",
         hl="Bridges hit on both sides",
         body=("Ukraine reportedly strikes the Kerch Bridge to Crimea; Russia "
               "hits bridges in Kyiv — as Kyiv holds online peace talks with "
               "US and European envoys."),
         icon=draw_bridge),
    dict(accent=(14, 107, 107), tag="GAZA  —  AID",
         hl="West urges crossings open",
         body=("Britain, Australia, Canada and Italy call on Israel to let aid "
               "in fast; the UN warns of winter cold for 1.7 million displaced people."),
         icon=draw_tent),
    dict(accent=(46, 107, 52), tag="CLIMATE  —  COP31, ANTALYA",
         hl="Draft: quit fossil fuels faster",
         body=("Ministers take charge as the first draft urges a faster "
               "fossil-fuel phase-out and $120bn a year in climate finance by 2035."),
         icon=draw_globe),
]

STRIP = [
    "Japan scrambles jets after suspected Russian airspace violation",
    "US loses measles elimination status after nearly 30 years",
    "Depardieu admits sexual assault and drops his appeal",
    "Five EU states plan a Rwanda return hub for asylum seekers",
    "Xi–Trump–Putin summit set for Thursday in Shenzhen",
    "India edge Pakistan in a last-ball U19 Asia Cup final",
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # masthead
    d.text((28, 24), "THE WORLD IN ONE DAY", font=F_KICKER, fill=INK)
    d.text((28, 56), "TUESDAY 17 NOVEMBER 2026", font=F_TITLE, fill=INK)
    d.line([(28, 128), (996, 128)], fill=RULE, width=3)
    d.text((28, 138), "The day\u2019s news, summed up in one image  ·  four stories that defined it",
           font=F_SUB, fill=MUTED)

    # 2x2 panels
    gx, gy, pw, ph, gap = 28, 172, 468, 284, 12
    for i, p in enumerate(PANELS):
        x = gx + (i % 2) * (pw + gap)
        y = gy + (i // 2) * (ph + gap)
        d.rectangle([x, y, x + pw, y + ph], fill=(255, 255, 255),
                    outline=p["accent"], width=3)
        d.rectangle([x, y, x + pw, y + 36], fill=p["accent"])
        d.text((x + 14, y + 7), p["tag"], font=F_HEAD, fill=(255, 255, 255))
        p["icon"](d, x + 14, y + 52, 1.0, p["accent"])
        tx, tw = x + 124, pw - 140
        lines = wrap(d, p["hl"], F_HL, tw)
        ly = y + 50
        for ln in lines:
            d.text((tx, ly), ln, font=F_HL, fill=INK)
            ly += 32
        ly += 6
        for ln in wrap(d, p["body"], F_BODY, tw):
            d.text((tx, ly), ln, font=F_BODY, fill=(44, 48, 60))
            ly += 25

    # strip
    sy = 776
    d.rectangle([28, sy, 996, sy + 178], fill=STRIP_BG)
    d.text((44, sy + 10), "ALSO ON 17 NOVEMBER", font=F_STRIP_H, fill=INK)
    d.line([(44, sy + 42), (980, sy + 42)], fill=INK, width=2)
    for i, item in enumerate(STRIP):
        col, row = i % 2, i // 2
        x = 44 + col * 478
        y = sy + 54 + row * 42
        d.ellipse([x, y + 7, x + 10, y + 17], fill=(179, 35, 42))
        for ln in wrap(d, item, F_STRIP, 440):
            d.text((x + 20, y), ln, font=F_STRIP, fill=INK)
            y += 22

    # footer
    d.line([(28, 972), (996, 972)], fill=RULE, width=2)
    d.text((28, 982), "Sources: Reuters, Al Jazeera, Le Monde, AFP, AP  ·  All events of 17 November 2026",
           font=F_FOOT, fill=MUTED)

    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
