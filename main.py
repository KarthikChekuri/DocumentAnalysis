from arg_parse import parse_arguments
from constants import WORD_BLACKLIST
from llm import analyse_transcript
from output_format import format_as_str, format_as_json, format_as_markdown

def read_transcript(file_path):
    with open(file_path, 'r') as file:
        return file.read()

args = parse_arguments()
transcript_path = args.transcript_file
def count_word_frequency(text):
    words = [word.strip('.,!?').lower() for word in text.split() if word.strip('.,!?').lower() not in WORD_BLACKLIST]
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
    print("Word Frequency:")
    for word, count in sorted(word_frequency.items(), key=lambda item: item[1], reverse=True):
        if count > args.min_count:
            print(f"{word} ({count}): {'#' * count}")
message = read_transcript(transcript_path)
print_message(message)

# Analyze the transcript and print the results
word_frequency = count_word_frequency(message)
analysis = analyse_transcript(message, word_frequency)
# Determine the output format and file extension
output_format = args.output_format
if output_format == 'json':
    format_function = format_as_json
    file_extension = 'json'
elif output_format == 'markdown':
    format_function = format_as_markdown
    file_extension = 'md'
else:
    format_function = format_as_str
    file_extension = 'txt'

# Save the formatted analysis to a file
formatted_analysis = format_function(analysis)
output_file_path = f"transcript_analysis.{file_extension}"
with open(output_file_path, 'w') as output_file:
    output_file.write(formatted_analysis)

print(f"\nTranscript analysis saved to {output_file_path}")
