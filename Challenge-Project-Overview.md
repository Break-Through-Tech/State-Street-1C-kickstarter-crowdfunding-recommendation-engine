# Kickstarter Crowdfunding Recommendation Engine

**Company / Org:** State Street  
**Challenge Advisor:** Parth Rana, parthrana34@gmail.com  
**AI Studio Coach:** Darshan Ugale, darshan.ugale@breakthroughtech.org  
**Program:** Break Through Tech AI Studio - Fall 2026

---

## 🏢 About State Street

State Street is a financial services and banking holding company specializing in investment management and servicing. The company operates at the intersection of financial services, data, technology, and analytics, providing an appropriate context for exploring how machine learning can support data-driven decision-making.

Note: This challenge does not contain any data from State Street.

---

## 🎯 The Challenge

### Project Summary

The goal of this project is to develop a **Kickstarter Crowdfunding Recommendation Engine** that predicts whether a crowdfunding campaign is likely to be successful or fail using information available around campaign launch. The project should go beyond prediction by identifying important factors associated with campaign outcomes and exploring how those insights could support actionable recommendations for campaign creators.

### Success Criteria

Success should be evaluated using multiple classification metrics rather than accuracy alone. The target is to achieve approximately **80% or better accuracy**, while also demonstrating strong **Precision, Recall, F1 Score, and ROC-AUC** performance and providing meaningful, interpretable insights into the factors driving predictions.

### Project Milestones

Use these milestones to guide your work. Your team will create a **GitHub Projects board** to track tasks within each milestone.

- **Milestone 1 — Data Preparation:** Clean and preprocess the Kickstarter dataset, filter the relevant campaign outcomes, prepare U.S.-based records, handle missing values, and encode categorical variables.
- **Milestone 2 — Exploratory Data Analysis:** Investigate relationships between campaign success and factors such as goal, duration, updates, location, category, subcategory, and reward levels. Identify patterns that can inform model development.
- **Milestone 3 — Machine Learning:** Establish baseline and advanced classification models, perform feature selection/engineering, compare model performance, and analyze model interpretability.
- **Milestone 4 — Recommendation Prototype:** Explore how predictions and insights from successful campaigns could be translated into actionable recommendations for campaigns predicted to be at risk.

> **Note for the team:** Please create a GitHub Projects board in this repository to break these milestones into weekly tasks. Go to the **Projects** tab → **New project** → Choose **Board** → Add columns for each month.

---

## 📊 Dataset

