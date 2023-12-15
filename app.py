import openai
from langchain.llms import OpenAI
from tts import text_to_speech

# Substitua 'your_api_key' pela sua chave API da OpenAI
api_key = 'your_api_key'

llm = OpenAI(openai_api_key=api_key)


def chatbot_response(prompt):

    full_prompt = [prompt]
    response = llm.generate(full_prompt)

    if response.generations:
        first_generation_list = response.generations[0]
        if first_generation_list:
            first_generation = first_generation_list[0]
            if first_generation and hasattr(first_generation, 'text'):
                return first_generation.text.strip()
    else:
        return "Desculpe, não consegui processar sua solicitação."


####################################################

# Frontend

import gradio as gr

def chat_interface(prompt):
    response = chatbot_response(prompt)
    audio_file = text_to_speech(response)
    return response, audio_file

interface = gr.Interface(
    fn=chat_interface,
    inputs=gr.Textbox(lines=2, placeholder="..."),
    outputs=[gr.Text(), gr.Audio()],
    title="Chatbot",
)

interface.launch()