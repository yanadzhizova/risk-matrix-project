# ***Can a Risk Matrix Hide a Red Flag?***



Final project for the course - *Math Concepts for Developers.*



##### **Overview**

Financial institutions use customer risk-rating models to assess money-laundering risk. These models often combine multiple risk factors into a single score using a weighted-average approach.



This project investigates a potential limitation of that approach: a customer may have an important warning sign (a red flag) on one factor but still receive an overall Low-risk classification because low ratings on other factors offset its effect.



The project combines mathematical analysis and simulation to examine how often this occurs and to evaluate possible improvements to the scoring model.



##### **Project Objectives**



The project:

* builds a simple risk matrix based on five risk factors;
* analyses the mathematics behind weighted-average scoring;
* generates a synthetic population of customers;
* measures how often red flags are hidden by the model;
* evaluates alternative weighting schemes;
* tests a red-flag rule as a possible solution;
* investigates the effect of alternative risk thresholds.



##### **Project Structure**

* notebook.ipynb – complete analysis, experiments, visualisations, and conclusions
* risk\_model.py – helper functions used throughout the notebook
* requirements.txt – project dependencies



##### **Technologies Used**

* Python
* NumPy
* pandas
* Matplotlib
* Jupyter Notebook



##### **Running the Project**

Open notebook.ipynb in Jupyter Notebook or JupyterLab and run all cells from top to bottom.

##### 

###### **Author**

Yana Stoyanova



###### **AI Disclosure**

**AI tools (Claude, by Anthropic) were used during the development of this project to support coding, debugging, and the presentation of results.**



**In particular, AI assistance was used when working with Python libraries such as pandas and Matplotlib, including the generation of code for creating the synthetic dataset, producing data visualizations, and refining parts of the written explanations and interpretation of results.**



**All mathematical reasoning, model design, experiments, analysis, conclusions, and final project decisions were reviewed, adapted, and validated by the author. The project content was not generated automatically and remains the author's own work.**

