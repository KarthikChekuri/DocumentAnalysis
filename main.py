from arg_parse import parse_arguments

def read_transcript(file_path):
    with open(file_path, 'r') as file:
        return file.read()

args = parse_arguments()
transcript_path = args.transcript_file
def count_word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def print_message(msg, min_count=3):
    print(msg)
    word_frequency = count_word_frequency(msg)
    print("Word Frequency:")
    for word, count in sorted(word_frequency.items(), key=lambda item: item[1], reverse=True):
        if count > min_count:
            print(f"{word} ({count}): {'#' * count}")
message = read_transcript(transcript_path)
print_message(message)
