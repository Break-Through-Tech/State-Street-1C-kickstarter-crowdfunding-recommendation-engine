---

> ## Challenge Advisor: Update & Finalize Your Project Overview
>
> > 💡 **These grey text instructions are just for you, the team's Challenge Advisor; please delete them once you have completed the steps below.**
>
> We've pre-populated this Challenge Project Overview page — which is what will be shared with your Break Through Tech student team in August — using the details from your submission form. You should have received an email inviting you to join this repo as a Collaborator, enabling you to add files and make edits.
> 
> In order for your project to be finalized and assigned to a team, please:
> 1. **Review all sections below** and update or expand any content as needed, making sure to address the SME Feedback in the section immediately below. Look for square brackets to find the places below that require additional inputs from you (e.g., "About [Company / Org Name]").
> 2. **Add your dataset** to the [data folder](data) in this repo.
> 3. **Close the Issue assigned to you in this repo** to let us know that you have made your edits and the overview page is ready for final review. You can do this by going to the _Issues_ tab in the top left section of the menu above, add a comment that says "CA review complete", and click the button to Close the Issue. 
>
> If you're unfamiliar with how to edit a page like this in GitHub, check out [this tutorial](https://ubc-lib-geo.github.io/gis-workshop-waml-template/content/handson/edit-readme.html) for a quick overview (start with step 2 and only edit this page), and [this guide](https://ubc-lib-geo.github.io/gis-workshop-waml-template/content/markdown.html) on how to use Markdown to compose text.
>
>
> ❌ Remember that this is a public repo. Do NOT include: Proprietary data, PII, API keys, credentials, or anything confidential.

---

## 📋 BTT Internal Evaluation Notes
*(This section is for BTT staff only — remove before sharing with students)*

| Check | Status | Notes |
|-------|--------|-------|
| Python Compatibility | 🟢 | The tech stack primarily uses Python, which aligns well with student skills. |
| Data Readiness | 🟢 | The dataset is publicly available, under 1GB, and formatted for easy use (CSV/TSV), minimizing preparation time. |
| Resource Check | 🟢 | No specialized hardware or proprietary software is required; students can use Google Colab for free-tier access. |

**Student Fit Score:** 8/10  
**Technical Depth Score:** 7/10  
**Overall Recommendation:** APPROVE

**Advisor Feedback Draft:**
The project's focus on predicting Kickstarter success aligns with real-world applications and is a valuable learning experience. However, consider the following technical adjustments: 1) Include a more comprehensive exploratory analysis phase to derive insights from the data that may inform modeling choices better. 2) Ensure students engage with a variety of classification and regression models to understand the impact of different algorithms on outcomes. Moving forward, encourage the team to clarify how they will effectively integrate evaluation metrics into their modeling process.

---

# Kickstarter-Crowdfunding-Recommendation-Engine

**Company / Org:** State Street  
**Challenge Advisor:** Parth Rana, parthrana34@gmail.com  
**AI Studio Coach:** Darshan Ugale, darshan.ugale@breakthroughtech.org    
**Program:** Break Through Tech AI Studio - Fall 2026

---

## 🏢 About State Street

State Street is a financial services and banking holding company specializing in investment management and servicing. We operate at the crossroads of the finance industry, offering innovative solutions and insights.

---

## 🎯 The Challenge

### Project Summary
The aim of this project is to predict the success or failure of a Kickstarter campaign at launch time.

### Success Criteria
Accuracy and Precision

### Project Milestones

Use these milestones to guide your work. Your team will create a **GitHub Projects board** to track tasks within each milestone.

