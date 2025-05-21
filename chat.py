import matplotlib.pyplot as plt

def word_count_bar_chart(word_count: dict):
    "Display a horizontal bar chart of word counts sorted in descending order"
    
    # Sort the word count dictionary by count in descending order
    sorted_word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    
    # Unpack the sorted word count into two lists
    words, counts = zip(*sorted_word_count)
    
    # Create a horizontal bar chart
    plt.barh(words, counts)
    plt.xlabel('Frequency')
    plt.title('Word Frequency Bar Chart')
    plt.gca().invert_yaxis()  # Invert y-axis to have the highest count on top
    plt.show()
