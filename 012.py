# -*- coding: utf-8 -*-
import re
import random


class SimpleKernel:
    def __init__(self):
        self.categories = {}
        self.last_response = None
        self.variables = {}

    def learn(self, aiml_content):
        pattern = re.compile(r'<category>\s*<pattern>(.*?)</pattern>(?:\s*<that>(.*?)</that>)?\s*<template>(.*?)</template>\s*</category>', re.DOTALL)
        matches = pattern.findall(aiml_content)

        for match in matches:
            pattern_text = match[0].strip().upper()
            that_text = match[1].strip().upper() if match[1] else None
            template_text = match[2].strip()
            self.categories[(pattern_text, that_text)] = template_text

    def respond(self, input_text):
        input_text = input_text.strip().upper()

        for (pattern_text, that_text), template_text in self.categories.items():
            if re.match(pattern_text.replace('*', '.*'), input_text):
                if that_text is None or (self.last_response and re.match(that_text.replace('*', '.*'), self.last_response)):
                    self.last_response = input_text
                    response = self.process_template(template_text)
                    return response
        return "Sorry, I don't understand that."

    def process_template(self, template):
        if '<random>' in template:
            choices = re.findall(r'<li>(.*?)</li>', template, re.DOTALL)
            template = random.choice(choices)
            template = re.sub(r'<get name="(.*?)"/>', lambda match: self.variables.get(match.group(1), ''), template)
        return template

    def set_variable(self, name, value):
        self.variables[name] = value


# 修改下列 AIML 内容，完成问答配置
aiml_content = '''
<aiml version="1.0.1" encoding="UTF-8">
    <category>
        <pattern>HELLO</pattern>
        <template>Hi there!</template>
    </category>
    <category>
        <pattern>HOW ARE YOU</pattern>
        <template>I'm doing well, thank you!</template>
    </category>
    <category>
        <pattern>WHAT IS YOUR NAME</pattern>
        <template>My name is Alice.</template>
    </category>
    <category>
        <pattern>你多大了</pattern>
        <template>
            <random>
                <li>哇, <get name="age"/> , 如花似玉的年龄.</li>
                <li>你都 <get name="age"/> 了, 好老.</li>
                <li><get name="age"/> , 我比你年轻好多好多.</li>
                <li>哦，<get name="age"/> , 您学到的知识比我多得多呢.</li>
            </random>
        </template>
    </category>
    <category>
        <pattern>*睡*</pattern>
        <template>我是人工智能，不需要睡觉。不过，真希望自己也能做个美梦呢。。</template>
    </category>
</aiml>
'''

# 创建内核实例并加载 AIML 内容
alice = SimpleKernel()
alice.【1】(aiml_content) 
alice.set_variable("age", "25")  # 设置变量年龄

# 模拟用户输入
user_inputs = [
    "HELLO",
    "HOW ARE YOU",
    "WHAT IS YOUR NAME",
    "你多大了",
    "我在睡觉",
    "你这个价格多少啊？",
    "你这个价格有点贵啊！"
]

# 处理每个用户输入并打印响应
for user_input in user_inputs:
    print(f"我是您的智能服务机器人，请您提问...>> {user_input}")
    response = alice.respond(user_input)
    print(response)