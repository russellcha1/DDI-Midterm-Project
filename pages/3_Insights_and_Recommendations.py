import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title='Insights, Recommendations, Future Research')
st.write('## Insights, Recommendations, and Future Research')
st.markdown('''
In this part of the presentation, I will go over the meaning behind what my
model yielded, as well as lessons that can be learned from my findings. I
will also go into what I might do going forward with this project, or what I
would have done with more time.
            
I would also like to preface this page by saying that no information or insights
that were produced should be taken as sound career advice or recommendations. These
insights are only to be used as deductions based on the data that I processed.
''')
st.write('## Insights and Recommendations')
st.markdown(
'''
In terms of skills, the obvious choice of skills
one might learn according to my findings would be highly specialized tools, or
blockchain/web3 development. However, as far as I know, these jobs are assigned 
sparingly or are contracted out, as blockchain is not used very heavily in our sector.
On the other hand, C and MATLAB, which are used for technical computing, are skills 
that are widely taught and have free documentation and lessons online. Furthermore,
even if these skills are not primarily used in one's role, they can be incorporated
as needed as **force multipliers**.

In the same vein, my common skills table that was shown in the last page shows that 
some helpful skills to learn can be categorized as application development, infrastructure and DevOps,
data analytics, and collaboration and process skills. In my data, these skills were either common,
yielded high pay, or both.
''')

st.write('## Future Research')
st.markdown(
'''
In the future, I would like to explore three avenues: incorporating all compensation, testing my 
model, and using a different model.

1. In the data I found, there were multiple columns relating to salary such as PTO and equity. Fully
incorporating all forms of compensation into my model using a "compensation score" may help with the model's
clarity and robustness.

2. A way to see how well my model can predict one's annual compensation would be to test my model. This
involves splitting the data I feed into the model into training and testing groups. The linear regression would
work just the same, using the training rows of data to make coefficients, and then would be tested
using the test data to see if the coefficients that were yielded from the training data can predict the
test data's annual compensation well.

3. Lastly, I would like to explore using different regression models for my data. Linear regression is a very
simple form of modeling data, and has limitations. Other models have different limitations, but also different
benefits. In the future, I would like to explore what these other models could tell me about the data and
may lead to better prediction.
''')