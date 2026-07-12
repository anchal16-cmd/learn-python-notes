import qrcode

print("=" * 50)
print("          QR CODE GENERATOR")
print("=" * 50)

# Get user input
data = input("Enter a URL or text: ").strip()

if not data:
    print("❌ Error: Input cannot be empty!")
    exit()

# Automatically add https:// if it looks like a website
if (
    "." in data
    and not data.startswith("http://")
    and not data.startswith("https://")
):
    data = "https://" + data

# Get file name
filename = input("Enter file name (without extension): ").strip()

if not filename:
    filename = "my_qrcode"

try:
    # Create QR Code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    # Create image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save image
    img.save(f"{filename}.png")

    print("\n✅ QR Code generated successfully!")
    print(f"📁 File saved as: {filename}.png")
    print(f"🔗 QR Code contains: {data}")

except Exception as e:
    print("❌ Something went wrong!")
    print("Error:", e)