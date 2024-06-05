import requests
import os
import re
import ffmpeg

class YandexFreeTTS:
    def __init__(self):
        self.voices = {
            'levitan': 'levitan',
            'zahar': 'zahar',
            'silaerkan': 'silaerkan',
            'oksana': 'oksana',
            'jane': 'jane',
            'omazh': 'omazh',
            'kolya': 'kolya',
            'kostya': 'kostya',
            'nastya': 'nastya',
            'sasha': 'sasha',
            'nick': 'nick',
            'zhenya': 'zhenya',
            'tanya': 'tanya',
            'ermilov': 'ermilov',
            'alyss': 'alyss',
            'ermil with tunning': 'ermil_with_tunning',
            'robot': 'robot',
            'dude': 'dude',
            'zombie': 'zombie',
            'smoky': 'smoky'
        }

        self.moods = ['neutral', 'evil', 'good']

    def get_voice(self, voice_name):
        return self.voices.get(voice_name, 'levitan')

    def get_mood(self, mood):
        return mood if mood in self.moods else 'neutral'

    def generate_speech_ya(self, output_path, filename, text, speaker, mood='neutral'):
        max_text_length = 990
        speaker = self.get_voice(speaker)
        mood = self.get_mood(mood)

        print(speaker, text)

        sentences = re.findall(r'[^\.!\?]+[\.!\?]+|[^\.!\?]+$', text)
        print(sentences)

        part = ''
        part_index = 0

        for i, sentence in enumerate(sentences):
            if (len(part) + len(sentence)) <= max_text_length:
                part += sentence
            else:
                self.generate_part(part, part_index, speaker, mood, output_path)
                part = sentence
                part_index += 1

        if part:
            self.generate_part(part, part_index, speaker, mood, output_path)

        files = [os.path.join(output_path, f'output{i+1}.mp3') for i in range(part_index+1)]

        if len(files) == 1:
            os.rename(files[0], os.path.join(output_path, filename))
            print(f'renamed output1.mp3 to {filename}')
        else:
            try:
                self.merge_audio(files, os.path.join(output_path, filename))
                print(f'merged all parts into {filename}')

                for file in files:
                    os.remove(file)
                print('deleted all individual parts')
            except Exception as e:
                print('error merging audio files:', e)

    def generate_part(self, text, index, speaker, mood, output_path):
        encoded_text = requests.utils.quote(text)

        try:
            response = requests.get(
                f'https://tts.voicetech.yandex.net/generate?key=d4f59475-9389-4622-a072-f1cbb0968bdf&text={encoded_text}&format=mp3&lang=ru-RU&emotion={mood}&speaker={speaker}&speed=1',
                stream=False
            )

            file_path = os.path.join(output_path, f'output{index+1}.mp3')
            with open(file_path, 'wb') as f:
                f.write(response.content)

        except Exception as e:
            print(f'error generating part {index+1}:', e)

    def merge_audio(self, files, output):
        command = ffmpeg.input('pipe:')
        for file in files:
            command = command.concat(file)
        command = command.output(output, c='copy')
        command.run()

# Тесты
# if __name__ == '__main__':
#     tts = YandexFreeTTS()
#     output_path = 'output'
#     os.makedirs(output_path, exist_ok=True)
#     test_text = 'Это тестовый текст для проверки голосов.'

#     # Тест для каждого голоса
#     for voice, voice_name in tts.voices.items():
#         print(f'Тестирование голоса: {voice}')
#         tts.generate_speech_ya(output_path, f'{voice}.mp3', test_text, voice_name)

#     # Тесты для разных настроений
#     tts.generate_speech_ya(output_path, 'evil.mp3', test_text, 'levitan', 'evil')
#     tts.generate_speech_ya(output_path, 'good.mp3', test_text, 'oksana', 'good')

#     print('Тесты завершены.')
