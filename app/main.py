import anthropic
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()

app = FastAPI()
client = anthropic.AsyncAnthropic()

class ChatRequest(BaseModel):
    messsage: str

@app.post("/chat")
async def chat(body: ChatRequest):
    response = await client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=300,
        messages=[
            {"role": "user", "content": body.messsage}
        ]
    )

    text = "".join(block.text for block in response.content if block.type == "text")
    return {"message": text}