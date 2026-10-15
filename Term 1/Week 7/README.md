# Term 1 - Week 7: Computer Vision

---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?**

**What did I hand in?**
_List the files, or link to them. Notebook exports, screenshots, scripts._

**What did I find difficult, and how did I solve it?**

### Checklist
- [ ] My workshop / homework files are in `homework/`
- [ ] Everything runs without errors, or I explained what does not and why

---


## 2. Hackathon prototype -> [`hackathon/`](hackathon/)

> Your tool and your SDG for this hackathon are announced at the **start of Friday's class**.
> Write them down here once you know them.

**Project title:**
SolarMood – Solar Energy News Sentiment Dashboard
**My pair partner:**
Meggie Raaphorst
**Tool we had to use:**
A pre-trained sentiment model from Hugging Face (https://huggingface.co/models), run with the transformers library, as in this week's lecture. AI coding assistants (Cursor, Claude Code, Antigravity) may help you build the product around it.
**SDG we had to address:**
9 — Industry, Innovation and Infrastructure
**What problem does it solve, and for whom?**
The solar energy industry is growing rapidly, making it increasingly important for companies to monitor technological developments, government policies, investments and market changes. According to IRENA (2025), global solar energy capacity grew by 32.2% in 2024, adding approximately 452 GW. Furthermore, the International Energy Agency (2026) reported that solar PV accounted for more than 75% of global renewable capacity additions in 2025.

Our specific target user is a market intelligence analyst working at a solar panel manufacturing company. This professional needs to monitor industry news to identify emerging technologies, policy changes, investment developments and potential market risks.

The problem is that relevant information is spread across many news sources, making it time-consuming to monitor developments and identify changes in news sentiment. Manually reading hundreds of headlines is inefficient and makes it harder to notice patterns over time.

SolarMood addresses this problem by automatically collecting solar energy news every 30 minutes and analysing headlines with a pretrained Hugging Face sentiment model. The results are displayed in an interactive Streamlit dashboard, allowing the analyst to monitor sentiment trends, filter articles and investigate unusual changes.

Our prototype has already collected more than 773 news articles, demonstrating the amount of information that can be gathered and organised automatically.

SolarMood supports SDG 9 by applying AI-driven innovation to information monitoring within the renewable energy industry. However, it measures the tone of news headlines rather than the actual economic or environmental impact of developments.

Sources:

IRENA (2025). Renewables in 2024: 5 Key Facts Behind a Record-Breaking Year. https://www.irena.org/News/articles/2025/Apr/Renewables-in-2024-5-Key-Facts-Behind-a-Record-Breaking-Year

IEA (2026). Global Energy Review 2026 – Solar PV and Wind. https://www.iea.org/reports/global-energy-review-2026/technology-solar-pv-and-wind

**What did you build?**
We built SolarMood, an AI-powered news monitoring application.

The system automatically retrieves solar energy news from Google News RSS feeds and uses a pretrained Hugging Face RoBERTa model to classify each new headline as positive, neutral or negative.

The results are stored in a CSV dataset and displayed through an interactive Streamlit dashboard. Users can view sentiment distributions, monitor sentiment over time and filter articles.

The automatic news collection process runs every 30 minutes when the scheduled collector is active.

**Link to the live thing (if any):**
https://solarmood-milou-jkelt2tjctww4cb8fjsbri.streamlit.app/
https://github.com/milouvanleuven-code/SolarMood-Milou

**How do I run it?**
The deployed dashboard can be opened directly through the link above.

To run SolarMood locally:

Download or clone the latest SolarMood repository from GitHub.
Install Python and open a terminal in the project folder.
Create a virtual environment using python -m venv .venv.
Activate the environment, or use its Python executable directly.
Install the dependencies using python -m pip install -r requirements.txt.
Start the dashboard using python -m streamlit run dashboard.py.
Open the local URL shown in the terminal.
Run python collector.py to perform a new collection and sentiment analysis.

The first run of the collector may download the pretrained Hugging Face model, so an internet connection and additional loading time are required.
For Windows users who cannot activate PowerShell scripts, the Python executable inside .venv\Scripts\ can be used directly.

Reproducibility note: The exact automatic scheduling procedure should be added from the final collector implementation. The final requirements.txt must also contain all libraries needed by the submitted code.

We evaluated our sentiment analysis using 50 manually labelled solar energy news headlines.

Our goal was to investigate whether the pretrained AI predictions agreed with human interpretations and whether a second method would perform differently.

We used two approaches:

RoBERTa: a pretrained Hugging Face model for text sentiment classification.
VADER: a lexicon-based sentiment analysis method.
We created Python scripts to compare both methods against the same human-labelled dataset.
Evaluation metric
RoBERTa
VADER
Headlines evaluated
50
50
Matching human labels
21
19
Agreement
42%
38%

RoBERTa achieved four percentage points higher agreement with the human labels than VADER. However, the sample is small, so we cannot conclude that RoBERTa is generally more accurate for all solar energy news.

What did the confusion matrices show?
RoBERTa frequently predicted neutral sentiment, including for headlines that humans labelled as positive.
VADER produced more positive classifications, including some headlines that humans considered neutral or negative.
This suggests that the models interpret the same headlines differently.

Three examples of classification disagreements

Example 1: Solar farming and disaster resilience
Headline: Hawai‘i energy forum launches online series on solar farming, disaster resilience and LNG – Maui Now
Human label: Positive
RoBERTa prediction: Neutral

The human evaluation may have interpreted the discussion of solar farming and resilience as a beneficial development. RoBERTa classified the wording as neutral because it describes an event without clearly positive emotional language.

Example 2: Community solar policy
Headline: Governor's energy plan promotes community solar – WVTF
Human label: Positive
RoBERTa prediction: Neutral

The headline describes a policy that may benefit community solar development. However, the wording is largely factual. The model does not necessarily recognise the positive sector-specific implications.

Example 3: Large-scale solar project
Headline: China connects 1-GW project combining solar PV, solar thermal – Renewables Now
Human label: Negative
RoBERTa prediction: Neutral

This example highlights the difficulty of manual labelling. Based on the headline alone, the negative human label is not immediately obvious. The model's neutral prediction may be reasonable because the headline is written factually.

This disagreement shows why human labels also need clear evaluation guidelines.
Most important finding
During our evaluation, we discovered that the human labels partly considered whether a news development was beneficial or harmful to the solar energy sector and sustainability.

However, the pretrained sentiment models primarily analyse the language used in the headline.
These are different tasks.
For example, a neutral headline about a new solar power plant could describe a positive development for the industry without containing explicitly positive wording.
Therefore, our percentages represent agreement with human sector-oriented judgements, rather than an objective measurement of model accuracy.
To improve future evaluations, we would separate two questions:
Is the wording of the headline positive, neutral or negative?
Is the development potentially beneficial, neutral or harmful to the solar energy sector?
We would also create written labelling guidelines and ask a second human evaluator to review ambiguous examples.

**Who did what?**
My partner focused mainly on implementing the automatic news collection system, collecting and classifying the larger dataset
, improving the Streamlit dashboard and updating the shared GitHub project.
The automated collector successfully gathered more than 773 articles and was configured to run every 30 minutes.

My contribution:

I focused mainly on evaluating the reliability of the sentiment predictions and testing the technical setup.
I developed evaluate.py, which reads the human-labelled evaluation data, compares it with RoBERTa predictions and calculates the agreement and confusion matrix.
I also developed compare_models.py, which applies VADER to the same 50 headlines and compares its results with RoBERTa.
These scripts produced sentiment_evaluation_results.csv and model_comparison_results.csv.
In addition, I configured the Python environment, installed the required libraries, ran the Streamlit dashboard locally, tested the Google News collector and created an alternative automatic collection script.

This experience showed me the importance of coordinating tasks and synchronising our work through GitHub.

**Ethical reflection - what are the risks of your tool? Who could it harm?**
Although SolarMood provides a useful overview of solar energy news, it has several important limitations.

Risk 1 – Incorrect classifications
Our evaluation showed that RoBERTa agreed with the human labels in only 42% of the evaluated headlines.
This does not necessarily mean the model is incorrect in all other cases, because the human labels partly measured sector impact rather than linguistic sentiment.
However, it shows that the results need careful interpretation.
Who could be harmed? Market analysts and companies could make poor decisions if they mistake automated sentiment classifications for reliable assessments of industry developments.
Mitigation: We should clearly explain what the model measures, provide access to the underlying headlines and encourage human review before important decisions are made.

Risk 2 – Data and geographical bias
Our Google News searches use English-language settings and may overrepresent certain countries, publishers and topics.
As a result, the collected news may not represent the global solar energy industry equally.
Who could be harmed? Companies operating in underrepresented regions could receive an incomplete picture of developments relevant to their markets.
Mitigation: We should disclose the data source and language settings, allow users to inspect the articles and consider adding regional or multilingual sources in future versions.

Risk 3 – Model-domain mismatch

The RoBERTa model was trained on Twitter data rather than specifically on solar energy industry news.
Technical announcements, investments and policy changes may therefore be classified differently from how an industry specialist would interpret them.
Who could be harmed? Analysts could overlook relevant developments because neutral wording hides important sector implications.
Mitigation: We should evaluate the model on a larger solar-specific dataset and develop separate labels for linguistic sentiment and sector impact.

Risk 4 – Overconfidence and misleading visualisations
Charts can make AI predictions appear more objective than they actually are.
A sudden increase in negative classifications does not necessarily mean that the solar energy industry is performing worse.
Who could be harmed? Users who rely on the dashboard without checking the underlying news may draw misleading conclusions.
Mitigation: The dashboard should include a clear disclaimer that it measures news-headline sentiment, not public opinion, environmental impact or financial performance. The results should be used to identify articles for further investigation rather than to make automatic decisions.

Overall, SolarMood should be considered a decision-support tool, not a replacement for professional judgement.

### Checklist
- [x ] Prototype code (or export / workflow file) is in `hackathon/`
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
The most important thing I learned was that developing a working AI application is not the same as developing a reliable AI application.
At the beginning of the project, I mainly focused on getting Python, the Hugging Face model and the Streamlit dashboard to work. I learned how to install the required libraries, run scripts locally and understand how data moves through an AI pipeline.
However, the most interesting part was evaluating the model.
By comparing 50 human-labelled headlines with RoBERTa and VADER, I discovered that the two methods produced different results and that neither showed strong agreement with our human evaluations.
I also learned how to calculate agreement, interpret a confusion matrix and investigate individual classification disagreements.
The biggest insight was that our human labels and the AI models did not necessarily measure the same concept. We partly judged the impact of news on the solar industry, while the AI models mainly evaluated the wording of the headlines.
This taught me that before evaluating an AI model, it is essential to define exactly what the model is supposed to predict.
I also gained experience collaborating on a software project. My partner and I worked on different parts of SolarMood, but we initially developed some code separately. This caused duplicated work on the automatic news collection.

Next time, I would divide tasks more clearly at the beginning, agree on a shared GitHub workflow and regularly synchronise our changes.
**Where does this connect to "AI for Good"?**
SolarMood connects to SDG 9 – Industry, Innovation and Infrastructure – by demonstrating how AI can help professionals monitor technological and industrial developments.
The rapid growth of solar energy makes it valuable to organise information about new technologies, policies and infrastructure projects.
SolarMood uses AI to make this information easier to explore, potentially helping analysts identify developments that deserve further investigation.
However, this project also showed me that AI for Good requires more than a useful technical solution.
AI can introduce bias, produce misleading predictions and create false confidence if its limitations are not communicated clearly.
Our model evaluation showed why transparency, human oversight and careful interpretation are important.
My main takeaway is that responsible innovation means understanding both what AI can do and what it cannot reliably tell us.

Sources

International Renewable Energy Agency (IRENA). (2025). Renewables in 2024: 5 Key Facts Behind a Record-Breaking Year. https://www.irena.org/News/articles/2025/Apr/Renewables-in-2024-5-Key-Facts-Behind-a-Record-Breaking-Year
International Energy Agency (IEA). (2026). Global Energy Review 2026: Technology – Solar PV and Wind. https://www.iea.org/reports/global-energy-review-2026/technology-solar-pv-and-wind
Cardiff NLP. Twitter RoBERTa Base Sentiment Latest. https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest
Hutto, C. J., & Gilbert, E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Proceedings of the International AAAI Conference on Web and Social Media.
