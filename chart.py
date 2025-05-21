import matplotlib.pyplot as plt

def word_count_bar_chart(threshold_count: dict):
    # Sort the dictionary by value in descending order
    sorted_items = sorted(threshold_count.items(), key=lambda item: item[1], reverse=True)
    words, counts = zip(*sorted_items)

    plt.barh(words, counts)
    plt.xlabel('Frequency')
    plt.title('Word Frequency Bar Chart')
    plt.gca().invert_yaxis()  # Invert y-axis to have the highest frequency on top
    plt.show()
