import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=300,
    messages=[
        {
            "role": "user",
            "content": "What should i search to find out the latest ai models in claude?"
        }
    ]
)

for block in message.content:
    if block.type == "text":
        print(block.text)