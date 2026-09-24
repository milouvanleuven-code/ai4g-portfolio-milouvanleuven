from openai import OpenAI
from dotenv import load_dotenv
import tkinter as tk
from tkinter import filedialog
import base64
import mimetypes


# Load the API key from the .env file
load_dotenv()

client = OpenAI()


# Instructions for MoneyTranslate
instructions = """
You are MoneyTranslate, a tool that helps people understand
difficult financial information.

Explain the financial information in simple, clear language.

Always use exactly these sections:

AMOUNT:
State the amount mentioned.
If there is no amount, write "Not mentioned."

DEADLINE:
State the deadline exactly as described.
If there is no clear deadline, write "Not clearly mentioned."

WHAT DO I NEED TO DO?
Explain in simple language what the person is being asked to do.

WHAT CAN HAPPEN?
Explain what the information says could happen if the person
does not take action.
Do not invent consequences.

UNCLEAR OR MISSING INFORMATION:
Mention important information that is missing, unclear,
or difficult to read.

Rules:
- Do not give financial advice.
- Do not invent information.
- Keep amounts exactly as written.
- Do not calculate or invent dates that are not explicitly stated.
- If text in an image is unclear or unreadable, say so.
- Never guess an unreadable amount, date, account number, or deadline.
- Use short and simple sentences.
"""


# Start MoneyTranslate
print("=== MoneyTranslate ===")
print("Make difficult financial information easier to understand.\n")

print("How would you like to add your financial information?")
print("1. Paste or type the text")
print("2. Upload a photo of the letter")

choice = input("Choose 1 or 2: ")


# OPTION 1: TEXT
if choice == "1":

    print("\nPaste your financial text below.")
    print("When you are finished, type DONE on a new line.\n")

    text_lines = []

    while True:
        line = input()

        if line.strip().upper() == "DONE":
            break

        text_lines.append(line)

    financial_text = "\n".join(text_lines)

    if not financial_text.strip():
        print("\nNo text was entered.")

    else:
        print("\nMoneyTranslate is reading the text...")

        response = client.responses.create(
            model="gpt-5.6-luna",
            input=f"""
{instructions}

Financial text:
{financial_text}
"""
        )

        print("\n=== Simple explanation ===")
        print(response.output_text)


# OPTION 2: PHOTO
elif choice == "2":

    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    image_path = filedialog.askopenfilename(
        title="Choose a photo of your financial letter",
        filetypes=[
            ("Image files", "*.png *.jpg *.jpeg"),
            ("All files", "*.*")
        ]
    )

    root.destroy()

    if not image_path:
        print("\nNo photo was selected.")

    else:
        mime_type, _ = mimetypes.guess_type(image_path)

        if mime_type not in ["image/png", "image/jpeg"]:
            print("\nThis image type is not supported.")
            print("Please use a PNG, JPG, or JPEG image.")

        else:
            print("\nPhoto selected successfully.")
            print("MoneyTranslate is reading the photo...")

            with open(image_path, "rb") as image_file:
                image_base64 = base64.b64encode(
                    image_file.read()
                ).decode("utf-8")

            response = client.responses.create(
                model="gpt-5.6-luna",
                input=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "input_text",
                                "text": instructions
                            },
                            {
                                "type": "input_image",
                                "image_url": (
                                    f"data:{mime_type};base64,{image_base64}"
                                )
                            }
                        ]
                    }
                ]
            )

            print("\n=== Simple explanation ===")
            print(response.output_text)


# INVALID CHOICE
else:
    print("\nPlease restart MoneyTranslate and choose 1 or 2.")