import pypdf
import pyttsx3

pdfReader = pypdf.PdfReader(open('K:/NewJavaMaterial/New folder/PDF_to_Voice/data/GOLDMAN.pdf', 'rb'))
speaker = pyttsx3.init()

voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)  
speaker.setProperty('rate', 170)
speaker.setProperty('volume', 1.0)

full_text = ""

for page_num in range(len(pdfReader.pages)):
    text = pdfReader.pages[page_num].extract_text()
    if text:
        full_text += text
        speaker.say(text)
        speaker.runAndWait()

speaker.stop()

speaker.save_to_file(full_text, 'K:/NewJavaMaterial/New folder/PDF_to_Voice/data/audio.mp3')
speaker.runAndWait()