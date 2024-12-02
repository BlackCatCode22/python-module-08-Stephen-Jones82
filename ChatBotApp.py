# ChatBotApp.py
# Starter code for Python Chat Bot Program
#CIT-95 (Mohle) Spring 2024
# last updated: 4/24/24 by dH
#Suggested things to do:
# Add chat memory
#Use a local server like streamlit
# Modify streamlit with HTML to make a nice looking chatbot
# Use Langchain framework to read .pdf files
#Use an open source LLH that doesn't cost tokens
# pip install this dependency if you don't have this already
#pip install openai

import openai


# User-defined function go here, before the main() function (is a Python coding convention)
def generate_response(user_input):
    try:
       #Call the OpenAI API to generate a response
       completion = openai.ChatCompletion.create(
           # Find the model pricing page at OpenAI and examine your token usage with different models.
           model="gpt-3.5-turbo",
           messages=[{"role": "system", "content": "Assume the role of a Python teacher, and think step by step. Your name is Smarty pants."},
                     {"role": "user", "content": user_input}]

       )


#Extract the text of the response
       response_text = completion['choices'][0]['message']['content']
       return response_text
    except Exception as e:
    # Print an error message if the API call fails
        print("Error generating response:", e)
        return "I'm sorry, I couldn't generate a response."



def main():
    # This API key will not work (Because I deleted it after the video)
    # Use your own from OpenAI (there is a cost for this, but it is not much if you do not deploy
    # your app and have thousands of users) Typically, your API key will be in another Python file that
    # GitHub will not fork when asked to download
    # https://platform.openai.com/api-keys
    openai.api_key = ("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")
    # Print a welcome message
    print("\nWelcome to the Smarty pants simulator bot! Type 'quit' to exit.\n")

    # This loop will run until the break after user input "quit"
    while True:
        # Get user input.
        user_input = input("Python student question: ")

        # Check if user wants to quit the chatbot
        if user_input.lower() == "quit":
            print("Existing Python Study Bot.")
            break

        response = generate_response(user_input)

        # Print the response
        print("Python Study Bot:", response)

if __name__ == "__main__":
    main()