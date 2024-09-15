import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary  # For music commands
import newsLibrary   # For news commands
import wikipedia
import calenderLibrary  # For calendar commands
import time
import jokeLibrary  # For joke and fun fact commands
import weatherLibrary  # For weather functionality

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Initialize the to-do list
to_do_list = []

def speak(text):
    """Function to convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    """Process the recognized command"""
    command = command.lower()
    
    if "open google" in command:
        webbrowser.open("https://www.google.com/")
        print("Opening Google")
        speak("Opening Google")
        
    elif "open youtube" in command:
        musicLibrary.openYouTubeHome()
        speak("Opening YouTube homepage")
        
    elif "play" in command:
        song_name = command.replace("play", "").strip()
        musicLibrary.playYouTubeSong(song_name)
        speak(f"Playing {song_name}")
        
    elif "news" in command:
        headlines = newsLibrary.get_news()
        if isinstance(headlines, list):
            for headline in headlines:
                print(f"News: {headline}")
                speak(headline)
        else:
            print(headlines)
            speak(headlines)
            
    elif "search wikipedia for" in command:
        topic = command.replace("search wikipedia for", "").strip()
        try:
            summary = wikipedia.summary(topic, sentences=2)
            print(f"According to Wikipedia: {summary}")
            speak(f"According to Wikipedia, {summary}")
        except wikipedia.exceptions.PageError:
            speak(f"Sorry, I couldn't find any information on {topic}.")
        except wikipedia.exceptions.DisambiguationError as e:
            speak(f"Your search term is too broad. Here are some options: {e.options[:5]}")
        except Exception as e:
            speak("Sorry, there was an error processing your Wikipedia request.")
    
    elif "what's my schedule" in command:
        schedule = calenderLibrary.get_today_schedule()
        speak(f"Today’s schedule: {schedule}")
        
    elif "add event" in command:
        event_details = command.replace("add event", "").strip()
        try:
            event_name, times = event_details.split("at")
            start_time, end_time = times.split("to")
            response = calenderLibrary.add_event(event_name.strip(), start_time.strip(), end_time.strip())
            speak(response)
        except ValueError:
            speak("I couldn't understand the event details. Please provide the details in the format: 'Event Name at YYYY-MM-DDTHH:MM to YYYY-MM-DDTHH:MM'.")
    
    elif "set timer" in command:
        try:
            duration = int(command.replace("set timer for", "").strip())
            speak(f"Setting a timer for {duration} seconds.")
            time.sleep(duration)
            speak("Time's up!")
        except ValueError:
            speak("I couldn't understand the timer duration. Please specify the duration in seconds.")
    
    elif "tell me a joke" in command:
        joke = jokeLibrary.get_joke()
        print(joke)
        speak(joke)
    
    elif "tell me a fun fact" in command:
        fact = jokeLibrary.get_fun_fact()
        print(fact)
        speak(fact)
    
    elif "add reminder" in command:
        reminder = command.replace("add reminder", "").strip()
        to_do_list.append(reminder)
        speak(f"Reminder added: {reminder}")
    
    elif "show reminders" in command:
        if to_do_list:
            speak("Here are your reminders:")
            for reminder in to_do_list:
                speak(reminder)
        else:
            speak("You have no reminders.")
    
    elif "weather" in command:
        city = command.replace("weather", "").strip() or "your default city"
        weather_report = weatherLibrary.get_weather(city)
        print(f"Weather in {city}: {weather_report}")
        speak(f"The weather in {city} is {weather_report}")
    
    elif "stop" in command or "exit" in command:
        print("Deactivating Jarvis...")
        speak("Deactivating Jarvis. Goodbye!")
        exit(0)
    
    else:
        print(f"Command '{command}' not recognized.")
        speak("Sorry, I didn't understand the command.")

def listen_for_command():
    """Function to continuously listen for commands after activation"""
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for a command...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=8)
            
            command = recognizer.recognize_google(audio)
            print(f"Command: {command}")
            processCommand(command)
        
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            speak("Sorry, I didn't understand that.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            speak("There was an issue with the speech recognition service.")
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            speak("No input detected, listening again...")
        except Exception as e:
            print(f"Error: {e}")
            speak(f"An error occurred: {e}")

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    # Initial activation of Jarvis
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for the activation word 'Jarvis'...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)

            word = recognizer.recognize_google(audio)
            print(f"Activation word: {word}")
            
            if word.lower() == "jarvis":
                speak("Jarvis is now active. Listening for your commands.")
                listen_for_command()  # Enter continuous command mode
        
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            speak("Sorry, I didn't understand that.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            speak("There was an issue with the speech recognition service.")
        except sr.WaitTimeoutError:
            print("Listening timed out.")
        except Exception as e:
            print(f"Error: {e}")
            speak(f"An error occurred: {e}")
