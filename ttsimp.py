from openai import OpenAI

client = OpenAI()

def convert_text_to_speech(text, output_file, speed=1):
    response = client.audio.speech.create(    
        model="tts-1",
        voice="alloy",
        input=text,
        speed=speed)
    response.stream_to_file(output_file)

# Example usage
story_title = "Ruby's Tale: The Heart of Honesty in the Enchanted Forest"
with open("Ruby The Rabbit/story", "r") as file:
    text = file.read()
intro_text = f"""
Welcome to Sleep Soundly, AI generated stories to fall asleep to. 

Tonight's Story: {story_title}
"""
convert_text_to_speech(intro_text, "Ruby The Rabbit/intro.mp3")

for i in range(6):
    output_file = f"Ruby The Rabbit/Part {i+1}.mp3"
    text = open(f"Ruby The Rabbit/part{i+1}.txt", "r").read()
    convert_text_to_speech(text, output_file)
