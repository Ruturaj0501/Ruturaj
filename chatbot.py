import wikipedia
import spacy
import time

# Initialize spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Function to process user input using spaCy NLP
def process_input(user_input):
    # We can process the input, but for general knowledge, we can directly take the query as the topic
    return user_input.strip()

# Function to get general knowledge from Wikipedia
def get_wikipedia_summary(query):
    try:
        # Set the language of Wikipedia to English
        wikipedia.set_lang("en")
        
        # Get summary from Wikipedia for the query
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"There are multiple topics related to '{query}'. Please be more specific. For example, {e.options[:3]}"
    except wikipedia.exceptions.HTTPTimeoutError:
        return "Sorry, the Wikipedia service is temporarily unavailable. Please try again later."
    except wikipedia.exceptions.RedirectError:
        return "The topic you requested is a redirect. Please try another term."
    except wikipedia.exceptions.PageError:
        return f"Sorry, we couldn't find information on '{query}'. Please try another topic."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Function to interact with the user
def chatbot():
    print("Hello! Welcome to the General Knowledge Chatbot! Ask me anything.")
    time.sleep(1)
    print("You can ask about history, science, geography, people, and much more.\n")

    while True:
        print("Type 'exit' to quit.")
        user_input = input("Ask me a question: ")
        
        if user_input.lower() == 'exit':
            print("Thank you for using the General Knowledge Chatbot. Goodbye!")
            break
        
        # Process user input
        query = process_input(user_input)
        
        print("\nSearching for answers...\n")
        answer = get_wikipedia_summary(query)
        
        print(f"Answer: {answer}")
        print("\nWould you like to ask another question? (yes/no)")
        if input("> ").lower() != "yes":
            print("Thank you for using the General Knowledge Chatbot. Goodbye!")
            break

# Run the chatbot
if __name__ == "__main__":
    chatbot()