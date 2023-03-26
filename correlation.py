import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# 1) Group Training Data month by month (month : dataframe of all statements from month)
# 2) For each group, find correlation between charge off and variable
    # a) If variable continuous, then use correlation analysis
    # b) Categorical, use chi-square test

# So, what we've been able to do so far is create a survival analysis model where we generate the percentage of bank statements that have
# had a chargeoff based on credit score over the year of 2019. Now, we were thinking of using the percentage to help us predict the future
# chargeoffs of only one month. So, how do we use something that's scaled over a year to predict the future of one month?
# 1 month survival analysis but not possible

# Step 1
# Group Training Data by Month
df = pd.read_csv("data/train_mini.csv")
all_months = df['mth_code'].unique()
month_statements = {}
for month in all_months:
    month_statements[month] = df[df.mth_code == month].reset_index()

# Replacing Credit Score Ranges
scores = [(581,600),(721,740),(761,850),(661,680),(601,620), (701,720), (621,640), (561,580), (641,660), (741,760), (681,700),(560,300)]
medians = [(tup[0] + tup[1])/2 for tup in scores]
ranges = { }
for mid in medians:
    fico_range = scores[medians.index(mid)]
    if (fico_range[0] == 560):
        ranges['<= 560'] = mid
    elif (fico_range[0] == 761):
        ranges['761+'] = mid 
    else:
        key = str(fico_range[0]) + '-' + str(fico_range[1])
        ranges[key] = mid
for month in all_months:
    month_statements[month].replace({"bank_fico_buckets_20": ranges}, inplace=True)

# Numerical Variables

# Make a dataframe containing only numerical variables and chargeoff column
numerical_iv = ["bank_fico_buckets_20","mob","nbr_mths_due","variable_rate_margin","stmt_balance", "prev_balance","net_sales","net_payments",
                "credit_limit_amt","credit_limit_pa", "principal_amt", "total_writeoff_amt","fee_chg_off_reversal_amt", "net_finance_charge", 
                "non_principal_amount_gross","non_principal_amount_net", "non_principal_amount_stmt", "aged_writeoff_amt","bankruptcy_writeoff_amt", "fc_reversals", 
                "fee_reversals","fraud_writeoff_amt","other_writeoff_amt", "promo_bal_amt","recovery_amt"] #iv (x)
# charge_off is dv (y)
numerical_month_statements = {}
for month in all_months:
    d = {}
    for iv in numerical_iv:
        d[iv] = month_statements[month][iv]
    numerical_month_statements[month] = pd.DataFrame(data=d)

# create correlation plot
x = numerical_month_statements[201910]['principal_amt']
y = month_statements[201910]['charge_off']
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(y,x,color="lightblue")
ax.set_xlim(-0.5,1.5) # center the two tick marks in the middle
ax.set_xticks([0,1],labels=[r'$No\ Charge-Off$', r'$Charge-Off$'])
ax.set_xlabel(r'$\ Status\ of\ Charge-Off$')
ax.set_ylabel(r'$\ Principal\ Amount\ (\$) $')
ax.set_title('10/2019 - Charge-Offs based on Principal Amount')

x2 = numerical_month_statements[201910]['credit_limit_amt']
y2 = month_statements[201910]['charge_off']
fig2 = plt.figure()
ax2 = fig2.add_subplot(1,1,1)
ax2.scatter(y2,x2,color="red")
ax2.set_xlim(-0.5,1.5) # center the two tick marks in the middle
ax2.set_xticks([0,1],labels=[r'$No\ Charge-Off$', r'$Charge-Off$'])
ax2.set_xlabel(r'$\ Status\ of\ Charge-Off$')
ax2.set_ylabel(r'$\ Credit\ Limit\ (\$) $')
ax2.set_title('10/2019 - Charge-Offs based on Credit Limit')

x3 = numerical_month_statements[201910]['bank_fico_buckets_20']
y3 = month_statements[201910]['charge_off']
fig3 = plt.figure()
ax3 = fig3.add_subplot(1,1,1)
ax3.scatter(y3,x3,color="lightgreen")
ax3.set_xlim(-0.5,1.5) # center the two tick marks in the middle
ax3.set_xticks([0,1],labels=[r'$No\ Charge-Off$', r'$Charge-Off$'])
ax3.set_xlabel(r'$\ Status\ of\ Charge-Off$')
ax3.set_ylabel(r'$\ FICO\ Limit\ (\$) $')
ax3.set_title('10/2019 - Charge-Offs based on FICO Score')

# for iv in numerical_iv:
#     x = numerical_month_statements[month][iv]
#     y = month_statements[month]['charge_off']
#     fig = plt.figure()
#     ax = fig.add_subplot(1,1,1)
#     ax.scatter(y,x,color="lightblue")
#     ax.set_xlim(-0.5,1.5) # center the two tick marks in the middle
#     ax.set_xticks([0,1],labels=[r'$No\ Charge-Off$', r'$Charge-Off$'])
#     ax.set_xlabel(r'$\ Status\ of\ Charge-Off$')
#     ax.set_ylabel(r'$\ {iv}\ (\$) $')
#     ax.set_title(f'Charge-Offs based on {iv}')

# create correlation tests



# Categorical Variables
# #categorical = ["financial active", "net_payment_behaviour_tripd", "promotion_flag", "account_status_code", "ever_delinquent_flg", "active_12_mths",
#                 "open_closed_flag", "purchase_active", "closed", "active", "charge_off", "charge_off_age", "charge_off_bk", "writeoff_type_bko", 
#                 "writeoff_type_fraud_kiting", "writeoff_type_fraud_synthetic", "writeoff_type_deceased", "writeoff_type_other", "writeoff_type_aged",
#                 "writeoff_type_settlement", "writeoff_type_fraud_other", "writeoff_type_repo", "writeoff_type_null", "industry", "writeoffdate", "chargeoffreasoncode", varrateidx]
# Make a dataframe containing only categorical variables and chargeoff column
# do df.corr()
# create correlation plot
# create correlation tests


# Step 2
# 



