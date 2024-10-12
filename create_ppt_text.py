import os
import json
import dashscope
import prompts
from dashscope.api_entities.dashscope_response import Message

def json_to_text(data):
    if isinstance(data, str):  # 如果 data 是字符串，将其解析为字典
        data = json.loads(data)

    output = []
    output.append(f"Title: {data['title']}\n")
    
    for slide in data['slides']:
        if slide['slide_number'] != "END":
            output.append(f"Slide: {slide['slide_number']}")
            output.append(f"Header: {slide['header']}")
            output.append("Content:")
            for content in slide['content']:
                output.append(f"Paragraph: {content['paragraph']}")
                if 'description' in content:
                    output.append(f"description: {content['description']}")
            output.append("\n")
        else:
            output.append("Slide: END")
    
    return "\n".join(output)


def create_ppt_text(prompt, slides=15, info="", language="1"):
    final_prompt = prompts.make_prompt(prompt, slides, info, language)
    print(final_prompt)
    messages = [Message(role='system',content=prompt)]
    messages.append(Message(role='user',content=final_prompt))
    response = dashscope.Generation.call(
        model = 'qwen1.5-110b-chat',
        api_key = os.environ.get('API_KEY'),
        messages=messages
    )
    
    # 调用llm生成PPT内容
    # print(response)
    result = response['output']['text']
    print(result)
    output_text = json_to_text(result)
    return output_text

# create_ppt_text('python学习教程');exit()