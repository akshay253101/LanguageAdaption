import matplotlib.pyplot as plt
import pandas as pd

# creates and save plot figure at the provided path
def create_plot(path: str):
    csv_path = path + ".csv"
    data = pd.read_csv(csv_path)

    # Only language data frame are required to plot values, dropping Tag and Date columns
    lang_data = data.copy().drop(["Tag", "Date"], axis = 1)

    # set figureSize to full screen
    plt.figure(figsize=(16,9), tight_layout=True)

    # Loop over languages detected in repo since first tag
    for lang in lang_data.columns:
        plt.plot(data.Date, data[lang], marker='o', label = lang)
        current_major_tag_version = "0"
        # Provide annotation for major version i.e, 5.6, 5.7, ignoring 5.6.1, 5.6.2
        for i, tag in enumerate(data.Tag):
            major_tag_version = ".".join(tag.split("v")[1].split(".")[:2])
            if major_tag_version > current_major_tag_version:
                plt.annotate(tag, xy=(data.at[i,"Date"], data.at[i,lang]),fontsize = 8, ha = 'left', va = "bottom", rotation = 70)
                current_major_tag_version = major_tag_version

    plt.grid(alpha=0.4)    
    plt.xticks(fontsize=8, rotation=70)
    plt.xlabel("Date of commit")
    plt.ylabel("LOC Percentage")
    plt.legend(loc='best', title='Languages')
    # Save figure as png
    plt.savefig(path + ".png")
    plt.show()