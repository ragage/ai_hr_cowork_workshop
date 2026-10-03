"""Draw the 'select the Download icon' hint image used in the guides, emails, and decks.

A stylized GitHub file header: file name on the left, the Raw / Copy / Download / Edit buttons on the right,
with the Download button highlighted, its "Download raw file" tooltip, and a pointer.
Output: reference/media/download-hint.png (3x scale, 400 dpi so Word shows it at about 4.8 in wide).
"""
import pathlib

from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT = str(pathlib.Path(__file__).resolve().parents[1] / "reference" / "media" / "download-hint.png")
S = 3                      # render scale
W, H = 640, 190            # logical size
F = r"C:\Windows\Fonts"
INK, MUTED, BORDER, BTN, BLUE = (31, 35, 40), (89, 99, 110), (209, 217, 224), (246, 248, 250), (9, 105, 218)
PLUM, PURPLE = (59, 16, 65), (128, 100, 162)


def font(name, size):
    return ImageFont.truetype(f"{F}\\{name}", int(size * S))


def R(*v):
    return [int(x * S) for x in v]


def shadow_layer(box, radius, blur, color, spread=0):
    layer = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
    x0, y0, x1, y1 = box
    ImageDraw.Draw(layer).rounded_rectangle(R(x0 - spread, y0 - spread, x1 + spread, y1 + spread),
                                            radius=radius * S, fill=color)
    return layer.filter(ImageFilter.GaussianBlur(blur * S))


def glyph(d, cx, cy, ch, size, fill):
    f = font("SegoeIcons.ttf", size)
    d.text((cx * S, cy * S), ch, font=f, fill=fill, anchor="mm")


img = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))

# Card with a soft brand gradient
grad = Image.new("RGBA", (W * S, H * S))
gd = ImageDraw.Draw(grad)
for x in range(W * S):
    t = x / (W * S)
    c = tuple(int(a + (b - a) * t) for a, b in zip((250, 245, 253), (238, 245, 253)))
    gd.line([(x, 0), (x, H * S)], fill=c + (255,))
mask = Image.new("L", (W * S, H * S), 0)
ImageDraw.Draw(mask).rounded_rectangle(R(4, 4, W - 4, H - 4), radius=16 * S, fill=255)
img.alpha_composite(shadow_layer((4, 6, W - 4, H - 4), 16, 3, (60, 30, 80, 40)))
img.paste(grad, (0, 0), mask)
d = ImageDraw.Draw(img)
d.rounded_rectangle(R(4, 4, W - 4, H - 4), radius=16 * S, outline=(226, 214, 236), width=S)

# Headline
d.rounded_rectangle(R(26, 24, 66, 44), radius=10 * S, fill=PLUM)
d.text(R(46, 34), "TIP", font=font("segoeuib.ttf", 10.5), fill="white", anchor="mm")
d.text(R(76, 34), "Downloading from GitHub", font=font("segoeuib.ttf", 17), fill=INK, anchor="lm")
d.text(R(26, 58), "If a link opens the file on GitHub, select the", font=font("segoeui.ttf", 12.5), fill=MUTED)
d.text(R(26, 76), "Download icon at the top right of the file.", font=font("segoeui.ttf", 12.5), fill=MUTED)

# File header bar
bar = (20, 112, W - 20, 168)
img.alpha_composite(shadow_layer(bar, 10, 2.5, (0, 0, 0, 28)))
d = ImageDraw.Draw(img)
d.rounded_rectangle(R(*bar), radius=10 * S, fill="white", outline=BORDER, width=S)
glyph(d, 44, 140, "\ue8a5", 16, MUTED)
d.text(R(60, 140), "participant-workbook.docx", font=font("seguisb.ttf", 13.5), fill=INK, anchor="lm")

# Buttons (right-aligned): Raw | [Copy | Download] | Edit
y0, y1 = 124, 156
d.rounded_rectangle(R(424, y0, 474, y1), radius=7 * S, fill=BTN, outline=BORDER, width=S)
d.text(R(449, 140), "Raw", font=font("seguisb.ttf", 12.5), fill=INK, anchor="mm")
d.rounded_rectangle(R(482, y0, 550, y1), radius=7 * S, fill=BTN, outline=BORDER, width=S)
d.line(R(516, y0, 516, y1), fill=BORDER, width=S)
glyph(d, 499, 140, "\ue8c8", 15, MUTED)
d.rounded_rectangle(R(558, y0, 592, y1), radius=7 * S, fill=BTN, outline=BORDER, width=S)
glyph(d, 575, 140, "\ue70f", 15, MUTED)

# Highlighted Download button: glow, blue ring, blue icon
dl = (516, y0, 550, y1)
img.alpha_composite(shadow_layer(dl, 9, 5, BLUE + (110,), spread=3))
d = ImageDraw.Draw(img)
d.rounded_rectangle(R(*dl), radius=7 * S, fill=(221, 236, 255), outline=BLUE, width=2 * S)
glyph(d, 533, 140, "\ue896", 16, BLUE)

# Tooltip above the Download button
tx0, tx1, ty0, ty1 = 470, 596, 82, 106
img.alpha_composite(shadow_layer((tx0, ty0, tx1, ty1), 7, 2.5, (0, 0, 0, 60)))
d = ImageDraw.Draw(img)
d.rounded_rectangle(R(tx0, ty0, tx1, ty1), radius=7 * S, fill=(37, 41, 46))
d.polygon(R(527, ty1 - 1, 539, ty1 - 1, 533, ty1 + 6), fill=(37, 41, 46))
d.text(R((tx0 + tx1) / 2, (ty0 + ty1) / 2), "Download raw file", font=font("segoeui.ttf", 12), fill="white", anchor="mm")

# Pointer
px, py = 541, 149
pts = [(0, 0), (0, 17), (4.2, 13.2), (7, 19.5), (9.8, 18.3), (7.1, 12.2), (12.5, 12.2)]
poly = [(px + a, py + b) for a, b in pts]
img.alpha_composite(shadow_layer((px, py, px + 12, py + 20), 3, 1.6, (0, 0, 0, 70)))
d = ImageDraw.Draw(img)
d.polygon([v for p in poly for v in R(*p)], fill="white", outline=INK, width=int(1.3 * S))

img.save(OUT, dpi=(400, 400), optimize=True)
print("saved", OUT, img.size)
