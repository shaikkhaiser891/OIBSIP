# 🎙️ Python Voice Assistant

A Python-based **Voice Assistant** that listens to spoken commands, understands user requests, and responds using text-to-speech. The project starts with beginner-friendly voice recognition features and can be extended with NLP, weather APIs, email, reminders, and general knowledge capabilities.

---

## 📌 Project Overview

The Voice Assistant captures commands through a microphone, converts speech into text, processes the command, and provides a spoken response.

### Basic Workflow

```text
User speaks
     ↓
Microphone
     ↓
Speech Recognition
     ↓
Command Processing
     ↓
Action
     ↓
Text-to-Speech
     ↓
Assistant speaks
```

---

## 🎯 Objectives

* Capture voice input using a microphone.
* Convert spoken commands into text.
* Respond to basic commands.
* Tell the current date and time.
* Search the web using voice commands.
* Provide spoken feedback using text-to-speech.
* Handle speech recognition errors gracefully.
* Extend the assistant with APIs and NLP features.

---

## 🛠️ Technologies Used

### Beginner Tier

* **Python**
* **SpeechRecognition**
* **PyAudio**
* **pyttsx3**
* **datetime**
* **webbrowser**

### Advanced Tier

* **NLTK** or **Transformers**
* **OpenWeatherMap API**
* **smtplib**
* **Requests**
* Python's **threading/time** functionality
* Local knowledge base or QA API

---

## ✨ Features

### Beginner Features

* [ ] Capture voice input using a microphone
* [ ] Respond to "Hello" with a predefined greeting
* [ ] Tell the current time
* [ ] Tell the current date
* [ ] Search the web using a spoken topic
* [ ] Convert speech to text
* [ ] Convert responses to speech
* [ ] Handle commands that are not understood
* [ ] Exit the assistant using a voice command

### Advanced Features

* [ ] Natural language intent recognition
* [ ] Send emails using voice commands
* [ ] Set timed reminders
* [ ] Audible reminder alerts
* [ ] Fetch live weather information
* [ ] Answer general knowledge questions
* [ ] Add custom commands
* [ ] Configuration file support
* [ ] Privacy documentation

---

## 📂 Project Structure

```text
voice-assistant/
│
├── voice_assistant.py
├── requirements.txt
├── config.json
└── README.md
```

For a larger advanced implementation:

```text
voice-assistant/
│
├── main.py
├── speech.py
├── commands.py
├── weather.py
├── email_service.py
├── reminders.py
├── config.json
├── requirements.txt
└── README.md
```

---

## 💻 Requirements

Before running the project, make sure you have:

* Python 3.9 or later
* A working microphone
* Speakers or headphones
* Internet connection for online speech recognition and web searches
* Windows, Linux, or macOS

Check your Python installation:

```bash
python --version
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/voice-assistant.git
```

Move into the project directory:

```bash
cd voice-assistant
```

### 2. Install dependencies

```bash
pip install SpeechRecognition pyttsx3 PyAudio
```

Or, if a `requirements.txt` file is provided:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Run the Python program:

```bash
python voice_assistant.py
```

You should hear:

```text
Voice assistant started.
```

The assistant will then wait for your voice command.

---

## 🗣️ Example Commands

### Greeting

```text
You: Hello
Assistant: Hello! How can I help you?
```

### Time

```text
You: What is the time?
Assistant: The current time is 04:30 PM.
```

### Date

```text
You: What is today's date?
Assistant: Today is Sunday, August 16, 2026.
```

### Web Search

```text
You: Search Python programming
Assistant: Searching the web for Python programming.
```

The assistant will open the browser and perform the search.

### Exit

```text
You: Exit
Assistant: Goodbye! Have a great day.
```

---

# 🚀 Advanced Features

## 🧠 Natural Language Understanding

The advanced version can understand different ways of expressing the same intent.

For example:

```text
"What time is it?"
"Can you tell me the current time?"
"Could you tell me what time it is?"
```

All three commands can be interpreted as the **time intent**.

NLP libraries such as `nltk` or `transformers` can be used to improve intent recognition.

---

## 🌦️ Weather Information

The assistant can retrieve live weather information using the **OpenWeatherMap API**.

Example:

