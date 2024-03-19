import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyD6Lu4yVdthnv6ekXka5iW9H3Sd970g_Cg")
# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro-001",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

def main():
    st.title("Business Insights Generator")
    
    # Create input fields
    initial_prompt = st.text_area("Enter the prompt here:", '''Give me business insights for the following conversation \n''')
    num_words = st.number_input("Enter the number of words:", value=25)
    num_bullet_points = st.number_input("Enter the number of bullet points:", value=3)
    additional_text = st.text_area("Enter Conversation text:", '''Interviewer: Hello, thank you for joining us today. We're excited to get your feedback on our
app.
Interviewee: Hi, happy to be here. Overall, the app's been good.
Interviewer: That's great to hear! Could you tell us more about your experience using the
app?
Interviewee: Sure. It's user-friendly, but more personalized features would enhance it.
Interviewer: Personalization noted. What specific features would you like to see for a more
fulfilling experience?
Interviewee: Customizable notifications and tailored content based on my preferences would
be fantastic.
Interviewer: Noted. Now, are there any areas you feel could use improvement within the
app?
Interviewee: Occasionally, the app lags during peak hours. Improving its speed would be
beneficial.
Interviewer: Thank you for sharing that. We'll look into optimizing the app's performance. Any
other areas?
Interviewee: The search function could be more accurate. It sometimes misses relevant
results.
Interviewer: Understood. We'll work on refining the search algorithm. Any final thoughts or
suggestions?
Interviewee: Overall, I'm satisfied. Just a few tweaks would make the app even better.
Interviewer: We appreciate your feedback. It's invaluable for us to enhance the app. Thank
you for your time today.''')
    
    combined_prompt = initial_prompt + "in" + str(num_words) + "words" + "in" +str(num_bullet_points) + "The conversation is:" + additional_text

    submit_button = st.button("Generate Insights")

    # If submit button is clicked
    if submit_button:
        # Generate response
        response = generate_insights(combined_prompt)
        
        # Display the response
        st.write("Generated Insights:")
        st.write(response)

def generate_insights(prompt):
    # Split prompt into parts
    prompt_parts = prompt.split("\n")
    
    # Generate content
    response = model.generate_content(prompt_parts)
    
    return response.text

if __name__ == "__main__":
    main()
