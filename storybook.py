import os
import streamlit as st
from openai import OpenAI

my_secret = os.environ['OPENAI_API_KEY']
client = OpenAI(api_key=my_secret)

#Story prompt generator method

def story_gen(prompt):
  system_prompt = """
You are a world renowned 50 years experience children storyteller.
You will be given a concept to generate a story suitable for ages 5-7 years old.
"""

  response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
        {"role":"system",
         "content":system_prompt},
        {"role":"user",
         "content":prompt}
    ],
    temperature=1.3,
    max_tokens=1000
  )
  return response.choices[0].message.content

#Cover prompt generator method
def cover_gen(prompt):
  system_prompt = """
You will be given a children story book.
Generate a prompt for cove art that is suitable and shows themes.
The prompt will be sent to dell-e-2
"""

  response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
        {"role":"system",
         "content":system_prompt},
        {"role":"user",
         "content":prompt}
    ],
    temperature=1.3,
    max_tokens=1000
  )
  return response.choices[0].message.content

#Image generator method
def image_gen(prompt):
  response = client.images.generate(
      model = "dall-e-2",
      prompt = prompt,
      size = "1024x1024",
      n = 1,
  )
  return response.data[0].url
  
st.title("🌟 Magic Storybook Generator 🌟")
st.divider()

prompt = st.text_area("Enter your story concept:")

if st.button("Generate Storybook"):
  story = story_gen(prompt)
  cover = cover_gen(story)
  image = image_gen(cover)

  st.balloons()
  st.image(image)
  st.write(story)