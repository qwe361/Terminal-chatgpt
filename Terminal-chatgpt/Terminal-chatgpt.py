import json
import urllib.request
import urllib.parse

# 获取OpenAI API Key
while True:
    api_key = input("请输入您的OpenAI API Key：")

    # 检查API Key是否有效
    url = "https://api.openai.com/v1/engines/davinci/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "prompt": "test",
        "max_tokens": 1,
        "n": 1,
        "stop": None,
        "temperature": 0.5
    }

    req = urllib.request.Request(url, json.dumps(data).encode(), headers)

    try:
        with urllib.request.urlopen(req) as f:
            response = json.load(f)
        break
    except urllib.error.HTTPError as error:
        print(f"OpenAI API Key无效，请重新输入：{error}")
    except Exception as error:
        print(f"发生错误，请重新输入：{error}")

print("OpenAI API Key已验证成功！")

# 向ChatGPT发送文本并获取回答


def get_answer(prompt):
    url = "https://api.openai.com/v1/engines/davinci/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "prompt": prompt,
        "max_tokens": 60,
        "n": 1,
        "stop": None,
        "temperature": 0.5
    }

    req = urllib.request.Request(url, json.dumps(data).encode(), headers)

    with urllib.request.urlopen(req) as f:
        response = json.load(f)

    answer = response["choices"][0]["text"].strip()
    return answer


# 与用户交互
while True:
    # 获取用户输入
    user_input = input("请问有什么需要我帮助的吗？")

    # 向ChatGPT发送用户输入，并获取回答
    answer = get_answer(user_input)

    # 输出ChatGPT的回答
    print(answer)
