import sys
import os
import ctypes
import pymupdf

APP_NAME = "PDF Sayfalarını Ayıkla"

def show_message(title, text, flags=0x40):
    ctypes.windll.user32.MessageBoxW(
        0,
        text,
        title,
        flags
    )

def main():

    if len(sys.argv) < 2:
        show_message(
            APP_NAME,
            "Bir PDF dosyası seçilmedi.",
            0x10
        )
        return 1

    pdf_path = os.path.abspath(sys.argv[1])

    if not os.path.isfile(pdf_path):
        show_message(
            APP_NAME,
            "PDF dosyası bulunamadı:\n\n" + pdf_path,
            0x10
        )
        return 1

    if not pdf_path.lower().endswith(".pdf"):
        show_message(
            APP_NAME,
            "Seçilen dosya PDF değil.",
            0x10
        )
        return 1

    document = None

    try:

        document = pymupdf.open(pdf_path)

        total = len(document)

        if total == 0:
            show_message(
                APP_NAME,
                "PDF dosyasında sayfa bulunamadı.",
                0x10
            )
            return 1

        base = os.path.splitext(pdf_path)[0]

        for i in range(total):

            output = f"{base}_{i + 1:03d}.pdf"

            if os.path.exists(output):
                os.remove(output)

            single = pymupdf.open()

            single.insert_pdf(
                document,
                from_page=i,
                to_page=i
            )

            single.save(output)
            single.close()

        document.close()
        document = None

        folder = os.path.dirname(pdf_path)

        show_message(
            APP_NAME,
            "şlem tamamlandı.\n\n"
            f"Toplam sayfa: {total}\n\n"
            "Dosyalar şu klasöre oluşturuldu:\n\n"
            + folder,
            0x40
        )

        return 0

    except Exception as e:

        if document is not None:
            try:
                document.close()
            except:
                pass

        show_message(
            "PDF Ayıklama Hatası",
            "PDF işlenirken hata oluştu:\n\n" + str(e),
            0x10
        )

        return 1


if __name__ == "__main__":
    sys.exit(main())
