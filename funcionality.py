import random
import json

import torch

from utils.model import NeuralNet
from utils.nltk_utils import bag_of_words, tokenize
from utils.voice_utils import speak

from features.funcions import functions
from utils.context import get, update
from utils.chat import chat

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "./models/data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Jarvis"
def Process(sentence):
    og_sentence = sentence
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                res = random.choice(intent['responses'])
                for cmnd in intent['commands']:
                    try:
                        functions[cmnd]()
                        new_msg=[{"role": "user", "message": og_sentence}, {"role": "assistant", "message": res}]
                        update(history=get("history")+new_msg)
                        speak(res)
                    except:
                        speak(f"Failed to execute command {cmnd}")
    else:
        res = chat(og_sentence)
        speak(res)