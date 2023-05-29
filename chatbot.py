knowledge_base = {
    "father": "A father is a male parent.",
    "mother": "A nother is a female parent.",
    "husband": "A husband is a male spouse.",
    "male": "A male is a man or a boy",
    "female": "A female is a woman or a girl",
    "spouse": "A spouse is a married person",
    "inlaw": "An inlaw is a person related by marriage",
    "family": "A family is a group of two or more persons related by birth, marriage, or adoption who live together",
    "parent": "A parent is the caregiver of a child.",
    "child": "A child is a young person between infancy and puberty",
    "person": "A person is a human being regarded as an individual.",
    "being": "A human being is a man, woman, or child.",
    "marriage": "A marriage is a union between man and woman called spouses.",
}

def chat():

    while True:
        user_input = input("User: ")
        if(user_input.lower().startswith('hello') or user_input.lower().startswith('hi')):
            print("Chatbot: Hello there! what would you like to know today?")
            continue
        if user_input.lower() == "bye" or user_input.lower().startswith("thank"):
            print("Chatbot: Sure, Goodbye!")
            break
        if (user_input.lower().startswith('who is') or user_input.lower().startswith('what is')) and user_input.endswith('?'):
            keyword = user_input.rstrip('?').lower().split(' ')[-1];
            if keyword in knowledge_base:
                print("Chatbot:", knowledge_base[keyword])
            else:
                print("Chatbot: I'm sorry, I do not have a definition for that.")
        elif user_input.lower().endswith('?'):
            print("Chatbot:", "I'm sorry, I do not have an answer to that question. Could you ask another?")
        else:
            print("Chatbot:", "I'm not sure I know how to respond to that. Please could you rephrase?")

chat();
