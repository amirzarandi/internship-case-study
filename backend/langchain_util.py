from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from openai_util import get_text_tokens

def get_context_langchain(input, budget):
    load_dotenv()

    # Load the OpenAI API key from the environment variable
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    # Set token limits
    max_tokens = min(16385, budget)  # Ensure max tokens doesn't exceed 16,385

    # Connect to the database
    engine = create_engine("sqlite:///instalily.db")
    db = SQLDatabase(engine=engine)

    # Initialize the language model
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    # Create the agent for SQL interaction
    agent_executor = create_sql_agent(
        llm, db=db, agent_type="openai-tools", verbose=True
    )

    # Construct the context query prompt
    context_query = f"Retrieve context from instaliliy related to: {input}. When interacting with the instaliliy table, prioritize returning the top 10 rows by default, unless explicitly asked for the entire table. If the entire instaliliy table is requested, summarize the information"

    # Estimate the token count for the input message
    initial_token_count = get_text_tokens(context_query)
    if initial_token_count > max_tokens:
        print(f"Input is too long. Estimated {initial_token_count} tokens exceed the max allowed ({max_tokens}).")
        return

    try:
        # Run the context query within token limits
        result = agent_executor.invoke({"input": context_query, "max_tokens": max_tokens - initial_token_count})
        return result["output"]
    except Exception as e:
        print("Error while fetching context:", e)