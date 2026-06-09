# DDI-Midterm-Project
This repository contains my Supra Coders DDI Midterm Project. In it, I regress factors such as years of experience, field of work, and skills against annual salary.

## Research Question
The question that I aimed to answer in this project was, "Which skills are correlated with the highest increases in salary in the civilian sector?" The answer that I found gives insights into what skills employers find important, and the same goes for the military. I faced this project taking a two-pronged approach for military members- how to best improve skills that the military needs, and what to start thinking about to be marketable if a member is transitioning out of the military. As the country faces  pacing threats and new conflict, there is no better time for military members to be at their best. This goes for anyone, including those who work in tech fields. Thus, my goal was to provide information about how military members can start to improve their skills in order to find the most benefit for their units and themselves. My findings show a framework for how military members should start thinking about their careers, but should absolutely not be taken as sound career advice or recommendation.

## Data
The original DataFrame, or df, was sourced from kaggle, and had 10,000 rows and 50 columns. Each row represents one person and their corresponding values for each column. This was too much data for my project, and some of the columns were correlated with each other. You can see the first 10 rows of my data below.

![First 10 lines of my original df](pictures/original_df.png)

The first thing I did was filter out jobs that did not pay in US Dollars. I did this using `df = df[df['currency']=='USD']`. I then addressed the number of columns in the df. The original was too large to display in jupyter notebook, so I used `df.columns` to see all the column names. After seeing all of them, I only kept 'skills', 'annual_net_salary_usd', 'experience_years_total', 'location', 'education_level', 'primary_tech_field', and 'company_size'. Going through each of the columns I kept, experience_years_total is the years of experience each person has, and it is a continuous numerical variable. The location column is the location of each person's work, and is a nominal categorical variable. The column education_level is an ordinal categorical variable that describes the highest level of education a person achieved. The primary_tech_field column is a nominal categorical variable that is the tech field that each person works in. The company_size variable describes the size of each person's company that they work for and is an ordinal categorical variable. Skills is a list of each skills each person has and is a nominal categorical value which I converted into a binary dummy variable in later steps. Lastly, the annual_net_salary_usd column is a continuous numerical variable that describes each person's monetary, net salary that they are given as compensation After filtering, I was left with my new `important_columns` df which looked like this.

![First 10 lines of filtered df](pictures/filtered_df.png)

After filtering all my data, I wanted to address the skills column. It was one long string with each skill a person had separated by a `;` and a space. In order for me to be able to run a regression on this column, I needed to create dummy variables, so I used `skills = important_columns['skills'].str.get_dummies(';')` to create new columns with each of the skill names. I found that there was an exact copy of column names because I forgot to filter the space after each semicolon, so I used `skills.columns = skills.columns.str.strip()` and `skills = skills.groupby(skills.columns, axis=1).max()` to take out the space and group the column names together. Now I had a skills dataframe that looked like this.

![First 10 lines of skills df](pictures/skills_df.png)

This looks scary, but the number of rows matches the number of rows in my filtered df, so if I have to concatenate them, they share an axis with the same size so everything will work out fine. 

Lastly, I had to create dummy variables for each of the columns that had categorical data. I know that the `get_dummies` command is smart and will not convert continuous variables into dummy variables, so I ran `dummy = pd.get_dummies(df_clean[['experience_years_total', 'location', 'education_level', 'primary_tech_field', 'company_size']], drop_first=True, dtype=int)` keeping the years of experience in the new dummy df so that I had all variables that I needed. I then reset both dummy and skills' indices and concatenated them. This was the last step in my data cleaning.

## Visualizations

In order to see how each variable affects the annual salary of each person, I ran a linear regression on all the columns against the annual salary. A linear regression is a simple regression model that predicts the dependent variable based on one or more dependent variables. The reason it is called a linear regression is that the resulting line of best fit is a first order equation. I ran my model with the columns that I kept from the last step, and the output can be seen below.

![Factor coefficients](pictures/controlled)