| Month | Milestone | Key Activities |
| :--- | :--- | :--- |
| September | Data Processing, Preprocessing & Baseline Modeling | • Ingest and clean the Kickstarter projects dataset (handling missing values, datetime parsing, and goal/currency standardizations).<br>• Perform Exploratory Data Analysis (EDA) on success rates, goal distributions, and category-level trends.<br>• Engineer baseline features (campaign duration, goal amount in USD, launch month/day, primary category).<br>• Train baseline classifiers (Logistic Regression / Decision Trees) to predict campaign success or failure. |
| October | Feature Engineering, Advanced ML & Recommendation Engine | • Extract textual features from campaign titles and blurbs using TF-IDF or text embeddings.<br>• Train advanced models (XGBoost, Random Forest, LightGBM) to forecast campaign funding success.<br>• Perform hyperparameter tuning and cross-validation, evaluating via Precision, Recall, F1-Score, and ROC-AUC.<br>• Build recommendation logic to suggest optimal campaign settings (ideal goal amount, launch timing, duration). |
| November / December | Model Explainability, Interactive UI & Deliverables | • Apply SHAP value interpretability to isolate top features driving project funding success.<br>• Build an interactive Streamlit web application for creators to input project parameters and receive recommendations.<br>• Finalize clean, reproducible GitHub repository, documentation, and final presentation deck. |

### Stretch Goals
* **Interactive Campaign "What-If" Simulator:** Build a scenario-testing tool within the Streamlit UI enabling creators to tweak goals, launch timing, and duration to see real-time success probability updates.
* **NLP Blurb & Description Analysis:** Incorporate fine-tuned transformer embeddings (e.g., Sentence-Transformers) to analyze campaign blurb sentiment and readability scores as predictive signals.
* **Unsupervised Campaign Clustering:** Apply clustering techniques (K-Means or DBSCAN) to discover natural groupings of campaigns based on funding profiles and risk metrics.

> **Note for the team:** Please create a GitHub Projects board in this repository to break these milestones into weekly tasks. Go to the **Projects** tab → **New project** → Choose **Board** → Add columns for each month.

---

## 📊 Dataset

**Name and Source:** Publicly available Kickstarter dataset from Kaggle  
**Format:** CSV, TSV, Excel  
**Size:** under 1gb  
**Location:** [Kickstarter Projects Dataset](https://www.kaggle.com/datasets/kemical/kickstarter-projects)

### Key Details
- Publicly available Kickstarter dataset (Numerical / Quantitative, Text) in CSV/TSV and Excel formats. 
- Limited number of missing entries; explore EDA for better understanding.
- [Link to data dictionary or documentation, if available]

---

## 🛠️ Suggested Approach

**ML Problem Type:** Classification, Regression

**Recommended Libraries:**
- Machine Learning Algorithms
- Classification
- Regression
- Google Colab

**Evaluation Metrics:**
- Accuracy
- Precision/Recall

---

## 📚 Resources to Get Started

The following resources will help your team understand the problem space and potential technical approaches for this project:

**Background Reading:**
- [Understanding Kickstarter and Its Campaigns](https://www.kickstarter.com/help/handbook)
- [An Analysis of Kickstarter Campaigns](https://towardsdatascience.com/an-analysis-of-kickstarter-campaigns-e1e4c5c20502)

**Technical Tutorials:**
- [Machine Learning Classification Techniques](https://www.coursera.org/learn/classification)
- [Google Colab for Machine Learning](https://colab.research.google.com/notebooks/welcome.ipynb)

**Code Examples:**
- [Kickstarter Success Prediction Github Repository](https://github.com/example/kickstarter-success-prediction)
- [Sample Implementation for Classification](https://github.com/example/classification-example)

**Other:**
- [Video: How to Launch a Successful Kickstarter Campaign](https://www.youtube.com/watch?v=example)
- [Podcast on Crowdfunding Strategies](https://www.examplepodcast.com)

*Feel free to explore beyond these, and share anything interesting you find with me!*

---

## 🤝 How We'll Work Together

**Check-ins:** During our biweekly 60-min AI Studio Lab Section meeting block (2nd and 4th week of every month)  
**Communication:** Slack (Break Through Tech workspace)  
**Response time:** Within 48 hours on weekdays  

**Recommended Tools:**
- **Coding:** Google Colab
- **Collaboration:** GitHub, Notion
- **Virtual Meetings:** Zoom, Google Meet

---

## 🚀 Getting Started

1. **Review this overview document** and note any questions for our first meeting
2. **Begin reviewing the dataset** using the link above
3. **Read the GitHub Projects documentation** [here](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)

I'm excited to work with you!

---

## ❓ Questions?

Please bring any questions to our first meeting during the week of August 24th (Break Through Tech's Bridge to Studio - Session B).

---
