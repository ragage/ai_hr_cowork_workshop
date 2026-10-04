"""Draw the prompt-element legend (Goal · Source · Expectations · Constraints) used across the kit.

Same colors as the Word workbook (make_word_docs.py) and the deck (build_deck.py). Each element is a soft
card with a round icon (target, folder, checklist, shield), its name, and what it answers.
Outputs (reference/media/, rendered at 3x):
- prompt-key.png        one row, short descriptions (workbook, prompt library, quick-reference card), 6.5 in wide
- prompt-key-slide.png  one row, the full questions (deck slide 15), 12.23 in wide
- prompt-key-grid.png   2 x 2, names only (Prompt key corner of every exercise card), 4.62 in wide
- prompt-key-card.png   2 x 2, short descriptions (quick-reference card), 4.6 in wide
"""
import pathlib

from PIL import Image, ImageDraw, ImageFilter, ImageFont

MEDIA = pathlib.Path(__file__).resolve().parents[1] / "reference" / "media"
S = 3
F = r"C:\Windows\Fonts"
# key: name, card fill, dark (text + icon disc), icon glyph (Segoe Fluent Icons), short description, question
ELEMENTS = [
    ("Goal", "DCEBFF", "1F4E99", "\uF272", "The outcome, for whom, and why",
     "What outcome do I want, for whom, and why?"),
    ("Source", "DFF5E1", "1E6B32", "\uED25", "Files, sites, or data to use",
     "Which files, sites, or data should Cowork use?"),
    ("Expectations", "FFE9CC", "8A4B00", "\uE9D5", "What good looks like: format, length, tone",
     "What should the result look like: format, length, tone?"),
    ("Constraints", "EDE3FA", "5B2C91", "\uEA18", "What Cowork must not do",
     "What must Cowork not do: guess, invent, send?"),
]
ALT = ("Prompt key: Goal (blue) is the outcome, for whom, and why; Source (green) is the files, sites, or data to "
       "use; Expectations (orange) describe what good looks like; Constraints (purple) say what Cowork must not do.")


def rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def font(name, size):
    return ImageFont.truetype(str(pathlib.Path(F, name)), int(size * S))


def wrap(d, text, f, width):
    lines, line = [], ""
    for word in text.split():
        trial = (line + " " + word).strip()
        if d.textlength(trial, font=f) <= width * S or not line:
            line = trial
        else:
            lines.append(line)
            line = word
    return lines + [line]


def render(name, cols, card_w, card_h, gap, desc_key, name_size, desc_size, icon_d, width_in):
    m = 8  # room for the shadow
    rows = (len(ELEMENTS) + cols - 1) // cols
    W = m * 2 + cols * card_w + (cols - 1) * gap
    H = m * 2 + rows * card_h + (rows - 1) * gap
    img = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
    shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    cards = []
    for i, el in enumerate(ELEMENTS):
        x, y = m + (i % cols) * (card_w + gap), m + (i // cols) * (card_h + gap)
        cards.append((x, y, el))
        sd.rounded_rectangle([x * S, (y + 2) * S, (x + card_w) * S, (y + card_h + 2) * S],
                             radius=10 * S, fill=(0, 0, 0, 38))
    img = Image.alpha_composite(img, shadow.filter(ImageFilter.GaussianBlur(3 * S)))
    d = ImageDraw.Draw(img)
    f_name, f_desc = font("seguisb.ttf", name_size), font("segoeui.ttf", desc_size or 10)
    f_icon = font("SegoeIcons.ttf", icon_d * 0.5)
    for x, y, (label, fill, dark, glyph, short, question) in cards:
        fill, dark = rgb(fill), rgb(dark)
        tint = tuple(int(c + (255 - c) * 0.55) for c in dark)
        d.rounded_rectangle([x * S, y * S, (x + card_w) * S, (y + card_h) * S], radius=10 * S, fill=fill,
                            outline=tint, width=max(1, S))
        bar = Image.new("L", img.size, 0)  # accent bar, clipped to the card's rounded corners
        ImageDraw.Draw(bar).rounded_rectangle([x * S, y * S, (x + card_w) * S, (y + card_h) * S], radius=10 * S,
                                              fill=255)
        ImageDraw.Draw(bar).rectangle([(x + 6) * S, 0, img.size[0], img.size[1]], fill=0)
        img.paste(dark, mask=bar)
        pad = (card_h - icon_d) / 2 if desc_key is None else min(14, (card_h - icon_d) / 2)
        cx, cy = x + 6 + pad + icon_d / 2, y + card_h / 2
        d.ellipse([(cx - icon_d / 2) * S, (cy - icon_d / 2) * S, (cx + icon_d / 2) * S, (cy + icon_d / 2) * S],
                  fill=dark)
        d.text((cx * S, cy * S), glyph, font=f_icon, fill="white", anchor="mm")
        tx = cx + icon_d / 2 + 12
        if desc_key is None:
            d.text((tx * S, cy * S), label, font=f_name, fill=dark, anchor="lm")
            continue
        desc = wrap(d, short if desc_key == "short" else question, f_desc, x + card_w - tx - 10)
        line_h = desc_size * 1.3
        block = name_size * 1.25 + len(desc) * line_h
        ty = cy - block / 2
        d.text((tx * S, ty * S), label, font=f_name, fill=dark, anchor="la")
        for j, line in enumerate(desc):
            d.text((tx * S, (ty + name_size * 1.25 + j * line_h) * S), line, font=f_desc, fill=(36, 36, 36),
                   anchor="la")
    dpi = W * S / width_in
    out = MEDIA / name
    img.save(out, dpi=(dpi, dpi))
    print("saved", out.relative_to(MEDIA.parents[1]), f"({width_in} in)")


if __name__ == "__main__":
    render("prompt-key.png", 4, 236, 76, 12, "short", 17, 12.5, 40, 6.5)
    render("prompt-key-slide.png", 4, 290, 100, 14, "question", 21, 14.5, 50, 12.23)
    render("prompt-key-grid.png", 2, 225, 40, 10, None, 15, 0, 28, 4.62)
    render("prompt-key-card.png", 2, 236, 70, 10, "short", 16, 12.5, 34, 4.6)
