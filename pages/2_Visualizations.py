import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title='Data Visualization')
st.write('# Data Visualization')
st.markdown('In this part of my presentation, I will review the graphs of the data that was yielded from my linear regression model.')
st.markdown('## Linear regression with respect to my data')
st.markdown(
'''
In order to see how each variable affects the annual salary of each person, I ran a linear regression
on all the columns against the annual salary. A linear regression is a simple regression model that predicts
the dependent variable based on one or more dependent variables. The reason it is called a linear regression
is that the resulting line of best fit is a first order equation. I ran my model with the columns that I kept from
the last step, and the output can be seen below.         
''')

df = pd.read_csv('tech_salary_dataset.csv')
df = df[df['currency']=='USD']
important_columns = df[['skills', 'annual_net_salary_usd', 'experience_years_total', 'location', 'education_level', 'primary_tech_field', 'company_size']]
important_columns = important_columns.reset_index(drop=True)
skills = important_columns['skills'].str.get_dummies(';')
skills.columns = skills.columns.str.strip()
skills = skills.groupby(skills.columns, axis=1).max()
columns_to_check = ['experience_years_total', 'location', 'education_level', 'primary_tech_field', 'company_size', 'annual_net_salary_usd']
df_clean = df.dropna(subset=columns_to_check).copy()
df_clean = df_clean.reset_index(drop=True)
skills_clean = skills.loc[df_clean.index].reset_index(drop=True)
dummy = pd.get_dummies(df_clean[['experience_years_total', 'location', 'education_level', 'primary_tech_field', 'company_size']], drop_first=True, dtype=int)
dummy = dummy.reset_index(drop=True)
skills_clean = skills_clean.reset_index(drop=True)
x = pd.concat([dummy, skills_clean], axis=1)
y = df_clean['annual_net_salary_usd']
mod = LinearRegression()
mod.fit(x,y)
controlled = pd.Series(mod.coef_, x.columns).sort_values(ascending=False)
st.write(controlled)

st.markdown(
'''
This output is exactly what I wanted, so I split the skill factors and the non skill factors. I graphed the top and bottom 10 skill factors first which can be seen below.
''')

st.markdown('## Skill Data Visualization')

skill_bump = controlled.loc[skills_clean.columns]
skill_bump = skill_bump.sort_values(ascending=False)
fig, ax = plt.subplots()
skill_bump.head(10).plot(kind='barh', ax=ax, title='Top 10 Skills vs Correlated Increase in Salary')
ax.set_xlabel('USD')
ax.set_ylabel('Skill Name')
st.pyplot(fig)
fig, ax = plt.subplots()
skill_bump.tail(10).plot(kind='barh', ax=ax, title='Bottom 10 Skills vs Correlated Decrease in Salary')
ax.yaxis.tick_right()
ax.set_xlabel('USD')
ax.set_ylabel('Skill Name')
ax.yaxis.set_label_position('right')
st.pyplot(fig)

st.markdown(
'''
Here, we can see the top 10 skills that are correlated with the highest increases in pay within the df.
Smart Contracts, ethers.js, and Hardhat are associated with blockchain and web3 development. Blender and Shader Programming are associated with 3D graphics.
TestRail is for testing and quality assurance.
C and Matlab are used for technical computing to include analysis and simulations. And Airflow and Snowflake are used for data engineering and infrastructure.

As for the bottom 10, JavaScript, PostgreSQL, and Cypress are used for web and app development. CI/CD and GCP are used for DevOps and cloud infrastructure. OpenGL, Foundry, and dbt are used for graphics, visual computing
and data transformation and analytics. Network Security is used in cybersecurity. And Roadmapping is used in strategy and planning.

Seeing these graphs, it looks like the most in demand skills are very specialized, technical skills that not many people know, and the bottom 10 are a little more spread out.

It is important to note that these skills do not _cause_ higher or lower salaries, but are _associated_ with higher salaries in this specific model.
''')

st.markdown('## Other Factors')
st.markdown(
'''
After seeing the results of the skills, I wanted to see how other factors held up when seeing the correlated salary increases or decreases. So, I plotted the top and bottom 10 factors excluding skills
which can be seen below.
''')
controlled_factors = controlled.drop(skills.columns)
controlled_factors = controlled_factors.sort_values(ascending=False)
fig, ax = plt.subplots()
controlled_factors.head(10).plot(kind='barh', ax=ax, title='Top 10 Factors vs Correlated Increase in Salary')
ax.set_xlabel('USD')
ax.set_ylabel('Factor')
st.pyplot(fig)
fig, ax = plt.subplots()
controlled_factors.tail(10).plot(kind='barh', ax=ax, title='Bottom 10 Factors vs Correlated Increase in Salary')
ax.set_xlabel('USD')
ax.set_ylabel('Factor')

st.markdown('## Common Skills')
st.markdown('''
Knowing which skills and factors yield the highest correlated increases in salary are great. However, my graphs do not capture how common each skill is in the data. Highly specialized skills may
lead to much higher pay, as the information surrounding them is esoteric, making the skill not very accessible to most. Therefore, I went through my dataframe and created a metric: how much the skill increases the salary
multiplied by the number of times it shows up in the data. With this, I am able to figure out which skills are common and yield the highest correlated pay bumps. The output is shown below.
''')

skill_sum = skills_clean.sum()
common_skills = skill_sum[skill_sum > 0]
metrics = pd.DataFrame({'pay': skill_bump.loc[common_skills.index], 'count': skill_sum.loc[common_skills.index]})
metrics = metrics[metrics['pay'] > 0]
metrics['value_score'] = metrics['pay'] * metrics['count']
top_skills = metrics.sort_values(by='value_score', ascending=False)
st.write(top_skills.head(20))