# Credit Card Default
This project, "Credit Card Default Classification," is part of my Hacktiv8 coursework on classification. It serves as both a requirement for my Hacktiv8 studies and a component of my personal portfolio in Data Science. I created this project with a fictional background, made solely for the purpose of the project. You can find my other personal projects on [Richard Edgina Virgo](https://github.com/REV04).

#### -- Project Status: Finished

## Project Intro/Objective

The purpose of this project is to classify whether bank credit card customers are likely to default. I built a model to identify which credit card customers are likely to default. I will conduct Exploratory Data Analysis (EDA) to explore the credit card customer data. I created a pipeline to perform feature scaling and encoding. I used cross-validation to determine the best model, and found that the best model is Support Vector Classification (SVC). The model was then evaluated and improved with hyperparameter tuning using random search. After that i built deployment in hugging face

### Methods Used
- Logistic Regression
- Pipeline
- Data Visualization
- Data Analysis
### Technologies

- Python

## Project Description

The dataset used for creating this model is sourced from BigQuery. It contains information about credit card customers. I performed Exploratory Data Analysis (EDA) to understand the data. After EDA, I applied feature engineering to enhance the model's performance. I used a pipeline to customize preprocessing steps and employed cross-validation to identify the best model. After determining that the best model is Support Vector Classification (SVC), I proceeded with model training and evaluation using the F1 score. I then applied hyperparameter tuning using random search to further improve the model and evaluated it again after tuning. Finally, I analyzed the data to identify correct and incorrect predictions.

The result from the model is:
- F1 score model before hyperparameter tuning for train is 0.572 and test 0.4816. 
- F1 score model after hyperparameter tuning for train is 0.528 and test 0.512

The SVC model was selected based on the best cross-validation score using the F1-score metric. Before hyperparameter tuning, there was a significant differences in F1 scores between training and testing data, indicating overfitting. After hyperparameter tuning, although there was a decrease in the F1 score on training data, the difference in F1 scores between the training and test set becomes minimal, indicating a good fit for the model. Analyzing actual data against predictions reveals that the model struggles to predict data where the data is have variety and  accurately but performs well with less variety data.

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Exploratory Data Analysis (EDA), Model Training, Model Evaluation, and summary are being kept in Python/Credit_Card_Default.ipynb
3. Model Inference is being kept in Python/Credit_Card_Default_Inference.ipynb
4. url link for hugging face is being kept in Python/url.txt
5. Credit Card Default data set is being kept in DataSet/Credit_Card_Default.csv
6. Hugging Face deployment is being kept in deployment folder

## Featured Notebooks/Analysis/Deliverables

- [Hugging Face for model usage demonstration](https://huggingface.co/spaces/REV04/Credit_Card_Default_Richard)

## Contact

- If you have any question or want to contribute with this project, feel free to ask me in [linkedln](https://www.linkedin.com/in/richard-edgina-virgo-a7435319b/).
