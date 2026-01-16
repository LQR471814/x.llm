from openai import OpenAI
from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from rich import print


class JobDescription(BaseModel):
    position: str
    company_desc: str
    degree_required: Optional[str]
    qualifications: list[str]
    responsibilities: list[str]
    schedule: str


system_prompt = """
- Handshake is the name of a university job search platform.
"""

with open("desc.txt", "r") as f:
    desc = f.read()
    prompt = f"""
    Parse the following job description according to the JSON schema {JobDescription.model_json_schema()}:
    {desc}
    """

    client = OpenAI(base_url="http://192.168.1.12:8000/v1", api_key="none")
    response = client.beta.chat.completions.parse(
        model="Qwen/Qwen3-0.6B",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        response_format=JobDescription,
    )
    print(response)
