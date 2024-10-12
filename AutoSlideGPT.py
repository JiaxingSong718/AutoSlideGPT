import re
import time
from create_ppt import create_ppt
from create_ppt_text import create_ppt_text
from dotenv import load_dotenv
load_dotenv()

# These are all available designs:
#Design 1 = Envelope, beige
#Design 2 = Blue Bubble
#Design 3 = Light Blue Black
#Design 4 = Black, dark
#Design 5 = wood
#Design 6 = Multicolored, Simple
#Design 7 = Black, white

def generate_ppt(prompt, add_info, slides, theme, language):
    prompt = re.sub(r'[^\w\s.\-\(\)]', '', prompt)
    if not theme:
        print("No theme selected, using default theme.")
    if theme > 7:
        theme = 1
        print("Invalid theme number, default theme will be applied.")
    elif theme == 0:
        theme = 1
        print("Invalid theme number, default theme will be applied.")

    print("正在生成PowerPoint，这可能需要一些时间...\n")
    
    with open(f'Cache/{prompt}.txt', 'w', encoding='utf-8') as f:
        f.write(create_ppt_text(prompt, slides, add_info, language))

    ppt_path = create_ppt(f'Cache/{prompt}.txt', theme, prompt)
    return str(ppt_path)

# The main function
def main():
    print("欢迎使用AutoSlideGPT！")
    topic = input("请输入PowerPoint主题: ")
    add_info = input("在PowerPoint中考虑的因素（如果没有，请输入回车）：")
    if not add_info:
        add_info = ""
    slides = input("请输入PowerPoint的页数: ")
    language = input("请选择PowerPoint的语言（1为中文，2为英文）: ")
    theme = int(input("请选择PowerPoint的主题 (选择1-7): "))
    start_time = time.time()
    print ("生成PowerPoint并保存于：", generate_ppt(topic, add_info, slides, theme, language))
    end_time = time.time()
    print ("生成PowerPoint所用时间：", round((end_time - start_time), 2))
    
main()
