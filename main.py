import streamlit as st
import ollama

# Page Config
st.set_page_config(page_title="AI Chat - Context Aware", layout="wide")

# Initialize session state for conversation history
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Title
st.title("🧠 AI Chat with Context Awareness")

# Input box for user query
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message here:", placeholder="Ask anything...")
    submitted = st.form_submit_button("Send")

# Handle user input
if submitted and user_input.strip():
    # Append user input to the conversation history
    st.session_state.conversation_history.append({'role': 'user', 'content': user_input})

    # Call Ollama API with the conversation history
    stream = ollama.chat(
        model='llama3.2',
        messages=st.session_state.conversation_history,
        stream=True,
    )

    # Collect the AI's response
    response_chunks = []
    with st.spinner("AI is thinking..."):
        for chunk in stream:
            content = chunk.get('message', {}).get('content', '')
            if content:
                response_chunks.append(content)
    
    # Combine response chunks into a full response
    full_response = ''.join(response_chunks)
    
    # Append the AI's response to the conversation history
    st.session_state.conversation_history.append({'role': 'assistant', 'content': full_response})

    # Display the response
    st.success("AI Response:")
    st.write(full_response)

# Display the chat history
st.subheader("Conversation History")
for message in st.session_state.conversation_history:
    if message['role'] == 'user':
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**AI:** {message['content']}")

# Add a button to reset the chat
if st.button("Reset Chat"):
    st.session_state.conversation_history = []
    st.success("Chat reset successfully!")
