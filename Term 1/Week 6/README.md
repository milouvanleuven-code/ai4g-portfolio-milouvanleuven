# Term 1 - Week 6: Language Models
scikit-learn — the Python machine-learning
---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?**
Pick one concrete prediction problem about work, income or economic security, find a real dataset for it yourself, and train three classifiers on it: a k-nearest-neighbours model, a logistic regression, and one model of your own choice (a decision tree, a random forest, gradient boosting, an SVM, naive Bayes, anything scikit-learn offers that you can explain). Tune all three, compare them fairly, and tell a named user which one they should use, or why none of them is good enough.

This hackathon is not about the model. Fitting a model is one line of code. It is about everything around that line: understanding and cleaning the data, choosing the right train and testsets, tuning, and choosing a metric that matches what a wrong prediction costs a real person — someone who does not get the loan, the job interview or the support. A model that scores 0.99 on a leaky split fails this hackathon; a robust model that scores 0.72 honestly, and knows why, passes it.
**What did I hand in?**
_List the files, or link to them. Notebook exports, screenshots, scripts._

**What did I find difficult, and how did I solve it?**
The hardest part was finding a reliable, well-documented dataset that fit our topic and could actually answer our question. Many promising ideas fell apart: some datasets turned out to be synthetic, some were only available as group totals, and some were locked behind access restrictions. We solved this by brainstorming several ideas, including the gender pay gap, unemployment, working poverty and debt problems. For each one we checked how much trustworthy, public data was available. In the end we chose the topic with the richest data behind it, so the topic followed the evidence and not the other way around.
### Checklist
- [x ] My workshop / homework files are in `homework/`
- [ x] Everything runs without errors, or I explained what does not and why

---


## 2. Hackathon prototype -> [`hackathon/`](hackathon/)

> Your tool and your SDG for this hackathon are announced at the **start of Friday's class**.
> Write them down here once you know them.

**Project title:**
Underpaid and Overworked: predicting wage exploitation of migrant victims of forced labour

**My pair partner:**
Allan Hassan
**Tool we had to use:**
scikit-learn KNN, Logistic Regression and a model of our own choice: Random Forest
**SDG we had to address:**
8 — Decent Work and Economic Growth

**What problem does it solve, and for whom?**
Labour migrants often work longer hours and earn less than local workers. Worldwide, migrant workers are about three times as likely to end up in forced labour as other workers (ILO, Walk Free & IOM, 2022). In high-income countries migrants earn almost 13% less than nationals, and migrant women about 21% less than male nationals (ILO, 2020). In the Netherlands there are around 700,000 labour migrants (2022, an underestimate). 77.5% of EU labour migrants work full-time, compared with 52.3% of all workers. 48% of EU labour migrants still earn under 130% of the minimum wage after ten years (IBO Arbeidsmigratie, 2025). Only about 230 suspected victims of labour exploitation are registered per year (Nationaal Rapporteur Mensenhandel, 2021), so most cases stay hidden.

Our user is an intake caseworker at a victim-support organisation, such as CoMensha (the Dutch coordination centre against human trafficking) or FairWork. This person meets a newly identified victim of forced labour and has to decide, with limited time and few legal and financial specialists, who gets priority for a wage-recovery claim and debt counselling. The people affected are migrant victims of forced labour.

The model is not intended for:

employers or agencies screening workers
immigration enforcement
judging migrants in general

**What did you build?**
A Jupyter notebook that takes the raw CTDC dataset and predicts whether a migrant victim of forced labour had their wages withheld or was in debt bondage (target column meansDebtBondageEarnings). We train, tune and fairly compare a DummyClassifier baseline, KNN, Logistic Regression and Random Forest. The main metric is recall. At the end, a caseworker can enter a new case (gender, age band, citizenship, country of exploitation, sector, recruiter, year) and gets a prediction plus a probability.

**Link to the live thing (if any):**
_Deployed URL, workflow export, video demo - whatever proves it works._

**How do I run it?**
_Short instructions so someone else can start it._

**Who did what?**
Milou: problem research and sources, user group, SDG analysis, slides, ethical reflection
Allan: data cleaning code, pipeline and tuning
Together: choosing the target and metric, error analysis, recommendation

**Ethical reflection - what are the risks of your tool? Who could it harm?**
Our model makes predictions about people who have already been exploited, so its mistakes land on very vulnerable people. A false negative means a victim who lost wages is not prioritised for a wage claim or debt help and stays trapped in debt. That is why we chose recall as our main metric.

The data has four specific risks:

The rows are synthetic. The victims were never asked, and patterns learned from synthetic rows may not hold for real people. The model is therefore a prototype, not a tool for real cases.
Citizenship is a feature, which can turn into profiling. Migrants could be flagged or overlooked because of their passport, and the tool could be misused by employers or immigration enforcement. We therefore state explicitly who must not use it.
A blank field means "not recorded", and we treat it as "no". Poorly documented cases therefore look "safe". Wage loss is recorded for 50% of men but only 26% when gender is unknown, which leads to more false negatives for exactly the people we know least about. We check recall per gender group, and the decision threshold can be lowered to catch more cases.
The data hardly contains the Netherlands. It is mostly cases from the USA and Russia, with fewer than 20 Dutch forced-labour cases. The results may not hold for Polish or Romanian workers in Dutch agriculture.

Before any real use, the model must be retrained on real Dutch case data under a data-sharing agreement. A caseworker always makes the final decision.

### Checklist
- [x ] Prototype code (or export / workflow file) is in `hackathon/`
- [ x] This week's slides are in `hackathon/`
- [x ] The prototype actually runs, and I wrote down how to run it
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
A high score means nothing if it is not honest. The model is one line of code; the real work is in the choices around it. Splitting before preprocessing, removing duplicate rows and leaving out columns that leak the answer all make the score lower, but more honest. And choosing a metric is an ethical decision: we chose recall because missing a victim who lost wages is worse than one extra check.
**Where does this connect to "AI for Good"?**
Our model predicts something about people who have already been exploited, so every mistake has a human cost. Accuracy alone would hide those mistakes. A subgroup check showed that poorly documented people, such as those whose gender is unknown, are more likely to be missed. Using AI for good here means choosing the metric that protects the most vulnerable people, and being clear about who must not use the tool.
