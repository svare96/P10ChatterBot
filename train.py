from main import chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "./data/english"
)

# from chatterbot.trainers import ListTrainer

# trainer = ListTrainer(chatbot)

# trainer.train([
#     "Hi there!",
#     "Hello",
# ])

# trainer.train([
#     "Greetings!",
#     "Hello",
# ])

# trainer.train([
#     "How are you?",
#     "I am good.",
#     "That is good to hear.",
#     "Thank you",
#     "You are welcome.",
# ])
