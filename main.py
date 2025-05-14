def read_transcript(file_path):
    with open(file_path, 'r') as file:
        return file.read()

transcript_path = './transcript.txt'
def count_word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def print_message(msg):
    print(msg)
    word_frequency = count_word_frequency(msg)
    print("Word Frequency:", word_frequency)
message = read_transcript(transcript_path)
print_message(message)
