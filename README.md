### Can a Risk Matrix Hide a Red Flag?

Final project for the course Math Concepts for Developers.



##### Overview

Financial institutions use customer risk rating models to assess money-laundering risk. These models often combine several risk factors into a single score using a weighted average.



This project investigates a potential weakness of that approach: a customer may have a significant warning sign (a red flag) on one factor but still receive an overall Low-risk rating because low scores on other factors offset it.



##### The project:



* builds a simple risk matrix with five risk factors;
* analyses the mathematics behind weighted-average scoring;
* generates a synthetic population of customers;
* measures how often red flags are hidden by the scoring model;
* tests alternative weighting schemes and a simple red-flag rule.



##### Files

notebook.ipynb – complete analysis and results

risk\_model.py – helper functions used by the notebook

requirements.txt – project dependencies



##### Author

Yana Stoyanova

