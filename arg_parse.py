import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process a transcript file.')
    parser.add_argument('transcript_file', type=str, help='Path to the transcript file')
    parser.add_argument('--min_count', type=int, default=3, help='Minimum count for word frequency display')
    parser.add_argument('--output_format', type=str, choices=['json', 'markdown', 'text', 'yaml'], default='text', help='Output format for the analysis')
    return parser.parse_args()
