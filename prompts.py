import json
def make_prompt(prompt, slide_count, additional_info, language):
    if slide_count:
        slide_count = f"它必须恰好有{slide_count}张幻灯片/内容！！"
    else:
        slide_count = "至少8张幻灯片/内容。"
    if additional_info:
        additional_info = f"还请注意演示文稿：\n{additional_info}"
    
    if language=="1":
        language = "中文"
    else:
        language = "英文"

    output_format=json.dumps({
        "title": "TITLE OF THE PRESENTATION",
        "slides": [
            {
                "slide_number": 1,
                "header": "TABLE OF CONTENT",
                "content": [
                    {"paragraph": "CONTENT OF THIS POWERPOINT", "description": ""},
                    {"paragraph": "CONTENT OF THIS POWERPOINT", "description": ""},
                    {"paragraph": "CONTENT OF THIS POWERPOINT", "description": ""}
                ]
            },
            {
                "slide_number": 2,
                "header": "TITLE OF SLIDE",
                "content": [
                    {"paragraph": "title for paragraph 1", "description": "detail for paragraph 1"},
                    {"paragraph": "title for paragraph 2", "description": "detail for paragraph 2"}
                ]
            },
            {
                "slide_number": 3,
                "header": "TITLE OF SLIDE",
                "content": [
                    {"paragraph": "title for paragraph 1", "description": "detail for paragraph 1"},
                    {"paragraph": "title for paragraph 2", "description": "detail for paragraph 2"}
                ]
            },
            {
                "slide_number": 4,
                "header": "SUMMARY",
                "content": [
                    {"paragraph": "title for paragraph 1", "description": "detail for paragraph 1"},
                    {"paragraph": "title for paragraph 2", "description": "detail for paragraph 2"}
                ]
            },
            {
                "slide_number": "X",
                "header": "END",
                "content": [
                    {"paragraph": "title for paragraph 1", "description": "detail for paragraph 1"},
                    {"paragraph": "title for paragraph 2", "description": "detail for paragraph 2"}
                ]
            }
        ]
    }, ensure_ascii=True)

    main_prompt = f'''我要准备1个关于{prompt}的PPT，{slide_count}，请你根据主题生成详细内容，不要省略。
    生成结果必须符合以下条件：
    1.严格按照这个JSON格式输出{output_format}，只能返回JSON，且JSON不要用```包裹，确保响应结果可以由python json.loads()成功加载。
    2.内容要用{language}。
    3.在slide_number: 1中只需要paragraph，description为空字符串就可以。
    4.每个幻灯片里面的description写的多一点详细一点。'''

    return main_prompt

# print(make_prompt(prompt='12345',slide_count=5,additional_info='',language=1))

        
#     main_prompt = f"""我要准备1个关于{prompt}的PPT，{slide_count}，请你根据主题生成详细内容，不要省略。
# 您必须遵循以下几点：
# - 您制作的标题非常短！每页的内容尽可能丰富！
# - 您使演示易于理解。
# - 演示具有与幻灯片/内容计数相匹配的目录。
# - 内容要用中文。

# {additional_info}

# 以下是输出格式示例！- 严格遵循这种格式！

# Title: TITLE OF THE PRESENTATION

# Slide: 1
# Header: TABLE OF CONTENT
# Content: 
# Paragraph: CONTENT OF THIS POWERPOINT
# Paragraph: CONTENT OF THIS POWERPOINT
# Paragraph: CONTENT OF THIS POWERPOINT
# ...

# Slide: 2
# Header: TITLE OF SLIDE
# Content: 
# Paragraph: title for paragraph 1, 
# Description: detail for paragraph 1, 
                   
# Paragraph: title for paragraph 2, 
# Description": detail for paragraph 2, 

# Slide: 3
# Header: TITLE OF SLIDE
# Content: 
# Paragraph: title for paragraph 1, 
# Description: detail for paragraph 1, 
                   
# Paragraph: title for paragraph 2, 
# Description": detail for paragraph 2, 
# ...

# Slide: X
# Headers: SUMMARY
# Content: 
# Paragraph: title for paragraph 1, 
# Description: detail for paragraph 1, 
                   
# Paragraph: title for paragraph 2, 
# Description": detail for paragraph 2, 

# Slide: END
# """

#     return main_prompt

# def make_prompt(prompt, slide_count, additional_info, model_type):
#     # if slide_count:
#     #     slide_count = f"它必须恰好有 {slide_count} 张幻灯片/内容！！"
#     # else:
#     #     slide_count = "至少8张幻灯片/内容。"
#     if additional_info:
#         additional_info = f"还请注意演示文稿：\n{additional_info}"

#     if model_type == "vicuna":
#         prefix = "USER:"
#         suffix = "ASSISTANT:"
#     elif model_type == "alpaca":
#         prefix = "### Instruction:"
#         suffix = "### Response:"
#     elif model_type == "chatml":
#         prefix = "<|im_start|>user\n"
#         suffix = "<|im_end|>\n<|im_start|>assistant\n"
#     elif model_type == "llama2chat":
#         prefix = "[INST] "
#         suffix = " [/INST]"
#     else:
#         prefix = "### Instruction:"
#         suffix = "### Response:"
        
#     output_format=json.dumps({
#         "title":"example title",
#         "pages":[
#             {
#                 "Header": "title for page 1",
#                 "content": [
#                     {
#                         "title": "title for paragraph 1",
#                         "description": "detail for paragraph 1",
#                     },
#                     {
#                         "title": "title for paragraph 2",
#                         "description": "detail for paragraph 2",
#                     },
#                 ],
#             },
#             {
#                 "Header": "title for page 2",
#                 "content": [
#                     {
#                         "title": "title for paragraph 1",
#                         "description": "detail for paragraph 1",
#                     },
#                     {
#                         "title": "title for paragraph 2",
#                         "description": "detail for paragraph 2",
#                     },
#                     {
#                         "title": "title for paragraph 3",
#                         "description": "detail for paragraph 3",
#                     },
#                 ],
#             },
#         ],
#     },ensure_ascii=True)
#     main_prompt = f"""我要准备1个关于{prompt}的PPT，要求一共写{slide_count}页，请你根据主题生成详细内容，不要省略。
#     按这个JSON格式输出{output_format}，只能返回JSON，且JSON不要用```包裹，内容要用中文。"""

#     return main_prompt
