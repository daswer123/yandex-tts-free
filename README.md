# yandex-tts-free

Этот Python пакет позволяет генерировать речь из текста, используя бесплатное Yandex SpeachKit API. Доступен только Русский язык. Вы можете выбрать голос и настроение для синтезированной речи.

## Установка

Для начала работы установите пакет через pip:

```
pip install yandex-tts-free
```

## Требования

Для использования этого пакета необходимо иметь установленный ffmpeg в системе.

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
from yandex_tts_free import YandexFreeTTS

tts = YandexFreeTTS()
output_path = 'output'
text = 'Это тестовый текст для проверки голосов.'

# Генерация речи с голосом levitan и нейтральным настроением
tts.generate_speech(output_path, 'test.mp3', text, 'levitan')

# Генерация речи с голосом oksana и настроением good
tts.generate_speech(output_path, 'test_good.mp3', text, 'oksana', 'good')
```

## Отказ от ответственности

Этот пакет не является официальным продуктом Яндекса и использует их бесплатное TTS API. Используйте его на свой страх и риск. Разработчики не несут ответственности за любые проблемы, которые могут возникнуть в результате использования этого пакета.