from typing import List
from pydantic import BaseModel
from openai import OpenAI
from data_types import TranscriptAnalysis

client = OpenAI()

def analyse_transcript(transcript: str) -> TranscriptAnalysis:
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "You are a helpful assistant analyzing transcripts."},
            {"role": "user", "content": transcript},
        ],
        response_format=TranscriptAnalysis,
    )

    message = completion.choices[0].message
    if message.parsed:
        return message.parsed
    else:
        raise ValueError("Failed to parse the transcript analysis response.")
