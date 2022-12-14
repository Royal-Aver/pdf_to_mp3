from gtts import gTTS
import pdfplumber
from pathlib import Path

def pdf_to_mp3(file_path='test.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print('Processing...')

        # Read file into string
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        # glue all pages
        text = ''.join(pages)
        text = text.replace('\n', '')

        # convert text to mp3
        my_audio = gTTS(text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'Successfully! {file_name}.mp3 was added'

    else:
        return 'Invalid file, please check'


def main():
    file_path = input('Enter path to file: ')
    language = input('Enter language, "ru" or "en": ')
    print(pdf_to_mp3(file_path, language))


if __name__ == '__main__':
    main()
