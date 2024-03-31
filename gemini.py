# TODO(developer): Vertex AI SDK - uncomment below & run
# pip3 install --upgrade --user google-cloud-aiplatform
# gcloud auth application-default login

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
API_KEY = ''
genai.configure(api_key=API_KEY)

'''
safety_settings = {
    #HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
}
'''

def generate_text(project_id: str, location: str) -> str:
#https://cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-gemini-get-started
    # Load the model
    multimodal_model = genai.GenerativeModel("gemini-1.0-pro-vision")
    # Query the model
    response = multimodal_model.generate_content(
        [
            # Add an example image
            Part.from_uri(
                "gs://generativeai-downloads/images/scones.jpg", mime_type="image/jpeg"
            ),
            # Add an example query
            "what is shown in this image?",
        ]
    )
    #print(response)
    return response.text

def text_to_notes(transcript):
    multimodal_model = genai.GenerativeModel("gemini-1.0-pro")
    response = multimodal_model.generate_content(
        [transcript, "Format this professionally in markdown, with headings, bolded keywords, and bullet points"]
    )
    return response.text

def clean_up_text(transcript, format=None):
    multimodal_model = genai.GenerativeModel("gemini-1.0-pro")
    response = multimodal_model.generate_content(
        [transcript, "Transform this text so it is grammatically correct, without stutters and repeated words"]
    )
    
    if format == "True":
        response = multimodal_model.generate_content(
            [response.text, "While preserving the exact original text, format the following text with headers and paragraphs"
            ]
        )
    return response.text

def translate(transcript, language):
    multimodal_model = genai.GenerativeModel("gemini-1.0-pro")
    prompt = f"Translate this passage to {language}"
    response = multimodal_model.generate_content([transcript, prompt])
    return response.text

def find_keywords(transcript):
    multimodal_model = genai.GenerativeModel("gemini-1.0-pro")
    response = multimodal_model.generate_content(
        [transcript, "What are the top 5 important keywords of the text? What does the text say about them?"]
    )
    keywords_only = []
    keywords_only.append(response.text.split("1. **",1)[1].split(":**",1)[0])
    keywords_only.append(response.text.split("2. **",1)[1].split(":**",1)[0])
    keywords_only.append(response.text.split("3. **",1)[1].split(":**",1)[0])
    keywords_only.append(response.text.split("4. **",1)[1].split(":**",1)[0])
    keywords_only.append(response.text.split("5. **",1)[1].split(":**",1)[0])

    description_only = []
    #description_only.append(response.text.split(":**",1)[1].split("2. **",1)[0])
    #description_only.append(response.text.split(":**",1)[1].split("3. **",1)[0])
    #description_only.append(response.text.split(":**",1)[1].split("4. **",1)[0])
    #description_only.append(response.text.split(":**",1)[1].split("5. **",1)[0])
    return response.text, keywords_only

    
if __name__ == "__main__":
    
    project_id = "genaigensis2024"
    # Initialize Vertex AI
    vertexai.init(project=project_id, location="us-central1")
    #response = generate_text("genaigenesis2024", "us-central1")
    #print(response)
    
    #transcript = "Right? Because, because I want people to isolate, you know, jackets and shoes separately."
    transcript = open("transcript.txt", "r")
    #print(transcript.read())
    #generated_text = text_to_notes(transcript.read())
    #print(generated_text)
    
    cleaned_text = clean_up_text(transcript.read(), format="True")
    #print(cleaned_text)
    
    #translated_text = translate(transcribed_text, "French")
    #print(translated_text)
    
    flashcards, keywords_only = find_keywords(cleaned_text)
    
    
    
    
    