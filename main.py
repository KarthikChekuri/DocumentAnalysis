from arg_parse import parse_arguments
from constants import WORD_BLACKLIST
from llm import analyse_transcript
from output_format import format_as_str, format_as_json, format_as_markdown, format_as_yaml
from chart import word_count_bar_chart

def read_transcript(file_path):
    with open(file_path, 'r') as file:
        return file.read()

args = parse_arguments()
args.min_count = args.min_count or 10  # Set default min_count to 10 if not provided
transcript_path = args.transcript_file
def count_word_frequency(text):
    words = [word.strip('.,!?').lower() for word in text.split() if word.strip('.,!?').lower() not in WORD_BLACKLIST]
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    # Filter words based on the minimum count threshold
    threshold_word_frequency = {word: count for word, count in frequency.items() if count > args.min_count}
    return threshold_word_frequency


def print_message(msg):
    print(msg)
    word_frequency = count_word_frequency(msg)
    # Filter words based on the minimum count threshold
    threshold_word_frequency = {word: count for word, count in word_frequency.items() if count > args.min_count}
    
    # Display the word count bar chart
    word_count_bar_chart(threshold_word_frequency)
message = read_transcript(transcript_path)
print_message(message)

# Analyze the transcript and print the results
word_frequency = count_word_frequency(message)
analysis = analyse_transcript(message, word_frequency)
# Determine the output format and file extension
format_function = {
    'json': format_as_json,
    'markdown': format_as_markdown,
    'text': format_as_str,
    'yaml': format_as_yaml
}.get(args.output_format, format_as_str)

file_extension = {
    'json': 'json',
    'markdown': 'md',
    'text': 'txt',
    'yaml': 'yaml'
}.get(args.output_format, 'txt')

# Save the formatted analysis to a file
formatted_analysis = format_function(analysis)
output_file_path = f"transcript_analysis.{file_extension}"
with open(output_file_path, 'w') as output_file:
    output_file.write(formatted_analysis)

print(f"\nTranscript analysis saved to {output_file_path}")
