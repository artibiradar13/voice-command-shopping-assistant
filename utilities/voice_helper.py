import speech_recognition as sr


def get_voice_command():

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:

            print("Listening...")

            recognizer.adjust_for_ambient_noise(source)

            audio = recognizer.listen(source)


            print("Recognizing...")

            command = recognizer.recognize_google(audio)


            return command.lower()


    except sr.UnknownValueError:

        return "Could not understand audio"


    except sr.RequestError:

        return "Voice service error"


    except Exception as e:

        return "Error: " + str(e)