# Term 1 - Week 4: Strings, Text & Files

---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?**
Use an LLM API (via Python) to build a tool that reduces a specific inequality. The solution must make real API calls, handle responses, and deliver something a real person could use.

Examples: a language accessibility tool, a legal or medical information explainer for non-experts, a bias checker for job postings, a tool that bridges information gaps for underrepresented groups.
**What did I hand in?**
https://dehaagsehogeschool-my.sharepoint.com/:v:/r/personal/22087354_student_hhs_nl/Documents/Bijlagen/Video%20Project%20Moneytranslate.mp4?d=wf024c6f6ca5b46c494fc89dbd4cbef87&csf=1&web=1&e=cfpCm4&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D

Video Project Moneytranslate.mp4 


**What did I find difficult, and how did I solve it?**
I found working with Python quite difficult because I have almost no programming experience yet. Especially setting up the API key, installing the right packages and understanding errors in the code took some time. I solved this by working step by step, testing small parts of the code and fixing the errors one by one.

Even though it was challenging, I really enjoyed building MoneyTranslate because I could actually see the code turn into a working tool. I also found the project personally meaningful because I sometimes struggle with understanding complicated financial letters myself. This made me realize that a tool like MoneyTranslate could actually be useful for real people instead of just being a programming exercise.

### Checklist
- [ x] My workshop / homework files are in `homework/`
- [x ] Everything runs without errors, or I explained what does not and why

---


## 2. Hackathon prototype -> [`hackathon/`](hackathon/)

> Your tool and your SDG for this hackathon are announced at the **start of Friday's class**.
> Write them down here once you know them.

**Project title:**
MoneyTranslate
**My pair partner:**
Bart Bruggeling
**Tool we had to use:**
Claude API or OpenAI API — Large language model APIs, called from your own Python code
**SDG we had to address:**
10 — Reduced Inequalities
**What problem does it solve, and for whom?**
MoneyTranslate is designed for adults in the Netherlands who have difficulty understanding written financial information, especially people with low literacy who are dealing with financial problems.
This is a significant group. Around 3 million people aged 16–75 in the Netherlands have difficulty with reading, writing and/or numeracy. The Dutch government states that limited basic skills can make everyday tasks such as understanding letters and filling in forms difficult.
The problem is even more visible among people experiencing financial difficulties. Research by the University of Groningen, together with Kredietbank Nederland and Syncasso, found that 50.3% of the participants with financial problems had difficulty reading. The research also found that people can miss important information in letters and reminders and may not take action, which can make their financial problems worse.

MoneyTranslate aims to reduce this information inequality by turning difficult financial letters into short and simple explanations. It clearly shows important information such as the amount, deadline, required action and possible consequences.

**What did you build?**
We built a Python tool that uses the OpenAI API to simplify difficult financial information. A user can either paste the text of a financial letter or upload a photo of the letter. MoneyTranslate then shows the amount, deadline, required action, possible consequences and any information that is unclear or missing.

**Link to the live thing (if any):**
https://dehaagsehogeschool-my.sharepoint.com/:v:/r/personal/22087354_student_hhs_nl/Documents/Bijlagen/Video%20Project%20Moneytranslate.mp4?d=wf024c6f6ca5b46c494fc89dbd4cbef87&csf=1&web=1&e=AOn8Wi&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D 

**How do I run it?**
1. Install Python.
2. Install the required packages with `python -m pip install openai python-dotenv`.
3. Add an OpenAI API key to a local `.env` file as `OPENAI_API_KEY=your_key_here`.
4. Run `python moneytranslate.py`.
5. Choose option 1 to paste text or option 2 to upload a photo of a financial letter.

The `.env` file containing the API key is not included in the GitHub repository for security reasons.

**Who did what?**
Bart and I worked closely together throughout the project and communicated a lot about our ideas and decisions. I focused a little more on building and testing the Python code, while Bart focused more on developing the idea and preparing the presentation. However, we discussed and worked on all parts of the project together. Overall, we divided the work fairly and had good communication and collaboration throughout the hackathon.

**Ethical reflection - what are the risks of your tool? Who could it harm?**
The biggest risk of MoneyTranslate is that the AI could incorrectly interpret important financial information. For example, it could misread an amount or misunderstand a payment deadline. This could particularly harm the people the tool is designed to help, because a user who already has difficulty understanding financial information may be less likely to notice an AI error. To reduce this risk, MoneyTranslate is instructed not to guess unclear amounts, dates or deadlines and to explicitly state when information is unclear or missing. It also does not give financial advice. However, AI can still make mistakes, so MoneyTranslate should be used as an aid for understanding a financial document and not as a replacement for the original document or professional advice.

### Checklist
- [ x] Prototype code (or export / workflow file) is in `hackathon/`
- [ x] This week's slides are in `hackathon/`
- [ x] The prototype actually runs, and I wrote down how to run it
- [ x] Ethical reflection written above

---

## 3. Presentation -> [`presentation/`](presentation/)

*Only fill this in for the week your group was selected to present. You need at least **one** of these across the whole term.*

- [ ] My group presented in this week
- [ ] Slides are in `presentation/`
- [ ] Proof of the live demo is in `presentation/` (recording, screenshots, or link)

**How did it go? What would I do differently next time?**

---

## 4. Reflection

**What is the most important thing I learned this week?**
The most important thing I learned this week is how to connect a Python program to an LLM through an API. Before this hackathon, I had only interacted with AI through tools such as ChatGPT. I now understand that Python can send text or images to an AI model through an API and use the response inside a program. I also learned how important it is to handle errors and unclear input instead of assuming that an AI answer is always correct.
**Where does this connect to "AI for Good"?**
MoneyTranslate shows how AI can be used to reduce an information barrier. Complex financial language can disadvantage people who have difficulty understanding it. AI can make this information more accessible, but using AI for good also means considering the people who could be harmed when the AI makes a mistake. Therefore, accessibility and reliability both need to be considered when designing the tool.
