from textbase import bot, Message
from textbase.models import OpenAI
from typing import List

# Load your OpenAI API key
OpenAI.api_key = "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"

# Prompt for GPT-3.5 Turbo
MENTAL_HEALTH_PROMPT = """You are chatting with a mental health bot. Feel free to share your thoughts and feelings, and the bot will provide supportive responses."""
def create_bot_response(raw_response):
    # Process the raw response (you can add your custom logic here)
    processed_response = process_raw_response(raw_response)
    
    # Construct a message in the desired format
    bot_message = {
        "role": "assistant",
        "content": [
            {
                "data_type": "STRING",
                "value": processed_response
            }
        ]
    }

    return bot_message

def process_raw_response(raw_response):
    return "Mental Health Bot: " + raw_response
def handle_loneliness(message_history: List[Message]):
    # Construct a message history with the user's message and the system's message
    message_history_with_prompt = message_history + [
        Message(role="system", content=[{"data_type": "STRING", "value": MENTAL_HEALTH_PROMPT}]),
        Message(role="user", content=[{"data_type": "STRING", "value": "I'm feeling lonely and need someone to talk to."}])
    ]

    # Call GPT-3.5 Turbo with the updated message history
    response = OpenAI.generate(
        messages=message_history_with_prompt,
        model="gpt-3.5-turbo"
    )

    return response

def handle_sadness(message_history: List[Message]):
    # Construct a message history with the user's message and the system's message
    message_history_with_prompt = message_history + [
        Message(role="system", content=[{"data_type": "STRING", "value": MENTAL_HEALTH_PROMPT}]),
        Message(role="user", content=[{"data_type": "STRING", "value": "I'm feeling really sad and deppressed and don't know what to do."}])
    ]

    # Call GPT-3.5 Turbo with the updated message history
    response = OpenAI.generate(
        messages=message_history_with_prompt,
        model="gpt-3.5-turbo"
    )
    
    return response

def generate_general_response(message_history: List[Message]):
    # Construct a message history with the user's message and the system's message
    message_history_with_prompt = message_history + [
        Message(role="system", content=[{"data_type": "STRING", "value": MENTAL_HEALTH_PROMPT}]),
        Message(role="user", content=[{"data_type": "STRING", "value": "I'm not sure what you're feeling, but I'm here to help."}])
    ]

    # Call GPT-3.5 Turbo with the updated message history
    response = OpenAI.generate(
        messages=message_history_with_prompt,
        model="gpt-3.5-turbo"
    )
    
    return response

@bot()
def handle_stress(message_history: List[Message]):
    # Construct a message history with the user's message and the system's message
    message_history_with_prompt = message_history + [
        Message(role="system", content=[{"data_type": "STRING", "value": MENTAL_HEALTH_PROMPT}]),
        Message(role="user", content=[{"data_type": "STRING", "value": "I'm feeling stressed out and overwhelmed by everything."}])
    ]

    # Call GPT-3.5 Turbo with the updated message history
    response = OpenAI.generate(
        messages=message_history_with_prompt,
        model="gpt-3.5-turbo"
    )
    
    return response
def handle_nervous(message_history: List[Message]):
    # Construct a message history with the user's message and the system's message
    message_history_with_prompt = message_history + [
        Message(role="system", content=[{"data_type": "STRING", "value": MENTAL_HEALTH_PROMPT}]),
        Message(role="user", content=[{"data_type": "STRING", "value": "I'm feeling nervous right now!!"}])
    ]

    # Call GPT-3.5 Turbo with the updated message history
    response = OpenAI.generate(
        messages=message_history_with_prompt,
        model="gpt-3.5-turbo"
    )

    return response
def on_message(message_history: List[Message] = None, state: dict = None):
    if message_history is None:
        message_history = []  # Initialize with an empty list if not provided
    if message_history:
        print(type(message_history[-1]))
        print(message_history[-1])
        print(type(message_history[-1].content))
        print(message_history[-1].content)
        print(type(message_history[-1].content[0]))
        print(message_history[-1].content[0])

    user_message = message_history[-1].content[0].value if message_history else ""

    if "lonely" in user_message:
        bot_response = handle_loneliness(message_history)
    elif "sad" or "deppressed" in user_message:
        bot_response = handle_sadness(message_history)
    elif "stressed" in user_message:
        bot_response = handle_stress(message_history)
    elif "nervous" in user_message:
        bot_response = handle_nervous(message_history)
    else:
        bot_response = generate_general_response(message_history)

    response = {
        "data": {
            "messages": [bot_response],
            "state": state
        },
        "errors": []
    }

    return {
        "status_code": 200,
        "response": response
    }


