from fpdf import FPDF

# Initialize the PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

# Title
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Türkçe Ek Alıştırması – 20 Soru", ln=True)
pdf.ln(5)
pdf.set_font("Arial", size=12)

# Questions
questions = [
    "1. “Ben kahvemi sade içerim. _____ kahve istemiyorum.”",
    "   A) Sütlü   B) Sütsüz   C) Şekersiz",

    "2. “Bu sabah hava çok _____, mont giydim.”",
    "   A) Güneşli   B) Güneşsiz   C) Yağmursuz",

    "3. “Bu çorba çok _____, biraz su ekleyelim.”",
    "   A) Tuzlu   B) Tuzsuz   C) Yağsız",

    "4. “Dün gece _____ bir film izledik, hiç renk yoktu.”",
    "   A) Renkli   B) Renksiz   C) Resimli",

    "5. “O çok _____ bir insan, herkes ona güveniyor.”",
    "   A) Umutsuz   B) Umutlu   C) Paralı",

    "6. “Köyde elektrik yok, tamamen _____ bir ev.”",
    "   A) Işıksız   B) Işıklı   C) Elektrikli",

    "7. “Yağmur yağıyor, neyse ki _____ geldim.”",
    "   A) Şemsiyeli   B) Şemsiyesiz   C) Yağmurlu",

    "8. “Bu çocuk çok sessiz ama aynı zamanda _____.”",
    "   A) Sözlü   B) Sesli   C) Sessiz",

    "9. “Cebimde hiç para yok, tamamen _____ kaldım.”",
    "   A) Paralı   B) Parasız   C) Paralıyım",

    "10. “Bugün gökyüzü çok _____, dışarı çıkalım mı?”",
    "    A) Bulutlu   B) Bulutsuz   C) Yağmursuz",

    "11. “Bu dergi çok ilginç, tamamen _____.”",
    "    A) Resimli   B) Resimsiz   C) Yazılı",

    "12. “O, _____ kaldığı için zor durumda.”",
    "    A) İşsiz   B) İşli   C) İşsizli",

    "13. “Bu yemek _____, diyet yaparken iyi olur.”",
    "    A) Yağlı   B) Yağsız   C) Yağlısız",

    "14. “Bu kitap _____, okumak çok eğlenceli.”",
    "    A) Resimsiz   B) Kitapsız   C) Resimli",

    "15. “Tüm yollar _____, arabayla gidemedik.”",
    "    A) Karsız   B) Karlı   C) Karla",

    "16. “Bu peynir çok _____, bana göre değil.”",
    "    A) Tuzlu   B) Sütlü   C) Şekersiz",

    "17. “O, çok _____ biri. Hiç şaka yapmaz.”",
    "    A) Ciddili   B) Ciddisiz   C) Ciddi",

    "18. “Yeni arkadaşım _____, gözlük takıyor.”",
    "    A) Gözlüksüz   B) Gözlüklü   C) Gözlülü",

    "19. “Bu sabun tamamen doğal, _____.”",
    "    A) Kimyasallı   B) Kimyasalsız   C) Kimyasız",

    "20. “Küçükken hep _____ hayaller kurardım.”",
    "    A) Umutsuz   B) Umutlu   C) Umutsuzlu",
]

# Add questions to PDF
for line in questions:
    pdf.multi_cell(0, 10, line)

# Save the PDF
pdf.output("Turkish_Suffix_Quiz_20_Questions.pdf")