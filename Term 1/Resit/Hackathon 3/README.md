# Term 1 - Week 3: Hackathon 3 Resit

---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?**

The main assignment for this resit was to improve my Hackathon 3 prototype. The focus was on using a large language model through an API to create a useful application that contributes to SDG 10: Reduced Inequalities.

**What did I hand in?**

My improved MoneyTranslate 2.0 application, including the Python code, requirements file and documentation, is available in the `Hackathon 3/` folder.

**What did I find difficult, and how did I solve it?**

At first, I had difficulties connecting my Python application to the Gemini API. One model was no longer available to new users, and another temporarily returned a server error.

I solved this by checking which Gemini models were available and testing a different model.

I also found it challenging to make the application do more than simply send a question to AI and display the answer. I solved this by adding a Python function that independently compares financial amounts in the original letter with the AI explanation.

### Checklist

- [x] My workshop / homework files are in `homework/`
- [x] Everything runs without errors, or I explained what does not and why

---

## 2. Hackathon prototype -> [`Hackathon 3/`](Hackathon%203/)

**Project title:**

MoneyTranslate 2.0 – Making Financial Letters Easier to Understand

**My pair partner:**

Individual resit.

**Tool we had to use:**

Python and a large language model API (Google Gemini).

**SDG we had to address:**

SDG 10 – Reduced Inequalities.

**What problem does it solve, and for whom?**

Financial letters from organisations such as banks, municipalities and debt collection agencies can contain difficult words, complicated sentences and important financial information.

For people with limited literacy or limited Dutch language skills, understanding these letters can be challenging.

This is especially important when a letter contains a payment deadline or a warning about additional costs. Misunderstanding this information could lead to missed deadlines or unnecessary financial problems.

MoneyTranslate focuses specifically on people who struggle to read and understand financial letters.

The application aims to reduce this inequality by making important financial information easier to understand and act on.

Instead of requiring users to read and understand a complicated letter themselves, MoneyTranslate provides a simplified explanation.

**What did you build?**

I built MoneyTranslate 2.0, a Python application that uses Google Gemini to explain difficult financial letters in simple language.

The application has a user-friendly interface built with Streamlit.

Users can either paste the text of a financial letter or upload a photo of the letter. The photo option is especially important for people who struggle with reading or typing.

The application then provides six sections:

1. A simple explanation of the letter.
2. Important financial amounts.
3. Important dates and deadlines.
4. A list of actions the user should take.
5. Missing or unclear information.
6. Possible consequences mentioned in the letter.

Users can choose between Dutch and English and download the explanation.

**An important improvement compared to my original version is the independent amount verification.**

My first prototype mainly sent information to an AI model and displayed the response. This provided limited functionality beyond a normal chatbot.

In MoneyTranslate 2.0, Python also performs its own check.

Using regular expressions, the program identifies euro amounts in the original pasted text and compares them with amounts in the AI explanation.

For example, Python recognises that €1.250,00 and €1250.00 represent the same amount.

The application shows a confirmation when an amount appears in both texts and a warning when an amount is missing or appears only in the AI explanation.

This does not guarantee that the explanation is correct, but it adds an extra check instead of relying entirely on the AI response.

The verification currently works for pasted text, not uploaded photos.

I deliberately kept the Python code relatively simple so that I understand how the application works and can explain my programming choices.

**Link to the live thing (if any):**

The application currently runs locally using Streamlit. It has not been published as a public website.

The source code is available in this GitHub folder.

**How do I run it?**

1. Download the project files.

2. Make sure Python is installed.

3. Install the required packages:

   `python -m pip install -r requirements.txt`

4. Create a `.env` file in the project folder and add your own Gemini API key:

   `GEMINI_API_KEY=your_api_key_here`

5. Start the application:

   `python -m streamlit run app.py`

6. Open the local Streamlit page in your browser.

The application needs an internet connection to communicate with Gemini.

The `.env` file is not uploaded to GitHub because it contains a private API key.

**Who did what?**

I completed this resit individually.

I improved my original prototype by connecting it to Gemini, building a Streamlit interface, adding photo uploads, creating a clearer explanation structure and programming the amount verification.

I also tested the application using fictional financial letters.

For example, I tested a letter containing a payment of €1.250,00, an additional fee of €25,50 and a deadline of 20 November 2026.

