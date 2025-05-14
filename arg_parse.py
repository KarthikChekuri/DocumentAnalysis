import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process a transcript file.')
    parser.add_argument('transcript_file', type=str, help='Path to the transcript file')
    return parser.parse_args()
