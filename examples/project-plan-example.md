# Project Plan

## Title
<!-- Give your project a short title. -->
IEEE-CIS Fraud Detection.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
How can we predict the probability that an online transaction is fraudulent, based on the binary target "isFraud"?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
The dataset is of fraud detection consists of transaction and identity files linked by TransactionID. The transaction file includes categorical features related to payment details and email domains, while the identity file provides additional user verification data. The TransactionDT feature indicates time as a delta from a reference point, not as a timestamp. Participants must predict the 'isFraud' binary target for the test set, with the training set including this target for model development.

## Datasources

This specific dataset is collected from Kaggle, a very popular data science competition organizer and datasets provider. 

### Datasource1: ExampleSource
* Test_Identity_Data URL: https://www.kaggle.com/competitions/ieee-fraud-detection/data?select=test_identity.csv
* Test_transaction_Data URL: https://www.kaggle.com/competitions/ieee-fraud-detection/data?select=test_transaction.csv
* Train_Identity_Data URL: https://www.kaggle.com/competitions/ieee-fraud-detection/data?select=train_identity.csv
* Train_transaction_Data URL: https://www.kaggle.com/competitions/ieee-fraud-detection/data?select=train_transaction.csv
* Data Type: CSV

Short description of the DataSource.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Example Issue [#1][i1]
2. ...

[i1]: https://github.com/jvalue/made-template/issues/1
