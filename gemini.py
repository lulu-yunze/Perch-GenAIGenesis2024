# TODO(developer): Vertex AI SDK - uncomment below & run
# pip3 install --upgrade --user google-cloud-aiplatform
# gcloud auth application-default login

#Run this file if you have the API key
import vertexai
import google.generativeai as genai
from vertexai.generative_models import (
    GenerationConfig,
    GenerativeModel,
    HarmCategory,
    HarmBlockThreshold,
    Image,
    Part,
)
import markdown

API_KEY = '' #Add API key here
genai.configure(api_key=API_KEY)

def text_to_notes(transcript):
    multimodal_model = genai.GenerativeModel("gemini-1.0-pro")
    response = multimodal_model.generate_content(
        [transcript, "Format this professionally in markdown, with headings, bolded keywords, and bullet points"]
    )
    html_text = markdown.markdown(response.text)
    return html_text

def clean_up_text(transcript):
    multimodal_model = genai.GenerativeModel("gemini-1.0-pro")
    response = multimodal_model.generate_content(
        [transcript, "Transform this text so it is grammatically correct, without stutters and repeated words"]
    )
    return response.text

def translate(transcript, language):
    multimodal_model = genai.GenerativeModel("gemini-1.0-pro")
    prompt = f"Translate this passage to {language}"
    response = multimodal_model.generate_content([transcript, prompt])
    
    
    return response.text

def find_keywords(transcript):
    #Returns: 
    #response.text: keywords and descriptions together
    #keywords_only: only the keywords
    #descriptions_only: only the descriptions
    
    multimodal_model = genai.GenerativeModel("gemini-1.0-pro")
    response = multimodal_model.generate_content(
        [transcript, "What are the top 5 important keywords of the text? What does the text say about them?"]
    )

    #Uncomment if keywords_only and descriptions_only throw and error (probably because gemini generated in a different format)
    #keywords = multimodal_model.generate_content([response.text, "List the keywords in this text"])
    #descriptions = multimodal_model.generate_content([response.text, "List the descriptions in this text"])
    
    #Get only the keywords (front of the flashcards)
    keywords_only = []
    keywords_only.append(response.text.split("1. **",1)[1].split(":**",1)[0])
    keywords_only.append(response.text.split("2. **",1)[1].split(":**",1)[0])
    keywords_only.append(response.text.split("3. **",1)[1].split(":**",1)[0])
    keywords_only.append(response.text.split("4. **",1)[1].split(":**",1)[0])
    keywords_only.append(response.text.split("5. **",1)[1].split(":**",1)[0])

    #Get only the descriptions (back of the flashcards)
    descriptions_only = []
    shortened = response.text.split(":**",1)[1]
    descriptions_only.append(shortened.split(":** ",1)[1].split("\n2.",1)[0])
    shortened = shortened.split(":** ",1)[1]
    descriptions_only.append(shortened.split(":** ",1)[1].split("\n3.",1)[0])
    shortened = shortened.split(":** ",1)[1]
    descriptions_only.append(shortened.split(":** ",1)[1].split("\n4.",1)[0])
    shortened = shortened.split(":** ",1)[1]
    descriptions_only.append(shortened.split(":** ",1)[1].split("\n5.",1)[0])
    shortened = shortened.split(":** ",1)[1]
    descriptions_only.append(shortened.split(":** ",1)[1])
    
    return response.text, keywords_only, descriptions_only

    
if __name__ == "__main__":
    
    project_id = "genaigensis2024"
    # Initialize Vertex AI
    vertexai.init(project=project_id, location="us-central1")
    #response = generate_text("genaigenesis2024", "us-central1")
    #print(response)
    
    #transcript = "Right? Because, because I want people to isolate, you know, jackets and shoes separately."
    transcript = open("Transcript.txt", "r")
    file = transcript.read()
    #print(transcript.read())
    notes_html = text_to_notes(file)
    print(notes_html)
    
    cleaned_text = clean_up_text(file)
    print(cleaned_text)
    
    #translated_text = translate(transcribed_text, "French")
    #print(translated_text)
    
    flashcards, keywords_only = find_keywords(cleaned_text)
    print(keywords_only)
    
    
    
    
    
    