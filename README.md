# AI Chat with Memory using Ollama (llama3.2)

This is a **Streamlit** web application that interacts with the `llama3.2` AI model via the `ollama` library. The app allows users to chat with an AI assistant, which has the ability to remember and respond to previous queries within a single session. The interface is designed for ease of use with real-time responses and a dynamic chat interface.

## Features

- **Interactive Chat**: Users can ask questions or provide information, and the AI responds based on the conversation history.
- **Memory Persistence**: The AI remembers previous messages within a session, maintaining context.
- **Real-Time Responses**: Responses from the AI are streamed as they are generated, providing an engaging experience.
- **User-Friendly Interface**: Designed with Streamlit for a clean, intuitive layout.
- **Custom Footer**: A footer crediting **Vishal Paswan** as the creator is displayed at the bottom of the app.

## Requirements

Before running the app, ensure you have the following Python libraries installed:

- `streamlit`
- `ollama`

You can install these dependencies using the following commands:

```bash
pip install streamlit
pip install ollama
