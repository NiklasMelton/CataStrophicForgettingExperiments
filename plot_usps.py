import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_parquet("usps.parquet")
data.sort_values(by="spacing", inplace=True)

for model, model_group in data.groupby("model"):
    fig, ax = plt.subplots(1, 3)

    randomized = size_group[size_group["shuffle"]=="True"]
    ordered = size_group[size_group["shuffle"]=="False"]
    semi = size_group[size_group["shuffle"]=="semi"]

    for i, df in enumerate([randomized, ordered, semi]):
        ax[j, i].plot(df["spacing"], df["accuracy"], label="accuracy")
        ax[j, i].plot(df["spacing"], df["precision"], label="precision")
        ax[j, i].plot(df["spacing"], df["recall"], label="recall")
        ax[j, i].plot(df["spacing"], df["f1"], label="F1")
        ax[j, i].plot(df["spacing"], df["sil_test"], label="Silhouette")
        ax[j, i].legend()
        if i == 0:
            ax[j, i].set_title(f"Randomize Results")
        elif i == 1:
            ax[j, i].set_title(f"Ordered Results")
        else:
            ax[j, i].set_title(f"Semi-Ordered Results")
    fig.suptitle(model)
plt.show()