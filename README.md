# Regression Tabular Datasets

This repository contains numerous benchmark tabular datasets for testing various classification algorithms.

All datasets are splitted to train and test parts. If whole unsplitted dataset was accessible it is also splitted into 10-fold cross validation datasets. Each dataset contains target column names **class** for prediction. Files in parquet data format is used which could be easily loaded using pandas Python package.


## Dataset Overview

| Dataset Name | Rows | Columns | Missing Values |
| :------------------------------------------------------------------------------------------------------ | :----- | :-------------------------------- | :------------- |
| [auto-mpg](https://archive.ics.uci.edu/dataset/9/auto+mpg) | 398 | 7 (4 numerical, 3 categorical) | Yes |
| [auto-price](https://archive.ics.uci.edu/dataset/10/automobile) | 159 | 15 (14 numerical, 1 categorical) | No |
| [auto93](https://www.openml.org/search?type=data&sort=version&status=any&order=asc&exact_name=auto93&id=569) | 93 | 22 (16 numerical, 6 categorical) | No |
| [bodyfat](https://www.kaggle.com/datasets/fedesoriano/body-fat-prediction-dataset) | 252 | 14 (14 numerical, 0 categorical) | No |
| [bolts](https://www.openml.org/search?type=data&status=active&id=193) | 40 | 7 (7 numerical, 0 categorical) | No |
| [breasttumor](https://archive.ics.uci.edu/dataset/14/breast+cancer) | 286 | 9 (1 numerical, 8 categorical) | No |
| [cholesterol](https://www.openml.org/d/204) | 303 | 13 (6 numerical, 7 categorical) | Yes |
| [cloud](https://www.kaggle.com/datasets/mathurinache/cloud-dataset) | 108 | 6 (4 numerical, 2 categorical) | No |
| [concrete](https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength) | 103 | 9 (9 numerical, 0 categorical) | No |
| [cpu](https://www.openml.org/d/561) | 209 | 7 (6 numerical, 1 categorical) | No |
| [dee](https://www.openml.org/search?type=data&status=active&id=42360) | 365 | 6 (6 numerical, 0 categorical) | No |
| [diabetes](https://archive.ics.uci.edu/dataset/34/diabetes) | 43 | 2 (2 numerical, 0 categorical) | No |
| [echomonths](https://archive.ics.uci.edu/dataset/38/echocardiogram) | 130 | 9 (6 numerical, 3 categorical) | Yes |
| [elusage](https://www.openml.org/search?type=data&status=active&id=228) | 55 | 2 (1 numerical, 1 categorical) | No |
| [fishcatch](https://www.openml.org/search?type=data&status=active&id=232) | 158 | 7 (5 numerical, 2 categorical) | No |
| [fruitfly](https://www.openml.org/search?type=data&status=active&id=199) | 125 | 4 (2 numerical, 2 categorical) | No |
| [gascons](https://www.openml.org/d/226) | 27 | 4 (4 numerical, 0 categorical) | No |
| [kidney](https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease) | 76 | 5 (3 numerical, 2 categorical) | No |
| [lowbwt](https://www.openml.org/search?type=data&status=active&id=203) | 189 | 9 (2 numerical, 7 categorical) | No |
| [machine](https://archive.ics.uci.edu/dataset/29/computer+hardware) | 209 | 6 (6 numerical, 0 categorical) | No |
| [mbagrade](https://www.openml.org/d/190) | 61 | 2 (1 numerical, 1 categorical) | No |
| [ozone](https://archive.ics.uci.edu/dataset/172/ozone+level+detection) | 330 | 8 (8 numerical, 0 categorical) | No |
| [pharynx](https://www.openml.org/d/213) | 195 | 11 (1 numerical, 10 categorical) | No |
| [pollution](https://www.openml.org/d/542) | 60 | 15 (15 numerical, 0 categorical) | No |
| [pwlinear](https://www.openml.org/search?type=data&id=721) | 200 | 10 (10 numerical, 0 categorical) | No |
| [pyrim](https://www.openml.org/search?type=data&status=active&id=217) | 74 | 27 (27 numerical, 0 categorical) | No |
| [servo](https://archive.ics.uci.edu/dataset/87/servo) | 167 | 4 (0 numerical, 4 categorical) | No |
| [strike](https://www.openml.org/search?type=data&status=active&id=549) | 625 | 6 (5 numerical, 1 categorical) | No |
| [veteran](https://www.openml.org/search?type=data&status=active&id=497) | 137 | 7 (3 numerical, 4 categorical) | No |

Dataset summary is also available in csv file [datasets_summary.csv](https://github.com/cezary986/regression_tabular_datasets/blob/main/datasets_summary.csv) in root repo directory.

## Reading datasets using Python package

This repository also contains a tiny Python package which allows you to use datasets without the need to clone whole repository.
 
 To install it use the following command:

```bash
pip install git+https://github.com/cezary986/regression_tabular_datasets
```

The package exports two functions: `read_full_dataset` and `read_dataset_train_test`.
The first one reads full dataset and returns a tuple of X and y, where X is data and y are labels.
The second one reads dataset splitted to train and test parts and returns a tuple of X_train, y_train, X_test, y_test. 

Example:

```python
import regdatasets

# print list of all available datasets
print(", ".join(regdatasets.AVAILABLE_DATASETS))

# reads whole dataset without train/test split
X, y = regdatasets.read_full_dataset("diabetes")

# reads dataset splitted into train/test
X_train, y_train, X_test, y_test = regdatasets.read_dataset_train_test("diabetes")

# reads given dataset cross-validation fold
X_train, y_train, X_test, y_test = regdatasets.read_dataset_train_test("diabetes",  cv_fold=3)
```