```text
You: What is the weather in Kurnool?
Assistant: The current temperature is 30°C with clear skies.
```

An API key should be stored securely and should **not** be uploaded to GitHub.

Example configuration:

```json
{
    "weather_api_key": "YOUR_API_KEY"
}
```

---

## 📧 Voice-Based Email

The assistant can send emails using Python's `smtplib`.

Example:

```text
You: Send an email
Assistant: Who should I send it to?
You: Test account
Assistant: What is the message?
You: Hello, this is a test email.
```

For testing, use a dedicated dummy/test email account.

**Never upload real passwords or email credentials to GitHub.**

---

## ⏰ Reminders

The assistant can create timed reminders.

Example:

```text
You: Remind me after 10 minutes
Assistant: Okay, I will remind you in 10 minutes.
```

After the specified duration:

```text
Assistant: Reminder! Your 10 minutes are over.
```

---

## 📚 General Knowledge

The assistant can be extended to answer general knowledge questions using:

* A local knowledge base
* A QA API
* A suitable NLP model

Example:

```text
You: What is artificial intelligence?
Assistant: Artificial intelligence is the field of creating computer systems
that can perform tasks that normally require human intelligence.
```

---

## ⚙️ Custom Commands

Users can add their own commands through a configuration file.

Example:

```json
{
    "commands": {
        "open youtube": "https://www.youtube.com",
        "open github": "https://github.com",
        "open google": "https://www.google.com"
    }
}
```

The assistant can read these commands and perform the corresponding actions.

---

# 🔐 Privacy Considerations

The assistant may process:

* Voice input
* Recognized speech/text
* User commands
* Search queries
* Weather requests
* Email information, if the email feature is enabled

Online speech recognition may send recorded speech to an external service for processing.

Users should be informed about what data is processed and which external services are used.

### Security Recommendations

Never store sensitive information directly in source code.

Do not upload:

```text
API keys
Passwords
Email credentials
Authentication tokens
Private personal information
```

Use environment variables or a local configuration file instead.

Add sensitive configuration files to `.gitignore`:

```text
config.json
.env
```

---

# 🧪 Testing

Test the assistant with different commands.

### Basic Tests

* [ ] Test microphone input
* [ ] Test "Hello"
* [ ] Test time command
* [ ] Test date command
* [ ] Test web search
* [ ] Test unknown command
* [ ] Test speech recognition failure
* [ ] Test exit command

### Advanced Tests

* [ ] Test NLP intent recognition
* [ ] Test weather API
* [ ] Test email sending
* [ ] Test reminders
* [ ] Test custom commands
* [ ] Test invalid API responses
* [ ] Test missing internet connection

---

# ⚠️ Error Handling

The assistant should handle common errors gracefully.

Examples include:

```text
Microphone unavailable
Speech not understood
Internet connection unavailable
API request failed
Invalid command
Invalid email address
Invalid API key
```

Instead of terminating the program, the assistant should provide a useful response and continue running whenever possible.

---

# 📋 Example `requirements.txt`

```text
SpeechRecognition
pyttsx3
PyAudio
requests
nltk
```

Additional libraries can be added depending on the advanced implementation.

---

# 🔮 Future Improvements

Possible future improvements include:

* Wake-word detection such as "Hey Assistant"
* Offline speech recognition
* More advanced NLP
* AI-powered conversations
* Music playback
* Application launching
* Smart home control
* Calendar integration
* News updates
* WhatsApp or messaging integration
* Voice authentication
* Graphical user interface
* Multilingual voice support

---

# 🎓 Learning Outcomes

By completing this project, you can learn:

* Python programming
* Speech recognition
* Text-to-speech systems
* API integration
* Natural language processing
* Exception handling
* File/configuration management
* SMTP email communication
* Working with external services
* Basic software architecture
* Privacy and security considerations

---

# 👨‍💻 Author

**Shaik Mohammed Khaiser Hussain**

Engineering Student | Computer Science and Engineering Student

---

# 📄 License

This project is intended for educational and learning purposes.

You are free to modify and extend the project for personal or academic use.

---

## ⭐ Acknowledgements

This project uses open-source Python libraries and external services for speech recognition, text-to-speech, web search, weather information, and other functionality.

If you find this project useful, consider giving the repository a ⭐ on GitHub.
