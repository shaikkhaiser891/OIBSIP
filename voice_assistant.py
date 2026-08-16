import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech recognition and text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    """Convert text to speech."""
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen to the microphone and convert speech to text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

            print("Recognizing...")
            command = recognizer.recognize_google(audio)

            print("You:", command)
            return command.lower()

        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that. Please repeat.")
            return ""

        except sr.RequestError:
            speak("The speech recognition service is currently unavailable.")
            return ""


def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")


def tell_date():
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today is {current_date}")


def search_web(topic):
    speak(f"Searching the web for {topic}")
    url = "https://www.google.com/search?q=" + topic.replace(" ", "+")
    webbrowser.open(url)


def process_command(command):

    if not command:
        return True

    # Greeting
    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    # Time
    elif "time" in command:
        tell_time()

    # Date
    elif "date" in command or "today" in command:
        tell_date()

    # Web search
    elif "search" in command:
        topic = command.replace("search", "", 1).strip()

        if topic:
            search_web(topic)
        else:
            speak("What would you like me to search for?")

    # Exit
    elif "exit" in command or "quit" in command or "stop" in command:
        speak("Goodbye! Have a great day.")
        return False

    else:
        speak("I don't know that command yet. Please try another command.")

    return True


def main():

    speak("Voice assistant started.")

    while True:
        command = listen()

        if not process_command(command):
            break


if __name__ == "__main__":
    main()