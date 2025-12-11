import streamlit as st
import spacy
from transformers import pipeline
import json
from nlp_processor import TextProcessor

# Page config
st.set_page_config(
    page_title="Smart Text Memory Booster",
    page_icon="🧠",
    layout="wide"
)

# Initialize session state
if 'processor' not in st.session_state:
    with st.spinner('Loading NLP models... This may take a moment on first run...'):
        st.session_state.processor = TextProcessor()

# Title and description
st.title("🧠 Smart Text Memory Booster")
st.markdown("""
Transform any paragraph into easy-to-remember memory cards, summaries, MCQs, and flashcards!
**Powered by AI and NLP**
""")

# Sidebar for options
st.sidebar.header("⚙️ Options")
chunk_size = st.sidebar.slider("Chunk Size (sentences)", 2, 10, 3)
num_mcqs = st.sidebar.slider("Number of MCQs", 3, 10, 5)
num_flashcards = st.sidebar.slider("Number of Flashcards", 3, 15, 8)

# Main input area
st.header("📝 Input Text")
input_text = st.text_area(
    "Paste your paragraph or text here:",
    height=200,
    placeholder="Enter any educational text, article, or notes that you want to convert into memory aids..."
)

# Process button
if st.button("🚀 Generate Memory Aids", type="primary"):
    if input_text.strip():
        with st.spinner('Processing your text... Please wait...'):
            try:
                # Process text
                chunks = st.session_state.processor.chunk_text(input_text, chunk_size)
                summary = st.session_state.processor.generate_summary(input_text)
                mcqs = st.session_state.processor.generate_mcqs(input_text, num_mcqs)
                flashcards = st.session_state.processor.generate_flashcards(input_text, num_flashcards)
                
                # Display results in tabs
                tab1, tab2, tab3, tab4 = st.tabs(["📊 Summary", "📚 Text Chunks", "✅ MCQs", "🎴 Flashcards"])
                
                with tab1:
                    st.subheader("Summary")
                    st.info(summary)
                    st.download_button(
                        "Download Summary",
                        summary,
                        file_name="summary.txt",
                        mime="text/plain"
                    )
                
                with tab2:
                    st.subheader(f"Text Chunks ({len(chunks)} chunks)")
                    for i, chunk in enumerate(chunks, 1):
                        with st.expander(f"Chunk {i}"):
                            st.write(chunk)
                    
                    chunks_text = "\n\n---\n\n".join([f"**Chunk {i}:**\n{chunk}" for i, chunk in enumerate(chunks, 1)])
                    st.download_button(
                        "Download Chunks",
                        chunks_text,
                        file_name="chunks.txt",
                        mime="text/plain"
                    )
                
                with tab3:
                    st.subheader(f"Multiple Choice Questions ({len(mcqs)})")
                    for i, mcq in enumerate(mcqs, 1):
                        st.markdown(f"**Q{i}. {mcq['question']}**")
                        for j, option in enumerate(mcq['options'], 1):
                            st.write(f"{chr(64+j)}. {option}")
                        with st.expander("Show Answer"):
                            st.success(f"✓ Correct Answer: {mcq['answer']}")
                        st.divider()
                    
                    mcqs_text = "\n\n".join([
                        f"Q{i}. {mcq['question']}\n" + 
                        "\n".join([f"{chr(64+j)}. {opt}" for j, opt in enumerate(mcq['options'], 1)]) +
                        f"\n\nAnswer: {mcq['answer']}"
                        for i, mcq in enumerate(mcqs, 1)
                    ])
                    st.download_button(
                        "Download MCQs",
                        mcqs_text,
                        file_name="mcqs.txt",
                        mime="text/plain"
                    )
                
                with tab4:
                    st.subheader(f"Flashcards ({len(flashcards)})")
                    cols = st.columns(2)
                    for i, card in enumerate(flashcards):
                        with cols[i % 2]:
                            with st.container():
                                st.markdown(f"**Card {i+1}**")
                                st.markdown(f"**Q:** {card['question']}")
                                with st.expander("Show Answer"):
                                    st.write(card['answer'])
                                st.divider()
                    
                    flashcards_text = "\n\n".join([
                        f"Card {i+1}:\nQ: {card['question']}\nA: {card['answer']}"
                        for i, card in enumerate(flashcards)
                    ])
                    st.download_button(
                        "Download Flashcards",
                        flashcards_text,
                        file_name="flashcards.txt",
                        mime="text/plain"
                    )
                
                st.success("✅ Memory aids generated successfully!")
                
            except Exception as e:
                st.error(f"Error processing text: {str(e)}")
                st.info("Try with a shorter or different text.")
    else:
        st.warning("Please enter some text to process!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Made with ❤️ using Transformers, spaCy, and Streamlit</p>
    <p>🧠 Smart Text Memory Booster | AI-Powered Learning Tool</p>
</div>
""", unsafe_allow_html=True)