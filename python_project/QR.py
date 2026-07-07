import qrcode

# ---- Step 1: UPI Payment Information ----
upi_id = "7079503713@ybl"  # <-- yahan aapka UPI ID dalein
name = "Your Name"
amount = "50"  # ₹50 payment
note = "Payment for coffee"

# ---- Step 2: Generate UPI URI ----
upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR&tn={note}"

# ---- Step 3: Generate QR Code ----
qr = qrcode.make(upi_link)

# ---- Step 4: Save or Show QR Code ----
qr.save("upi_payment_qr.png")
qr.show()

print("✅ QR code generated successfully as 'upi_payment_qr.png'")
