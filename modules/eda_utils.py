import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def scatter(df: pd.DataFrame, x: str, y: str, title: str, xlabel: str, ylabel: str,
            alpha: float = 0.6, figsize=(8, 6)):
    plt.figure(figsize=figsize)
    sns.scatterplot(x=x, y=y, data=df, alpha=alpha)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def regplot(df: pd.DataFrame, x: str, y: str, title: str, xlabel: str, ylabel: str,
            alpha: float = 0.5, figsize=(8, 6)):
    plt.figure(figsize=figsize)
    sns.regplot(x=x, y=y, data=df, scatter_kws={"alpha": alpha})
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def corr(df: pd.DataFrame, x: str, y: str) -> float:
    return df[x].corr(df[y])

def heatmap_corr(df: pd.DataFrame, cols: list[str], title: str, figsize=(6, 5)):
    plt.figure(figsize=figsize)
    sns.heatmap(df[cols].corr(), annot=True, center=0)
    plt.title(title)
    plt.show()