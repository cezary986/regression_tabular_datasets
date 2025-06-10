import pandas as pd


def read_full_dataset(dataset_name: str) -> tuple[pd.DataFrame, pd.Series]:
    pass


def read_dataset_train_test(dataset_name: str, cv_fold: int) -> tuple[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]:
    if cv_fold < 1 or cv_fold > 10:
        raise ValueError("cv_fold must be in range 1-10")
    pass

