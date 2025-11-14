import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def perform_eda(df):
    """
    Performs EDA including descriptive statistics, outlier detection,
    and correlation analysis.

    Parameters:
    df (DataFrame): A DataFrame containing data for EDA.
    """

    # 1. Descriptive Statistics
    print("Descriptive Statistics:")
    print(df.describe())

    # 2. Outlier Detection (using Boxplot)
    plt.figure(figsize=(10, 5))
    sns.boxplot(data=df)
    plt.title("Boxplot for Outlier Detection")

    # 3. Correlation Analysis (using Heatmap)
    correlation_matrix = df.corr()
    print("\nCorrelation Matrix:")
    print(correlation_matrix)

    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Correlation Heatmap")

    plt.close('all')


# Example data
df = pd.DataFrame({
    'A': np.random.rand(50),
    'B': np.random.rand(50) * 10,
    'C': np.random.rand(50) * 100
})
perform_eda(df)