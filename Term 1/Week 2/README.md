# Term 1 - Week 2: Loops & Functions

---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?**
Build an automated workflow that improves someone's health or well-being. The automation must run on a real trigger (schedule, form submission, incoming message) and produce a meaningful output. Examples: a daily mental health check-in bot, a medication reminder system, an air quality alert, a pipeline that monitors health news and sends a personalised digest.

Rules of the game: you must use this week's tool (no substitutions), your project must address this week's SDG, and the result must be working and demonstrable — something a real user could actually use, not a mock-up. The problem you solve and how you solve it are entirely up to you.
**What did I hand in?**
https://milouvanleuven.app.n8n.cloud/form/2f281ad2-c8f0-47ac-81e9-d8ddcdccd912

<img width="1102" height="280" alt="image" src="https://github.com/user-attachments/assets/9c9ce083-d204-42bc-b35e-f0caf559b823" />

**What did I find difficult, and how did I solve it?**
I found it difficult to work with n8n because I had no previous experience with the program. I solved this by watching several tutorials and using AI to guide me through the different steps and help me understand how the workflow works.
### Checklist
- [x ] My workshop / homework files are in `homework/`
- [x ] Everything runs without errors, or I explained what does not and why

---


## 2. Hackathon prototype -> [`hackathon/`](hackathon/)

> Your tool and your SDG for this hackathon are announced at the **start of Friday's class**.
> Write them down here once you know them.

**Project title:**
Flow State 
**My pair partner:**
quinten van Ingen 
**Tool we had to use:**
n8n
**SDG we had to address:**
3 — Good Health & Well-being
**What problem does it solve, and for whom?**
Flow State is designed for students and other busy people who may struggle to notice how their mood, energy, sleep and mental load relate to their daily workload. It helps users reflect on their well-being and adjust their day before they become overwhelmed.


**What did you build?**
We built an automated daily well-being assistant in n8n. The user completes a short check-in about sleep, energy, mental load, mood and what is on their mind. The workflow checks the user's Google Calendar, looks at previous data stored in Google Sheets and uses AI to generate a personalised daily review with practical advice. A scheduled email also reminds the user to complete their daily check-in.


**Link to the live thing (if any):**
https://milouvanleuven.app.n8n.cloud/workflow/EY2pkUIRblr2rIyd

**How do I run it?**
Import the workflow JSON file into n8n and connect the required Google Calendar, Google Sheets, Gmail and OpenAI credentials. Publish the workflow and open the form URL. Submit the daily check-in form to start the main workflow. The separate Schedule Trigger automatically sends the daily reminder email.


**Who did what?**
We divided the work equally between us. We worked together on designing the workflow, setting up the different n8n nodes, testing the automation, and solving problems along the way. Both of us contributed equally to the final project.

**Ethical reflection - what are the risks of your tool? Who could it harm?**
Flow State uses sensitive information such as mood, sleep, mental load and calendar data, so privacy and responsible data handling are important. The AI can also misunderstand a user's situation and give advice that is inappropriate or inaccurate. If n8n, Gmail, Google Calendar or the AI service is unavailable, reminders or analyses may also be late or fail completely. For these reasons, Flow State should only be used as a self-reflection and planning assistant and should never diagnose mental-health conditions or replace professional help. Serious or persistent mental-health concerns should always be handled by a human professional.


### Checklist
- [x ] Prototype code (or export / workflow file) is in `hackathon/`
- [x ] This week's slides are in `hackathon/`
- [x ] The prototype actually runs, and I wrote down how to run it
- [x ] Ethical reflection written above

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
The most important thing I learned this week is how different tools and services can be connected in n8n to create a complete automated workflow. I learned how to use triggers, Google Calendar, Google Sheets, Gmail, JavaScript and AI together, and how data can be passed from one node to the next.

**Where does this connect to "AI for Good"?**
Flow State connects to AI for Good because AI is used to support mental well-being rather than just automate a task. It can help users become more aware of how their sleep, mood, energy and workload relate to each other. At the same time, this project showed me why AI in health-related applications needs clear ethical boundaries: AI can support reflection and planning, but it should not replace human judgement or professional healthcare.
