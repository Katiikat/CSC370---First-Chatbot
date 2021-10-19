import random

#create a function to color and return text
def colour(clr, msg):
    #used a format string to generate ANSI escape sequence for color and clear
    #https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_parameters
    return f"\033[1;{clr}m{msg}\033[0m"

def instructions():
    print(colour(34, "This is a really simple chatbot."))
    print(colour(34, "If you wish, you may name this chatbot anything you like"))
    print(colour(34, "by typing \"Y\" or \"N\" when prompted."))
    print(colour(34, "Otherwise, text this chatbot like you would normally, and enjoy!\n\n"))

def intro():
    give_name = input("Would you like to give your bot a name? Y/N\n")
    give_name = give_name.upper()

    if give_name == "Y" or give_name == "YES":
        name = input("What would you like to name your bot?\n")
    else:
        num = random.choice([0,1])
        print(f"Num = {num}")
        if num == 1:
            name = "Smith"
        elif num == 0:
            name = "Samantha"
        else:
            name = "Riley"
    # This should be a better intro to the user
    print(f"\n\nWelcome. My name is {name}. I'm excited to talk with you.")


def personality():
    pass

def main():
    # import the chatterbot package
    # This is the chatbot engine we will use
    from chatterbot import ChatBot

    #Give our chatbot a name
    chatbot = ChatBot("HAL 9000")

    # packages used to train your chatbot
    # from chatterbot.trainers import ListTrainer
    from chatterbot.trainers import ChatterBotCorpusTrainer

    # Set the trainers we want to train
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Now here we actually train our chatbot on the corpus
    # This is what gives our chatbot its personality
    trainer.train("chatterbot.corpus.english")

    instructions()
    intro()

    # Main loop for our chatbot to keep talking
    # Where the chatbot interacts with user
    # otherwise keep looping
    is_exit = False
    while not is_exit:
        # get user input
        user_input = input()
        # Intercept specific user response here and override the chatbot
        # We will do this by testing a condition first
        if user_input.lower().find("bye") != -1:
            # flip this flag if user wants to leave chat
            is_exit = True
            print("It was great chatting with you. Have a great day.")
        else:
            bot_response = chatbot.get_response(user_input)
            print(bot_response)

if __name__ == "__main__":
    main()