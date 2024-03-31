# TODO(developer): Vertex AI SDK - uncomment below & run
# pip3 install --upgrade --user google-cloud-aiplatform
# gcloud auth application-default login

#Use this file if you have google cloud console installed and logged in
import vertexai
import json
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

def text_to_notes(transcript):
    multimodal_model = GenerativeModel("gemini-1.0-pro")
    response = multimodal_model.generate_content(
        [transcript, "Format this professionally in markdown, with headings, bolded keywords, and bullet points"]
    )
    html_text = markdown.markdown(response.text)
    return html_text

def clean_up_text(transcript):
    multimodal_model = GenerativeModel("gemini-1.0-pro")
    response = multimodal_model.generate_content(
        [transcript, "Transform this text so it is grammatically correct, without stutters and repeated words"]
    )
    return response.text

def translate(transcript, language):
    multimodal_model = GenerativeModel("gemini-1.0-pro")
    prompt = f"Translate this passage to {language}"
    response = multimodal_model.generate_content([transcript, prompt])
    
    
    return response.text

def find_keywords(transcript):
    #Returns: 
    #response.text: keywords and descriptions together
    #keywords_only: only the keywords
    #descriptions_only: only the descriptions
    
    #Delete generation_config if it happens to bug out with API version...
    #generation_config = GenerationConfig(
    #    temperature=0,          # higher = more creative (default 0.0)
    #    top_p=0.4,                # higher = more random responses, response drawn from more possible next tokens (default 0.95)
    #    top_k=30,                 # higher = more random responses, sample from more possible next tokens (default 40)
    #    candidate_count=1,
    #    max_output_tokens=1024,   # default = 2048
    #)   
    multimodal_model = GenerativeModel("gemini-1.0-pro")
    response = multimodal_model.generate_content(
        [transcript, "What are the top 5 important keywords of the text? Give it a header \"Top keywords\" and format them as \"1. **Word:** description\""])

    #Uncomment if keywords_only and descriptions_only throw and error (probably because gemini generated in a different format)
    #keywords = multimodal_model.generate_content([response.text, "List the keywords in this text"])
    #descriptions = multimodal_model.generate_content([response.text, "List the descriptions in this text"])
    
    try: 
        #Get only the keywords (front of the flashcards)
        
        print(response.text)
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
        
        
    except:
        #new prompt Python string format
        shortened = response.text
        keywords_only = shortened.split("[", 1)[1].split("]", 1)[0].split(", ")
        for i, string in enumerate(keywords_only):
            print(string)
            keywords_only[i] = string.split("\"", 1)[1].split("\"", 1)[0]

        shortened = shortened.split("]", 1)[1]
        descriptions_only = shortened.split("[", 1)[1].split("]", 1)[0].split(", ")
        for i, string in enumerate(descriptions_only):
            print(string)
            descriptions_only[i] = string.split("\"", 1)[1].split("\"", 1)[0]

    return response.text, keywords_only, descriptions_only

    
if __name__ == "__main__":
    
    project_id = "genaigensis2024"
    # Initialize Vertex AI
    vertexai.init(project=project_id, location="us-central1")
    #response = generate_text("genaigenesis2024", "us-central1")
    #print(response)
    transcript = open("Transcript.txt", "r")
    file = transcript.read()
    #print(transcript.read())
    #notes_html = text_to_notes(file)
    #print("\n")
    #print("\n")
    #print(notes_html)
    
    cleaned_text = clean_up_text(file)
    #print("\n")
    #print("\n")
    #print(cleaned_text)
    
    #translated_text = translate(cleaned_text, "French")
    #print("\n")
    #print("\n")
    #print(translated_text)
    
    flashcards, keywords_only, descriptions_only = find_keywords(cleaned_text)
    
    print("\n")
    print("\n")
    #print(flashcards)
    
    print("\n")
    print("\n")
    print(keywords_only)

    print("\n")
    print("\n")
    print(descriptions_only)

    
    
    
    