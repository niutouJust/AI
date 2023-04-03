#!/usr/bin/env python
#coding=utf-8
import os
import openai
import sys
prompt = sys.argv[1:]
msg = sys.argv[2:]
print("输入的prompt是:", prompt)
print("输入的msg是:",msg )
exit()
openai.api_key = os.getenv('OPENAI-KEY')
completion = openai.Completion.create(
          model="text-davinci-003",
            prompt="你将扮演一个电商产品编辑，帮我修改一个标题，这是一个产品信息的标题，帮我改的更好一些，这个标题是：",
                temperature=0,
                max_tokens=2048,
    )
print(completion)
print(completion.choices[0].text)

