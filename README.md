
# PRISM: Personalized Resource for Intelligent Study and Management

## Overview

PRISM is an AI-driven educational platform designed to enhance the learning experience by providing tools for lecture transcription, intelligent content management, and exam preparation. The system integrates modern AI technologies to assist students and educators in organizing, understanding, and reviewing educational materials efficiently.

## Objectives

1. **Lecture Transcription**:
   - Automatically transcribe lecture recordings into text.
   - Provide accurate and organized transcripts for easy review.
  
2. **Content Analysis and Management**:
   - Use AI to analyze lecture content and organize it effectively.
   - Provide features for tagging, searching, and summarizing content.
  
3. **Study Assistance**:
   - Offer AI-driven assistance to clarify doubts and answer questions based on provided materials.
   - Predict potential exam questions and generate practice exams.

4. **User Interface and Experience**:
   - Develop an intuitive and user-friendly interface.
   - Ensure seamless interaction between the user and the AI components.

## Technologies Used

- **Frontend**: React.js
- **Backend**: Python
- **Speech-to-Text**: OpenAI Whisper
- **NLP and AI**: 
- **Database**: 
- **Authentication**: 
- **Deployment**: Vercel (Frontend and Backend), AWS for AI models
- **Version Control**: Git and GitHub

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/prism.git
cd prism
```

### 2. Install Dependencies

#### Frontend (React)

```bash
cd frontend
npm install
```

#### Backend (Python)

```bash
cd backend
*/setup virtual environment 
download dependencies 
flask
whisper
torch
*/
python3 -m venv venv
source venv/bin/activate 
*/ windows
.\venv/Scripts/activate\
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
source venv/bin/activate
*/
pip install flask whisper openai
pip install torch


```

### 3. Configure Environment Variables

Create a `.env` file in the backend directory to store API keys and other sensitive information.

```plaintext
DATABASE_URL=your-database-connection-string
NEXTAUTH_URL=your-authentication-url
```

### 4. Run the Development Servers

#### Frontend

```bash
npm run dev
```

#### Backend

```bash
pata nahi abhi
```

### 5. Deploy the Application

Deploy both frontend and backend using Vercel or any other preferred platform.

## Features and Implementation

### 1. Lecture Transcription

- **Objective**: Convert lecture audio recordings into text.
- **Process**:
  - Users upload audio files via the frontend.
  - The backend API receives the files and processes them using the Google Cloud Speech-to-Text API.
  - The transcribed text is returned to the user and stored in the database for future reference.

### 2. Content Analysis and Management

- **Objective**: Organize and analyze transcribed content.
- **Process**:
  - The AI model (using Hugging Face Transformers) processes the transcripts.
  - Tags and summaries are generated to facilitate easy navigation.
  - Users can search and filter content based on tags or keywords.

### 3. Study Assistance

- **Objective**: Provide intelligent study aids based on the transcribed and analyzed content.
- **Process**:
  - AI models are fine-tuned on the provided datasets (lecture transcripts, textbooks).
  - Users can input questions or topics, and the AI provides relevant explanations or answers.
  - The system predicts potential exam questions and allows users to generate practice exams.

### 4. User Interface and Experience

- **Objective**: Ensure a smooth and engaging user experience.
- **Process**:
  - Implement a responsive UI using React.js with a focus on ease of use.
  - Utilize Material-UI or Ant Design for consistent and professional UI components.
  - Manage state effectively using Redux or Context API.

## Future Enhancements

- **Real-time Transcription**: Implement live transcription during lectures.
- **Advanced Analytics**: Introduce deeper content analysis, such as sentiment analysis or keyword extraction.
- **Mobile Application**: Develop a mobile app version of PRISM for on-the-go access.

## Contributing

Contributions are welcome! (depends !!)

## License

iska nahi pata
