def read_transcript(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    for _ in range(10):
        print(msg)

transcript_path = './transcript.txt'
message = read_transcript(transcript_path)
print_message(message)
