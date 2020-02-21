import eliza

# Get user's name
def intro():
    print('Hi, I am ELIZA.')
    print('Before we start the conversation please tell me your name.')

    user_input = ""
    while user_input == "":
        try:
            user_input = input('> ')
        except EOFError:
            print(input)
        if user_input:
            return user_input

def controller(user_name):
    print('Therapist\n---------')
    print('Talk to the program by typing in plain English, using normal upper-')
    print('and lower-case letters and punctuation.  Enter "quit" when done.')
    print('=' * 72)
    print('Hello, ' + user_name + '.  How are you feeling today?')

    user_input = ""
    bot = eliza.eliza(user_name)
    while user_input != "quit":
        try:
            user_input = input("> ")
        except EOFError:
            print(user_input)
        if user_input:
            while user_input[-1] in "!.":
                user_input = user_input[:-1]
        print(bot.respond(user_input))

if __name__ == "__main__":
    # Load the intro to get user's name
    username = ""
    username = intro()
    # The main controller to run eliza
    if username != "":
        controller(username)