Gemini correctly identified the amounts and deadline, and the Python verification confirmed that both amounts appeared in the original text.

**Ethical reflection - what are the risks of your tool? Who could it harm?**

MoneyTranslate is designed to help people who may already be in a vulnerable financial situation. This means that mistakes could have serious consequences.

**1. Incorrect AI explanations**

Gemini can misunderstand a letter or provide incorrect information. For example, it might identify the wrong payment deadline or explain a warning incorrectly.

This could cause users to miss a payment or make a financial decision based on incorrect information.

To reduce this risk, I instructed Gemini not to invent amounts, dates or consequences. I also added a Python check that compares amounts in the original pasted text with the AI explanation.

However, this check is limited. It does not verify deadlines, the meaning of amounts or information extracted from photos. Therefore, users must still check the original letter.

**2. Privacy and personal information**

Financial letters can contain sensitive information, such as names, addresses, account numbers and details about debts.

When a user submits a letter, its contents are sent to Google's Gemini API.

This creates privacy risks, especially if users do not understand what happens to their information.

For this reason, the application clearly warns users not to upload real letters containing personal information. I also used fictional letters during testing.

A real public version would need stronger privacy protection before it could safely be used with personal financial documents.

**3. Overdependence on AI**

People who struggle with reading may trust a simple AI explanation without checking the original letter.

This is particularly risky because the explanation can sound confident even when it contains mistakes.

MoneyTranslate therefore states that it is an educational prototype and should not replace professional financial or legal advice.

**4. Accessibility and inequality**

The goal of MoneyTranslate is to reduce inequality, but the application is not accessible to everyone.

For example, users still need a smartphone or computer, internet access and some digital skills.

People with very limited reading skills may also struggle with the simplified explanation.

The photo-upload function reduces the need to type a letter, but it does not solve every accessibility problem.

**5. Incorrect information in uploaded photos**

Photos can be blurry, incomplete or difficult for Gemini to read.

If an important amount or date is not visible, the AI could misunderstand the letter.

I instructed Gemini to say when information is unreadable instead of guessing.

The application currently cannot independently verify amounts extracted from photos, which is an important limitation.

**Conclusion**

I believe AI can help reduce inequalities by making complicated financial information easier to understand.

However, it should support users rather than replace their own judgement or professional assistance.

The most important lesson from this project is that a useful AI application needs more than a working API connection. It also needs a clear target group, additional functionality, testing and awareness of ethical risks.

### Checklist

- [x] Prototype code (or export / workflow file) is in `Hackathon 3/`
- [x] This week's slides are in `Hackathon 3/`
- [x] The prototype actually runs, and I wrote down how to run it
- [x] Ethical reflection written above

---

## 3. Presentation -> [`presentation/`](presentation/)

*Only fill this in for the week your group was selected to present. You need at least **one** of these across the whole term.*

- [ ] My group presented in this week
- [ ] Slides are in `presentation/`
- [ ] Proof of the live demo is in `presentation/` (recording, screenshots, or link)

**How did it go? What would I do differently next time?**

Not applicable to this individual resit.

---

## 4. Reflection

**What is the most important thing I learned this week?**

The most important thing I learned was that connecting an AI model to Python is only the beginning of building a useful application.

In my first version, I mainly focused on getting the API to work.

After receiving feedback, I realised that I needed to think more carefully about the problem, the target group and what my application actually adds.

I learned how to build a simple interface using Streamlit, how to send images to Gemini and how to use regular expressions in Python to compare financial amounts.

I also learned that it is important to understand my own code instead of making an application unnecessarily complicated.

**Where does this connect to "AI for Good"?**

MoneyTranslate connects to AI for Good through SDG 10: Reduced Inequalities.

People with limited literacy or language skills do not always have the same opportunities to understand important financial information.

AI can help make this information more accessible by translating complicated letters into simple explanations and clear action lists.

The photo-upload option also makes the application easier to use for people who have difficulty typing or copying text.

At the same time, I learned that AI for Good is not only about creating a helpful tool. It is also about understanding the risks, protecting vulnerable users and being honest about the limitations of AI.

MoneyTranslate is a small prototype, but it demonstrates how AI could support people who face barriers when dealing with financial information.