**Name and Source:** Kickstarter Projects dataset, publicly available through Kaggle  
**Format:** Structured tabular dataset (CSV)  
**Original Size:** Approximately 45,957 observations and 17 columns  
**Source:** [Kickstarter dataset on Kaggle](https://www.kaggle.com/parienza/kickstarter)

### Key Details

- The dataset contains Kickstarter project information including **Project ID, Project Name, URL, Category, Location, Status, Goal, Pledge, Funded Percentage, Backers, Funded Date, Levels, Reward Levels, Updates, and Comments**.
- The original data contains multiple campaign statuses. For the project's binary classification objective, the source project filtered the data to **successful and failed** campaigns and removed live, suspended, and canceled campaigns.
- The project further focused on campaigns in the **United States**, splitting location information into City and State, and removed records with missing values. The resulting dataset used in the original project contained approximately **38,491 records and 18 columns**.
- Students should independently review the raw dataset, validate the preprocessing assumptions, and document each transformation so that the final modeling dataset is reproducible.
- Potential data-quality considerations include missing values, categorical variables, inconsistent category labels, and the need to ensure that features used for prediction are appropriate for the intended prediction point.
- The original project used campaign attributes including **goal, duration, updates, levels, city, state, category, and subcategory** as important predictive variables.

---

## 🛠️ Suggested Approach

**ML Problem Type:** Supervised learning — binary classification.

### Recommended Models and Libraries

- **pandas / NumPy:** Data loading, cleaning, transformation, and numerical analysis.
- **scikit-learn:** Preprocessing, train/test splitting, Logistic Regression, Random Forest, K-Nearest Neighbors, feature selection, and model evaluation.
- **XGBoost or LightGBM:** Optional advanced tree-based models for comparison with the baseline models.
- **matplotlib / seaborn / Plotly:** Exploratory analysis and visualization.
- **SHAP:** Optional explainability tool for understanding model predictions and feature contributions.

### Suggested Modeling Strategy

Start with an interpretable baseline such as **Logistic Regression**, then compare it with **Random Forest** and one or more gradient-boosted tree models. K-Nearest Neighbors can also be included as a benchmark. Students should investigate whether feature engineering, feature selection, class balancing, and hyperparameter tuning materially improve results.

### Evaluation Metrics

Evaluate models using:

- **Accuracy**
- **Precision**
- **Recall / Sensitivity**
- **F1 Score**
- **ROC-AUC**
- **Confusion Matrix**

The original project found Random Forest to be the strongest of the three initial models, with approximately **80.2% accuracy** and an **F1 score of 0.834**. These results should be treated as a historical benchmark rather than a guaranteed target; students should reproduce and critically evaluate the results using a sound validation methodology.

---

## 📚 Resources to Get Started

The following resources will help your team understand the problem space and potential technical approaches for this project.

### Background Reading

- [Kickstarter](https://www.kickstarter.com/) — Background on the crowdfunding platform and campaign model.
- [Predicting the Success of Kickstarter Campaigns](https://towardsdatascience.com/predicting-the-success-of-kickstarter-campaigns-3f4a976419b9) — Background reading related to Kickstarter campaign prediction.

### Dataset and Documentation

- [Kickstarter dataset on Kaggle](https://www.kaggle.com/parienza/kickstarter) — Public dataset used in the original project.
- Review the dataset columns and metadata on Kaggle before beginning preprocessing.

### Technical Documentation

- [scikit-learn documentation](https://scikit-learn.org/stable/) — Classification, preprocessing, feature selection, and evaluation.
- [pandas documentation](https://pandas.pydata.org/docs/) — Data manipulation and analysis.
- [XGBoost documentation](https://xgboost.readthedocs.io/) — Optional gradient-boosting implementation.
- [SHAP documentation](https://shap.readthedocs.io/) — Optional model explainability.

### Code and Collaboration

- Use the repository's GitHub Issues and Projects features to document tasks, experiments, questions, and decisions.
- Keep preprocessing, modeling, evaluation, and visualization code reproducible and clearly documented.

*Feel free to explore beyond these resources and share anything interesting you find with the team.*

---

## 🤝 How We'll Work Together

**Official check-ins:** During the biweekly 45-minute AI Studio Lab Section meeting block (2nd and 4th week of every month).

**Other ways to reach out to me with questions:**

- **Email:** Parth Rana — parthrana34@gmail.com
- Please copy your teammates and AI Studio Coach on project-related questions.
- Additional team check-ins can be requested when needed and subject to availability.
- I will aim to respond within **48 hours**. Please reach out to your AI Studio Coach with urgent questions.

### Recommended Free Coding / Collaboration Tools

- **GitHub:** Use GitHub for source control, collaboration, documentation, issues, and project tracking. Each student should work on a separate branch and use pull requests to merge completed work into the main branch.
- **GitHub Projects:** Use a Kanban-style board to organize weekly tasks, assign ownership, and track progress across the three-month project.
- **VS Code / Jupyter:** Recommended environments for Python development and exploratory analysis.
- **Google Colab:** Optional free cloud-based environment for students who need additional compute resources.
- **Google Drive / Dropbox:** Optional for sharing supplementary documents or files that do not belong in the GitHub repository.

### Suggested Working Framework

Use lightweight **Agile/Kanban practices**: break milestones into small tasks, assign clear owners, maintain a visible backlog, review progress during check-ins, and document important modeling decisions. Regular commits and peer code reviews are encouraged.

---

## 🚀 Getting Started

1. **Review this overview document** and note any questions for our first meeting.
2. **Download and inspect the Kickstarter dataset** from Kaggle.
3. **Create or review the GitHub Projects board** and divide the milestones into weekly tasks.
4. Establish a reproducible data-preprocessing workflow and document the assumptions behind each transformation.
5. Begin with exploratory data analysis before selecting and tuning the final machine learning models.
6. Read the [GitHub Projects documentation](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects).

I’m excited to work with you!

---

## ❓ Questions?

Please bring any questions to our first meeting during the week of **August 24th** (Break Through Tech’s Bridge to Studio — Session C).
