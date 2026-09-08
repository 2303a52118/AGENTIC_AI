# Import os so that environment variables can be accessed from Python.
import os

# Import load_dotenv so that variables stored inside the .env file
# can be loaded into the Python environment.
from dotenv import load_dotenv

# Import ChatOpenRouter for communicating with models through OpenRouter.
from langchain_openrouter import ChatOpenRouter


# Load variables stored in the local .env file.
load_dotenv()


# Read the OpenRouter API key from the environment.
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

# Read the model name from the environment.
model_name = os.getenv("MODEL_NAME")


# Check whether the OpenRouter API key exists.
if not openrouter_api_key:
    raise ValueError(
        "OPENROUTER_API_KEY is missing. Please add it to the .env file."
    )


# Check whether the model name exists.
if not model_name:
    raise ValueError(
        "MODEL_NAME is missing. Please add it to the .env file."
    )


# Create the LangChain chat model object.
llm = ChatOpenRouter(
    # OpenRouter model name.
    model=model_name,

    # OpenRouter API key.
    api_key=openrouter_api_key,

    # Make responses more deterministic.
    temperature=1,

    # Maximum response length.
    max_tokens=1024,

    # Retry failed requests twice.
    max_retries=2,
)


# Display application heading.
print("\n==========================================")
print(" LangChain Simple Question Answering Agent ")
print("==========================================\n")


# Start an infinite loop.
while True:

    # Get a question from the user.
    question = input("Enter your question: ")

    # Remove unnecessary spaces.
    question = question.strip()

    # Check whether the user wants to exit.
    if question.lower() in ["exit", "quit", "q"]:
        print("\nExiting the LangChain QA application.")
        break

    # Check for an empty question.
    if not question:
        print("Please enter a question.\n")
        continue

    # Show processing message.
    print("\nGenerating answer...\n")

    try:

        # Send the question to the LLM.
        response = llm.invoke(question)

        # Extract the answer.
        answer = response.content

        # Display the answer.
        print("Answer:")
        print(answer)

        # Separator.
        print("\n------------------------------------------\n")

    except Exception as error:

        # Display a friendly error message.
        print("An error occurred while generating the answer.")

        # Display the actual error.
        print(f"Error details: {error}")

        print()