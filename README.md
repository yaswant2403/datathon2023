# Statistically Significant Squad's Datathon Submission

### Problem Statement

In the financial industry, credit charge offs are a crucial metric to measure as they directly impact the health of the institution. A charge off occurs when a customer fails to make payment and eventually is written off as a loss. With that, it is increasingly important for banks to accurately forecast their charge offs in order to make informed decisions for the future.

Based on customer and macroeconomic data, forecast an accurate number of monthly charge offs over the period of February 2020 thru January 2021.

### Solution

To create our model, we took a survival analysis approach and utilized a basic Kaplan-Meier method to calculate the probability of no charge-offs in a month. We first tested our model over a time period of one year (2019), which we took from the provided training data. After stratifying by credit score, we were able to find the monthly survival probabilities for each credit score. Using what we had learned from testing our method on the training data and the calculated survival rates, we imported the forecast data to predict the amount of charge-offs for each month from Jan 2020-Feb 2021. We took into account credit score, and grouped by each score. Then, using our previously calculated score-specific survival rates based off our training data, we calculated the total number of charge-offs for each month, as well as the total amount of charge-offs in the year. 

### You can find more on our presentation [here](https://docs.google.com/presentation/d/1YLJwrh1emreDT9Y2ZghzMV_a2FkhC2q668_Oh5PBX_c/edit?usp=sharing).

This is the Statistically Significant Squad's Datathon 2023 submission!!!
