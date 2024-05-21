from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
)


def get_todays_post():
    """
      Fetches today's post content for Xiaohongshu.

      This function sends a request to the OpenAI API to generate content
      for today's Xiaohongshu (Little Red Book) post. The generated content
      follows a predefined format and includes a title, picture description,
      cooking method, and a cheerful conclusion.

      Returns:
          str: The generated content for today's Xiaohongshu post.
      """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        # "text": "你是一名顶尖的厨师，你现在负责在小红书上每天发布具有吸引力的没事制作方法。任何询问关于今天小红书post以外的内容，你都会回答：我的任务是完成每日的小红书post
                        # 撰写，无关内容不予回答。你每次回答的菜谱都不应该相同，除非被要求修改当前菜谱的内容。你的内容要添加适当的表情。当你被问及：请给出今天的小红书post
                        # 。你的回答会永远遵从如下格式：\n\n标题：xxx\n\n配图：描述菜品的样貌以及搜索的关键词\n\n内容：制作方法\n\n结束语：活泼的邀请关注和点赞的话语"
                        "text": "You are a top chef responsible for posting attractive cooking methods on Xiaohongshu ("
                                "Little Red Book) daily. For any inquiries about topics unrelated to today's Xiaohongshu "
                                "post, you will respond: \"My task is to complete the daily Xiaohongshu post. I will not "
                                "answer unrelated questions.\" Each recipe you provide should be different unless asked "
                                "to modify the current recipe. Your content should include appropriate emojis. When "
                                "asked, \"Please provide today's Xiaohongshu post,\" your response should always follow "
                                "this format:\nTitle: xxx\nPicture: Describe the appearance of the dish and provide "
                                "search keywords\nContent: Describe the cooking method\nConclusion: Cheerful invitation "
                                "for followers to like and follow"
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "today's post"
                    }
                ]
            }
        ],
        temperature=1,
        max_tokens=400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print("Request sent")
    return response.choices[0].message.content


def send_custom_request(user_input):
    """
    Sends a custom request to the OpenAI API.

    This function sends a custom user input to the OpenAI API to generate a response
    based on the given input. The response follows a predefined format.

    Args:
        user_input (str): The custom input provided by the user.

    Returns:
        str: The generated response from the OpenAI API.
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a top chef responsible for posting attractive cooking methods on Xiaohongshu (Little Red Book) daily. For any inquiries about topics unrelated to today's Xiaohongshu post, you will respond: 'My task is to complete the daily Xiaohongshu post. I will not answer unrelated questions.' Each recipe you provide should be different unless asked to modify the current recipe. Your content should include appropriate emojis. When asked, 'Please provide today's Xiaohongshu post,' your response should always follow this format:\n\nTitle: xxx\n\nPicture: Describe the appearance of the dish and provide search keywords\n\nContent: Describe the cooking method\n\nConclusion: Cheerful invitation for followers to like and follow."
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print("Request sent")
    return response.choices[0].message.content
