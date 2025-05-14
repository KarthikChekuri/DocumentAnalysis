def read_transcript(file_path):
    with open(file_path, 'r') as file:
        return file.read()

transcript_path = './transcript.txt'
    print(msg)
message = read_transcript(transcript_path)
print_message(message)
