# 🧠 Smart Text Memory Booster

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)](https://streamlit.io/)
[![Transformers](https://img.shields.io/badge/Transformers-4.35%2B-yellow)](https://huggingface.co/transformers/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

An AI-powered NLP application that transforms any paragraph into easy-to-remember **memory cards**, **summaries**, **MCQs**, and **flashcards**. Perfect for students, educators, and anyone looking to enhance their learning experience!

## ✨ Features

- 📝 **Text Chunking**: Automatically breaks down large paragraphs into digestible chunks
- 📊 **Smart Summarization**: Generates concise summaries using BART transformer model
- ✅ **MCQ Generation**: Creates multiple-choice questions with options and answers
- 🎴 **Flashcards**: Generates Q&A flashcards for active recall practice
- 💾 **Export Options**: Download all generated content as text files
- 🎨 **Clean UI**: Beautiful Streamlit interface with tabs and interactive elements

## 🚀 Tech Stack

- **Python**: Core programming language
- **Transformers**: Hugging Face models for summarization and QA
  - `facebook/bart-large-cnn` for summarization
  - `distilbert-base-cased-distilled-squad` for question answering
- **spaCy**: NLP processing for text chunking and entity extraction
- **Streamlit**: Interactive web UI framework

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/syedabersabil/smart-text-memory-booster.git
cd smart-text-memory-booster
```

2. **Create virtual environment (recommended)**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download spaCy model**
```bash
python -m spacy download en_core_web_sm
```

## 🎯 Usage

### Local Development

1. **Run the Streamlit app**
```bash
streamlit run app.py
```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Enter your text** in the input area

4. **Adjust settings** in the sidebar:
   - Chunk size (2-10 sentences)
   - Number of MCQs (3-10)
   - Number of flashcards (3-15)

5. **Click "Generate Memory Aids"** and explore the tabs:
   - 📊 Summary
   - 📚 Text Chunks
   - ✅ MCQs
   - 🎴 Flashcards

## 🌐 Deployment

### Deploy on Streamlit Cloud (Free)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Connect your GitHub account
4. Select your repository and branch
5. Set main file path: `app.py`
6. Click "Deploy"!

### Deploy on Hugging Face Spaces

1. Create a new Space at [huggingface.co/spaces](https://huggingface.co/spaces)
2. Choose "Streamlit" as SDK
3. Upload your files or connect GitHub repo
4. Add `requirements.txt` and set Python version
5. Your app will be live!

## 📁 Project Structure

```
smart-text-memory-booster/
│
├── app.py                 # Main Streamlit application
├── nlp_processor.py       # Core NLP processing logic
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Git ignore rules
```

## 🔧 Configuration

You can modify the following parameters in the sidebar:

- **Chunk Size**: Number of sentences per chunk (default: 3)
- **Number of MCQs**: How many questions to generate (default: 5)
- **Number of Flashcards**: How many flashcards to create (default: 8)

## 🎓 Use Cases

- **Students**: Convert lecture notes into study materials
- **Educators**: Create quick quizzes and study aids
- **Content Creators**: Generate summaries and key points
- **Researchers**: Break down complex papers into chunks
- **Language Learners**: Create vocabulary flashcards

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for transformer models
- [spaCy](https://spacy.io/) for NLP capabilities
- [Streamlit](https://streamlit.io/) for the awesome UI framework

## 📧 Contact

**Syed Aber Sabil**
- GitHub: [@syedabersabil](https://github.com/syedabersabil)
- Project Link: [https://github.com/syedabersabil/smart-text-memory-booster](https://github.com/syedabersabil/smart-text-memory-booster)

## 🐛 Known Issues

- First run may take time to download models
- Very long texts (>1000 words) may need chunking before processing
- MCQ generation quality depends on text structure

## 🔮 Future Enhancements

- [ ] Support for multiple languages
- [ ] PDF and document upload support
- [ ] Better MCQ generation with more context
- [ ] Export to Anki flashcard format
- [ ] Save and load previous sessions
- [ ] Hindi/Hinglish language support
- [ ] Integration with popular note-taking apps

---

⭐ If you find this project helpful, please give it a star!
