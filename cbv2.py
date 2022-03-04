import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer 
import json

def get_text():
    input_text = st.text_input("You: ","So, what's in your mind")
    return input_text 

data = json.loads(open(r'G:\Chatbot\data_tolokers.json','r').read())#change path accordingly
data2 = json.loads(open(r'C:\Users\HUSN ARA\Chatbot\sw.json','r').read())#change path accordingly

tra = []
for k, row in enumerate(data):
    #print(k)
    tra.append(row['dialog'][0]['text'])
for k, row in enumerate(data2):
    #print(k)
    tra.append(row['dialog'][0]['text'])
    
    

st.sidebar.title("Chat Bot")
st.title("""
Chat Bot "Talking Bot"  
Chat Bot is an NLP conversational chatterbot. Refresh the Talking Bot by clicking the "Refresh bot" button. 
""")


bot = ChatBot(name = 'PyBot', read_only = False,preprocessors=['chatterbot.preprocessors.clean_whitespace','chatterbot.preprocessors.convert_to_ascii','chatterbot.preprocessors.unescape_html'], logic_adapters = ['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.BestMatch'])
#corpus_trainer = ChatterBotCorpusTrainer(bot) 
#corpus_trainer.train('chatterbot.corpus.english') 
#return bot


ind = 1
if st.sidebar.button('Refresh Bot'):
    #do something
    #bot = ChatBot(name = 'PyBot', read_only = False,preprocessors=['chatterbot.preprocessors.clean_whitespace','chatterbot.preprocessors.convert_to_ascii','chatterbot.preprocessors.unescape_html'], logic_adapters = ['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.BestMatch'])
    corpus_trainer = ChatterBotCorpusTrainer(bot) 
    corpus_trainer.train('chatterbot.corpos.english') 
    trainer2 = ListTrainer(bot) 
    trainer2.train(tra)
    st.title("Talking Bot is ready to talk to you")
    ind = ind +1
        
user_input = get_text()


if True:
    st.text_area("Bot:", value=bot.get_response(user_input), height=200, max_chars=None, key=None)
else:
    st.text_area("Bot:", value="Please start the bot by clicking sidebar button", height=200, max_chars=None, key=None)