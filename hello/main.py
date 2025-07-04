import os
import logging
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv

load_dotenv()

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("openai").setLevel(logging.WARNING)

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client= external_client
)

config = RunConfig(
    model= model,
    model_provider= external_client,
    tracing_disabled= True
)

agent = Agent(name="Smart Student Assistance",  instructions="you are a helpfull assistance.", model=model)


result = Runner.run_sync(agent, input="Hello how are you?", run_config=config)
print(result.final_output)

