from data_types import TranscriptAnalysis
import json

def format_as_str(transcript: TranscriptAnalysis) -> str:
    output = []
    output.append(f"Quick Summary: {transcript.quick_summary}")
    output.append("Bullet Point Highlights:")
    for highlight in transcript.bullet_point_highlights:
        output.append(f"- {highlight}")
    output.append(f"Sentiment Analysis: {transcript.sentiment_analysis}")
    output.append("Keywords:")
    for keyword in transcript.keywords:
        output.append(f"- {keyword}")
    return "\n".join(output)

def format_as_json(transcript: TranscriptAnalysis) -> str:
    return json.dumps(transcript.dict(), indent=4)

def format_as_markdown(transcript: TranscriptAnalysis) -> str:
    output = []
    output.append(f"# Quick Summary\n\n{transcript.quick_summary}\n")
    output.append("## Bullet Point Highlights")
    for highlight in transcript.bullet_point_highlights:
        output.append(f"- {highlight}")
    output.append(f"\n## Sentiment Analysis\n\n{transcript.sentiment_analysis}\n")
    output.append("## Keywords")
    for keyword in transcript.keywords:
        output.append(f"- {keyword}")
    return "\n".join(output)
