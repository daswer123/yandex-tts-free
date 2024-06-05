# Yandex TTS Python

Этот Python скрипт позволяет генерировать речь из текста, используя Yandex SpeachKit API. Доступен только Русский язык. Вы можете выбрать голос и настроение для синтезированной речи.

## Доступные голоса

- levitan
- zahar
- silaerkan
- oksana
- jane
- omazh
- kolya
- kostya
- nastya
- sasha
- nick
- zhenya
- tanya
- ermilov
- alyss
- ermil with tunning
- robot
- dude
- zombie
- smoky

## Доступные настроения

- neutral
- evil
- good

## Использование

```python
from yandexspeach import YandexFreeTTS

tts = YandexFreeTTS()
output_path = 'output'
text = 'Это тестовый текст для проверки голосов.'

# Генерация речи с голосом levitan и нейтральным настроением
tts.generate_speech_ya(output_path, 'test.mp3', text, 'levitan')

# Генерация речи с голосом oksana и настроением good
tts.generate_speech_ya(output_path, 'test_good.mp3', text, 'oksana', 'good')
```

## Отказ от ответственности

Этот скрипт не является официальным продуктом Яндекса и использует их TTS API. Используйте его на свой страх и риск. Я не несу ответственности за любые проблемы, которые могут возникнуть в результате использования этого скрипта.
