#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import re


with open('dialogue.json') as f:
  d = json.load(f)

prev_person = None

# FIXME: Use your own names here, renaming people is used to introduce words, which are not a part of your dialogue
# Kind of like codewords
person_map = {'Имя1': 'Псевдоним1', 'Имя2': 'Псевдоним2'}

files = [sys.stdout, sys.stderr]

switch_idx = int(len(d['messages']) * 0.9)
cur_file_idx = 0
for idx, m in enumerate(d['messages']):
  if 'action' in m and m['action'] == 'phone_call':
    continue
  assert('from' in m)
  cur_person = m['from']
  if prev_person != cur_person:
    if prev_person is not None:
      print(file=files[cur_file_idx])
      #print('next_person\n', file=files[cur_file_idx])
    if idx >= switch_idx and cur_file_idx == 0:
      cur_file_idx = 1
    print(person_map[cur_person], file=files[cur_file_idx])
  msgs = m['text']
  if type(msgs) != list:
    msgs = [msgs]
  full_msg = ''
  for msg in msgs:
    if type(msg) == dict:
      assert('text' in msg)
      msg = msg['text']
    assert(type(msg) == str)
    full_msg += msg + '\n'

  if 'sticker_emoji' in m:
    full_msg = m['sticker_emoji']
  if 'photo' in m:
    full_msg = '[Фото] ' + full_msg
  if 'media_type' in m:
    if m['media_type'] == 'video_file':
      full_msg = '[Видео] ' + full_msg
    elif m['media_type'] == 'audio_file':
      full_msg = '[Аудио] ' + full_msg
  if 'mime_type' in m:
    if 'pdf' in m['mime_type']:
      full_msg = '[Пдф] ' + full_msg
    elif 'audio' in m['mime_type']:
      full_msg = '[Аудио] ' + full_msg
    elif 'video' in m['mime_type']:
      full_msg = '[Видео] ' + full_msg
    elif 'image' in m['mime_type']:
      full_msg = '[Фото] ' + full_msg

  while '\n\n' in full_msg:
    full_msg = full_msg.replace('\n\n', '\n')

  full_msg = full_msg.replace('😂', ' [эмодзи слёзы-радость]')
  full_msg = full_msg.replace('😭', ' [эмодзи слёзы-печаль]')
  full_msg = full_msg.replace('🖤', ' [эмодзи сердце]')
  full_msg = full_msg.replace('💜', ' [эмодзи сердце]')
  full_msg = full_msg.replace('❤️', ' [эмодзи сердце]')
  full_msg = full_msg.replace('🧡', ' [эмодзи сердце]')
  full_msg = full_msg.replace('😬', ' [эмодзи зубы]')
  full_msg = full_msg.replace('👌', ' [эмодзи ок]')
  full_msg = full_msg.replace('💦', ' [эмодзи сквирт]')
  full_msg = full_msg.replace('😏', ' [эмодзи намёк]')
  full_msg = full_msg.replace('🧜', ' [эмодзи русалка]')
  full_msg = full_msg.replace('🤔', ' [эмодзи хм]')
  full_msg = full_msg.replace('😳', ' [эмодзи ой]')
  emoji_pattern = re.compile("["
      u"\U0001F600-\U0001F64F"  # emoticons
      u"\U0001F300-\U0001F5FF"  # symbols & pictographs
      u"\U0001F680-\U0001F6FF"  # transport & map symbols
      u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
      "]+", flags=re.UNICODE)
  full_msg = emoji_pattern.sub(r'', full_msg)

  print(full_msg.strip(), file=files[cur_file_idx])
  prev_person = cur_person

print(file=files[cur_file_idx])

