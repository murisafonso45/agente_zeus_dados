import streamlit as st
from groq import Groq
from dotenv import loadenv
import os 

loadenv()

st.title("AGENTE DA MÚSICA")

# Cole a sua chave diretamente como texto entre aspas:
client = Groq(api_key)

pergunta = st.text_input("Digite sua pergunta...")

if pergunta:
    resposta = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "Você é um Profissional em música, sabe sobre todos os estilos possíveis e ama todos."
            },
            {
                "role": "user",
                "content": pergunta
            }
        ]
    )
    
    st.write(resposta.choices[0].message.content)