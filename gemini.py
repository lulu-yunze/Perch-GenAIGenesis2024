# TODO(developer): Vertex AI SDK - uncomment below & run
# pip3 install --upgrade --user google-cloud-aiplatform
# gcloud auth application-default login

import vertexai
from vertexai.generative_models import GenerativeModel, Part
from google.oauth2 import service_account

def generate_text(project_id: str, location: str) -> str:
#https://cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-gemini-get-started
    # Load the model
    multimodal_model = GenerativeModel("gemini-1.0-pro-vision")
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
    multimodal_model = GenerativeModel("gemini-1.0-pro")
    response = multimodal_model.generate_content(
        [transcript, "Format this professionally in markdown"]
    )
    return response.text

def clean_up_text(transcript):
    multimodal_model = GenerativeModel("gemini-1.0-pro")
    response = multimodal_model.generate_content(
        [transcript, "Transform this text so it is grammatically correct, without stutters and repeated words"]
    )
    return response.text  
    
    
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
    
    transcribed_text = clean_up_text(transcript.read())
    print(transcribed_text)