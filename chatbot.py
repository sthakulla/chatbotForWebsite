from textblob import TextBlob

end_keywords = ["end", "end chat", "finish", "quit", "bye", "exit"]

intents_data = {
    "hours": {
        "keywords": ["hours", "open", "close"],
        "response": "We are open from 10 AM to 7 PM, from Monday to Saturday. And, 11 AM to 6:30 PM  on Sunday."
    },
    "return" : {
        "keywords": ["refund", "money back", "return"],
        "response": "I'd be happy to help you with the return process. Let me transfer you to a live agent."
    }
}

class ChatBot:
    def __init__(self):
        # Initializing the sentiment analysis tool.
        self.sentiment_analyzer = TextBlob("")

    def start_chat(self):
        print("ChatBot: Hi, how can I help you?")
        while True:
            user_message = input("You: ").strip().lower()
            
            if any(keyword in user_message for keyword in end_keywords):
                break

            # Analyzing the sentiment of the user's message.
            self.sentiment_analyzer = TextBlob(user_message)
            sentiment_score = self.sentiment_analyzer.sentiment.polarity

            # Generating the chatbot's response based on sentiment.
            if sentiment_score > 0:
                chatbot_message = f"ChatBot: That's great to hear!\n"
            elif sentiment_score < 0:
                chatbot_message = f"ChatBot: I'm sorry to hear that.\n"
            else:
                chatbot_message = f"ChatBot: Hmm, I see.\n"

            # Printing the chatbot's response and sentiment.
            print(chatbot_message)
            
            response_message = self.get_response(user_message)
            print(response_message +"\n")
            
        
        print("Thank you for using Chatbot. Hope you had a pleasant experience!\n")

    def get_response(self, text):
        text = text.lower()
        # Analyzing the sentiment of the user's message.
        # if any(word in text for word in intents["keywords"]):
        for intent, data in intents_data.items():
            for keyword in data["keywords"]:
                if keyword in text:
                    return data["response"]

        # Default response if no keyword is matched
        return "I'm sorry, I couldn't understand your query."
                

if __name__ == "__main__":
    # Creating the chatbot and starting the chat loop.
    chatbot = ChatBot()
    chatbot.start_chat()
