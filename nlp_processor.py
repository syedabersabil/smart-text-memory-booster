import spacy
from transformers import pipeline
import re
import random

class TextProcessor:
    def __init__(self):
        """Initialize NLP models and pipelines"""
        try:
            # Load spaCy model
            try:
                self.nlp = spacy.load("en_core_web_sm")
            except OSError:
                print("Downloading spaCy model...")
                import os
                os.system("python -m spacy download en_core_web_sm")
                self.nlp = spacy.load("en_core_web_sm")
            
            # Initialize Hugging Face pipelines
            self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
            self.qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
            
        except Exception as e:
            print(f"Error initializing models: {e}")
            raise
    
    def chunk_text(self, text, chunk_size=3):
        """Chunk text into smaller segments based on sentences"""
        doc = self.nlp(text)
        sentences = [sent.text.strip() for sent in doc.sents]
        
        chunks = []
        for i in range(0, len(sentences), chunk_size):
            chunk = ' '.join(sentences[i:i+chunk_size])
            if chunk:
                chunks.append(chunk)
        
        return chunks if chunks else [text]
    
    def generate_summary(self, text, max_length=130, min_length=30):
        """Generate a concise summary of the text"""
        try:
            # Limit input length for summarization
            max_input_length = 1024
            if len(text.split()) > max_input_length:
                text = ' '.join(text.split()[:max_input_length])
            
            summary = self.summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
            return summary[0]['summary_text']
        except Exception as e:
            return f"Summary generation failed. Try with shorter text. Error: {str(e)}"
    
    def extract_key_phrases(self, text, num_phrases=5):
        """Extract important noun phrases from text"""
        doc = self.nlp(text)
        
        # Extract noun chunks and named entities
        noun_phrases = [chunk.text for chunk in doc.noun_chunks]
        named_entities = [ent.text for ent in doc.ents]
        
        # Combine and deduplicate
        key_phrases = list(set(noun_phrases + named_entities))
        
        # Filter out very short phrases
        key_phrases = [phrase for phrase in key_phrases if len(phrase.split()) >= 2]
        
        return key_phrases[:num_phrases] if key_phrases else ["concept", "topic", "subject"]
    
    def generate_mcqs(self, text, num_questions=5):
        """Generate multiple choice questions from text"""
        mcqs = []
        chunks = self.chunk_text(text, chunk_size=2)
        
        for i, chunk in enumerate(chunks[:num_questions]):
            try:
                # Extract key information
                doc = self.nlp(chunk)
                key_phrases = self.extract_key_phrases(chunk, num_phrases=3)
                
                if not key_phrases:
                    continue
                
                # Generate question based on key phrase
                answer = key_phrases[0]
                question_templates = [
                    f"What is {answer}?",
                    f"Which concept relates to {answer}?",
                    f"What describes {answer}?",
                    f"What is the significance of {answer}?",
                ]
                
                question = random.choice(question_templates)
                
                # Generate distractors (wrong options)
                other_phrases = [p for p in key_phrases[1:] if p != answer]
                distractors = other_phrases[:2] if len(other_phrases) >= 2 else ["Alternative concept", "Different topic"]
                
                # Create options
                options = [answer] + distractors + ["None of the above"]
                random.shuffle(options)
                
                # Find correct answer letter
                answer_index = options.index(answer)
                answer_letter = chr(65 + answer_index)  # A, B, C, D
                
                mcqs.append({
                    'question': question,
                    'options': options[:4],  # Limit to 4 options
                    'answer': f"{answer_letter}. {answer}"
                })
                
            except Exception as e:
                continue
        
        # If we couldn't generate enough, create generic ones
        while len(mcqs) < min(num_questions, 3):
            mcqs.append({
                'question': f"What is the main idea discussed in the text?",
                'options': ["Concept A", "Concept B", "Concept C", "Concept D"],
                'answer': "A. Concept A"
            })
        
        return mcqs[:num_questions]
    
    def generate_flashcards(self, text, num_cards=8):
        """Generate question-answer flashcards"""
        flashcards = []
        chunks = self.chunk_text(text, chunk_size=2)
        
        for i, chunk in enumerate(chunks[:num_cards]):
            try:
                # Extract key concepts
                doc = self.nlp(chunk)
                key_phrases = self.extract_key_phrases(chunk, num_phrases=2)
                
                if not key_phrases:
                    continue
                
                # Generate Q&A pairs
                concept = key_phrases[0]
                
                question_templates = [
                    f"What is {concept}?",
                    f"Explain {concept}",
                    f"Define {concept}",
                    f"What do you know about {concept}?",
                ]
                
                question = random.choice(question_templates)
                answer = chunk[:200]  # Use chunk as answer, limited length
                
                flashcards.append({
                    'question': question,
                    'answer': answer
                })
                
            except Exception as e:
                continue
        
        # Generate summary-based flashcard if we need more
        if len(flashcards) < num_cards:
            summary = self.generate_summary(text)
            flashcards.append({
                'question': "What is the main summary of this text?",
                'answer': summary
            })
        
        return flashcards[:num_cards]
