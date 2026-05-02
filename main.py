import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit page config
st.set_page_config(page_title="ProjectPilot AI", page_icon="🚀")

# App title
st.title("🚀 ProjectPilot AI")
st.subheader("Enter your project idea and get an AI-powered project blueprint")

# User input
project_idea = st.text_input("Enter your project idea:")

# Generate button
if st.button("Generate Project Blueprint"):

    if project_idea.strip() == "":
        st.warning("Please enter your project idea.")
    else:
        with st.spinner("Generating AI project blueprint..."):

            prompt = f"""
            Create a beginner-friendly academic project blueprint for: {project_idea}

            Include:
            1. Project Title
            2. Objective
            3. Required Components
            4. Estimated Budget in INR
            5. Step-by-Step Working
            6. Future Scope
            7. Difficulty Level

            Make it practical, clear, and student-friendly.
            """

            try:
                response = model.generate_content(prompt)
                output = response.text

            except Exception:
                output = f"""
# Project Title:
Smart {project_idea.title()} System

# Objective:
This project helps solve problems related to {project_idea} using automation.

# Required Components:
- Arduino / ESP32
- Sensors
- Power Supply
- Wires
- Display Module

# Estimated Budget:
₹1500 - ₹5000

# Step-by-Step Working:
1. User gives input
2. Sensors collect data
3. Controller processes
4. System responds
5. Output shown

# Future Scope:
- AI Features
- IoT
- Mobile App

# Difficulty Level:
Beginner
"""

            st.success("Project Blueprint Generated Successfully!")
            st.write(output)      