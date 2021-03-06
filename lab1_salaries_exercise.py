# -*- coding: utf-8 -*-
"""Lab1_Salaries Exercise.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jQhC5bl0jIw-F7PY5Q6lvt0ALXKg95JO

#### Introduction to Machine Learning CS452 Ashesi University 

## Lab 1

Name:
"""

Percy Brown

"""Student Number:"""

40382022

"""# SF Salaries Exercise 

Welcome to a quick exercise for you to practice your pandas skills! We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

** Import pandas as pd.**
"""

import pandas as pd

"""** Read Salaries.csv as a dataframe called sal.**

To make it easier, Salaries.csv was uploaded to my github repository - **PersieB
/Machine-Learning-Lab-1** where I read the file from the url to the raw dataset on in github repository.
"""

mygithub = 'https://raw.githubusercontent.com/PersieB/Machine-Learning-Lab-1/master/Salaries.csv'
sal = pd.read_csv(mygithub)

sal.info()

"""** Check the head of the DataFrame. **"""

sal.head()

"""** Use the .info() method to find out how many entries there are.**"""

sal.info()

"""**What is the average BasePay ?**"""

sal['BasePay'].mean()

"""** What is the highest amount of OvertimePay in the dataset ? **"""

sal['OvertimePay'].max()

"""** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **"""

sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']

"""** How much does JOSEPH DRISCOLL make (including benefits)? **"""

sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']

"""** What is the name of highest paid person (including benefits)?**"""

sal[sal['TotalPayBenefits']== sal['TotalPayBenefits'].max()]

"""** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**"""

sal[sal['TotalPayBenefits']== sal['TotalPayBenefits'].min()]

"""** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **"""

sal.groupby('Year')['BasePay'].mean()

"""** How many unique job titles are there? **"""

sal['JobTitle'].nunique()

"""** What are the top 5 most common jobs? **"""

sal['JobTitle'].value_counts().head(5)

"""** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **"""

sum(sal[sal['Year']==2013]['JobTitle'].value_counts()==1)

"""** How many people have the word Chief in their job title? (This is pretty tricky) **

The Job Titles are written in both upper and lower case. I convert all to upper, as well as the text to find to make things easier
"""

def has_Chief(job_title):
  text_to_find = 'Chief'
  text_to_find = text_to_find.upper()
  if text_to_find in job_title.upper().split():
    return 1
  else:
    return 0

sum(sal['JobTitle'].apply(lambda title:has_Chief(title)))

"""# Great Job!"""