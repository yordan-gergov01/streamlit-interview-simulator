# AI Mock Interview Chatbot

A Streamlit web app that simulates a job interview using OpenAI's GPT models. Users provide their personal details, target role, and company, then go through a short AI-driven interview and receive automated feedback with a score at the end.

## Features

- 📝 **Personal setup form** - collects name, experience, skills, seniority level, position, and target company.
- 💬 **Interactive interview chat** - an AI acting as an HR executive asks tailored questions based on the candidate's profile.
- 🔢 **Limited conversation turns** - the interview automatically wraps up after 5 user responses.
- ⭐ **Automated feedback** - a separate AI call reviews the full conversation and returns a score (1–10) with written feedback.
- 🔄 **Restart option** - reset the session and start a new interview from scratch.

## Tech Stack

- [Streamlit](https://streamlit.io/) — web app framework
- [OpenAI API](https://platform.openai.com/) (`gpt-4o-mini` for the interview, `gpt-4o` for feedback)
- [streamlit-js-eval](https://pypi.org/project/streamlit-js-eval/) — used to trigger a page reload on restart

## Demo Flow

1. Fill in your personal information and target role/company.
2. Click **Start Interview**.
3. Respond to the AI interviewer's questions (up to 5 exchanges).
4. Click **Get Feedback** once the interview is complete.
5. Review your score and feedback.
6. Click **Restart Interview** to try again.


### Configuration

Create a `.streamlit/secrets.toml` file in the project root and add your OpenAI API key:

```toml
OPENAI_API_KEY = "your-openai-api-key-here"
```

> ⚠️ **Never commit your `secrets.toml` file or API key to version control.** Add `.streamlit/secrets.toml` to your `.gitignore`.

### Running the App

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

## Project Structure

```
.
├── app.py                 # Main Streamlit application
├── .streamlit/
│   └── secrets.toml        # API keys (not committed)
└── README.md
```

## How It Works

- **Session state** is used throughout to persist form inputs, chat history, and interview progress across Streamlit reruns.
- The **system prompt** for the interview is dynamically built from the candidate's name, experience, skills, level, position, and company.
- After 5 user messages, the interview is marked complete and the **Get Feedback** button appears.
- The full conversation history is sent to a second GPT call with a dedicated feedback system prompt, which returns a score and written evaluation.

## License

This project is open source and available under the [MIT License](LICENSE).
