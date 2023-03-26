import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Group Subset of Training Data by Month
df = pd.read_csv("data/train_mini.csv")
all_months = df['mth_code'].unique()
month_statements = {}
for month in all_months:
    month_statements[month] = df[df.mth_code == month].reset_index()

# Replacing Credit Score Ranges with Median
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
ranges['Exception'] = 0
ranges['Missing'] = 0
for month in all_months:
    month_statements[month].replace({"bank_fico_buckets_20": ranges}, inplace=True)


# All Numerical variables
numerical_iv = ["bank_fico_buckets_20","mob","nbr_mths_due","variable_rate_margin","stmt_balance", "prev_balance","net_sales","net_payments",
                "credit_limit_amt","credit_limit_pa", "principal_amt", "total_writeoff_amt","fee_chg_off_reversal_amt", "net_finance_charge", 
                "non_principal_amount_gross","non_principal_amount_net", "non_principal_amount_stmt", "aged_writeoff_amt","bankruptcy_writeoff_amt", "fc_reversals", 
                "fee_reversals","fraud_writeoff_amt","other_writeoff_amt", "promo_bal_amt","recovery_amt"] #iv (x)

# Creating Dictionary with Key = Month : Val = Statements with only IV columns and charge-off
numerical_month_statements = {}
for month in all_months:
    d = {}
    for iv in numerical_iv:
        d[iv] = month_statements[month][iv]
    numerical_month_statements[month] = pd.DataFrame(data=d)

# Create Sample Correlation plots with specific independent variables
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
ax3.set_ylabel(r'$\ FICO\ Score\ $')
ax3.set_title('10/2019 - Charge-Offs based on FICO Score')

month = np.random.choice(np.asarray(all_months)) # set a random month 

# To generate distinct colors for scatter plots
def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)
colors = get_cmap(len(numerical_iv))

# Generating scatter plots for random months showcasing the 
# correlation between the different independent numerical variables
for iv in numerical_iv:
    x = numerical_month_statements[month][iv]
    y = month_statements[month]['charge_off']
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.scatter(y,x,c=colors(numerical_iv.index(iv)))
    ax.set_xlim(-0.5,1.5) # center the two tick marks in the middle
    ax.set_xticks([0,1],labels=[r'$No\ Charge-Off$', r'$Charge-Off$'])
    ax.set_xlabel(r'$\ Status\ of\ Charge-Off$')
    ax.set_ylabel(f'{iv}')
    ax.set_title(f'{str(month)[4:] + "/" + str(month)[:-2]} Charge-Offs Based on {iv}')

''''

ANALYSIS OF CATEGORICAL VARIABLES

'''

categorical = ["financial active", "net_payment_behaviour_tripd", "promotion_flag", "account_status_code", "ever_delinquent_flg", "active_12_mths",
                "open_closed_flag", "purchase_active", "closed", "active", "charge_off", "charge_off_age", "charge_off_bk", "writeoff_type_bko", 
                "writeoff_type_fraud_kiting", "writeoff_type_fraud_synthetic", "writeoff_type_deceased", "writeoff_type_other", "writeoff_type_aged",
                "writeoff_type_settlement", "writeoff_type_fraud_other", "writeoff_type_repo", "writeoff_type_null", "industry", "writeoffdate", "chargeoffreasoncode", varrateidx]
# Set up crosstab for categorical variables
col_array = [month_statements[month]['financial_active'], month_statements[month]['net_payment_behaviour_tripd'], 
            month_statements[month]['promotion_flag'], month_statements[month]['account_status_code'], 
            month_statements[month]['ever_delinquent_flg'], month_statements[month]['active_12_mths'], month_statements[month]['open_closed_flag'],
            month_statements[month]['purchase_active'], month_statements[month]['closed'], month_statements[month]['active'], month_statements[month]['charge_off'],
            month_statements[month]['charge_off_aged'], month_statements[month]['charge_off_bk'], month_statements[month]['writeoff_type_bko'],
            month_statements[month]['writeoff_type_fraud_kiting'], month_statements[month]['writeoff_type_fraud_synthetic'], 
            month_statements[month]['writeoff_type_deceased'], month_statements[month]['writeoff_type_other'], month_statements[month]['writeoff_type_aged'],
            month_statements[month]['writeoff_type_settlement'], month_statements[month]['writeoff_type_fraud_other'], month_statements[month]['writeoff_type_repo'],
            month_statements[month]['writeoff_type_null'], month_statements[month]['industry']]
crosstab = pd.crosstab(month_statements[month]['charge_off'],
                    col_array, margins=True, margins_name="Total")




