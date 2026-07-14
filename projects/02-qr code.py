import qrcode
from PIL import Image, ImageDraw, ImageFont

print("=" * 60)
print("              QR CODE GENERATOR")
print("=" * 60)

# User Input
data = input("🔗 Enter Website URL or Text: ").strip()

if not data:
    print("❌ Input cannot be empty!")
    exit()

# Automatically add https://
if "." in data and not data.startswith(("http://", "https://")):
    data = "https://" + data

filename = input("💾 Enter File Name: ").strip()

if filename == "":
    filename = "my_qrcode"

try:
    # ----------------------------
    # Create QR Code
    # ----------------------------
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    qr_image = qr.make_image(
        fill_color="#0B1F3F",     # Navy Blue
        back_color="white"
    ).convert("RGB")

    qr_image = qr_image.resize((320, 320))

    # ----------------------------
    # Create Background Card
    # ----------------------------
    WIDTH = 600
    HEIGHT = 750

    card = Image.new("RGB", (WIDTH, HEIGHT), "#F5F7FA")
    draw = ImageDraw.Draw(card)

    # Fonts
    try:
        title_font = ImageFont.truetype("arial.ttf", 34)
        text_font = ImageFont.truetype("arial.ttf", 22)
        small_font = ImageFont.truetype("arial.ttf", 18)
    except:
        title_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    # ----------------------------
    # Header
    # ----------------------------
    draw.rectangle((0, 0, WIDTH, 90), fill="#0B1F3F")

    draw.text(
        (170, 28),
        "QR CODE",
        fill="white",
        font=title_font
    )

    # ----------------------------
    # White QR Box
    # ----------------------------
    draw.rounded_rectangle(
        (110, 120, 490, 500),
        radius=20,
        fill="white",
        outline="#CCCCCC",
        width=2
    )

    card.paste(qr_image, (100, 130))

    # ----------------------------
    # Footer Text
    # ----------------------------
    draw.text(
        (150, 540),
        "Scan to Open the Link",
        fill="#0B1F3F",
        font=text_font
    )

    # Save
    card.save(f"{filename}.png")

    print("\n" + "=" * 60)
    print("✅ QR Code Generated Successfully!")
    print(f"📁 Saved as: {filename}.png")
    print("=" * 60)

except Exception as e:
    print("❌ Error:", e)