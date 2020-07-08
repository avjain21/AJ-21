import speech_recognition as SRG
import time

store=SRG.Recognizer()
with SRG.Microphone() as s:

	print("Hey, Please Speak...")
	audio_input = store.record(s,duration=7)
	print("Recording Time:", time.strftime("%I:%M:%S"))

	try:
		text_output = store.recognize_google(audio_input)
		print("Text converted from Audio:\n")
		
		print("I think you said \n" + text_output)
		print(" F I N I S H !")
		print("Execution time:",time.strftime("%I:%M:%S"))
	except:
		print("Couldn't process the audio input.")