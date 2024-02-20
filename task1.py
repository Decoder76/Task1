import pandas as pd
import numpy as np
# import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def exercise_0(file):
    transaction = pd.read_csv(file)
    return transaction

def exercise_1(df):
    column_names = df.columns.tolist()
    return column_names


def exercise_2(df, k):
    return df.head(k)

def exercise_3(df, k):
    return df.sample(k)

def exercise_4(df):
    unicorn = df['type'].unique().tolist()
    return unicorn

def exercise_5(df):
    top_destinations = df['nameDest'].value_counts().head(10)
    return top_destinations

def exercise_6(df):
    fraudulent_rows = df[df['isFraud'] == 1]
    return fraudulent_rows

def exercise_7(df):
    distinct_destinations = df.groupby('nameOrig')['nameDest'].nunique().reset_index()
    distinct_destinations_sorted = distinct_destinations.sort_values(by='nameDest', ascending=False)

    return distinct_destinations_sorted
    
def visual_1(df):
    # Transaction types bar chart
    transaction_type_counts = df['type'].value_counts()
    plt.figure(figsize=(8, 6))
    transaction_type_counts.plot(kind='bar')
    plt.title('Transaction Types')
    plt.xlabel('Transaction Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Transaction types split by fraud bar chart
    transaction_types_fraud = df.groupby(['type', 'isFraud']).size().unstack()
    transaction_types_fraud.plot(kind='bar', stacked=True)
    plt.title('Transaction Types Split by Fraud')
    plt.xlabel('Transaction Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return "The transaction types bar chart provides an overview of the distribution of different types of transactions. The transaction types split by fraud bar chart shows how fraud is distributed across different transaction types."

def visual_2(df):
    cash_out_transactions = df[df['type'] == 'CASH_OUT']
    plt.figure(figsize=(8, 6))
    plt.scatter(cash_out_transactions['oldbalanceOrg'] - cash_out_transactions['newbalanceOrig'], cash_out_transactions['oldbalanceDest'] - cash_out_transactions['newbalanceDest'])
    plt.title('Origin Account Balance Delta vs. Destination Account Balance Delta (Cash Out Transactions)')
    plt.xlabel('Origin Account Balance Delta')
    plt.ylabel('Destination Account Balance Delta')
    plt.tight_layout()
    plt.show()

    return "The scatter plot of Origin Account Balance Delta vs Destination Account Balance Delta for Cash Out transactions helps visualize the relationship between these variables in Cash Out transactions."

def exercise_custom(df):
    return df.style.pipe(make_pretty)
    
def visual_custom(df):
    # Extract column names
    column_names = df.columns.tolist()

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(column_names))

    # Display the word cloud
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Column Names Word Cloud')
    plt.show()


    # Create a pie chart of transaction type percentages
    transaction_type_counts = df['type'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(transaction_type_counts, labels=transaction_type_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Transaction Type Distribution')
    plt.show()

    return "The visualizations provide insights into the transaction dataset."