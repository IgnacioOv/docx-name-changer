from docx import Document
import sys


def main():
    name = sys.argv[1]
    name_string = "Estimado " + name

    document = Document("test.docx")
    paragraph = document.paragraphs[0]

    paragraph.text = name_string

    document.save(f"carta_{name}.docx")


if __name__ == "__main__":
    main()
