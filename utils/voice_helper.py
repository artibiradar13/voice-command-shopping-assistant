import speech_recognition as sr

def get_voice_command():

    r = sr.Recognizer()

    try:

        with sr.Microphone() as source:

            print("Listening...")

            r.adjust_for_ambient_noise(source)

            audio = r.listen(source, timeout=5, phrase_time_limit=5)

        print("Processing...")

        command = r.recognize_google(audio)

        print("You said:", command)

        return command.lower()

    except sr.WaitTimeoutError:

        return None

    except sr.UnknownValueError:

        return None

    except sr.RequestError:

        return None