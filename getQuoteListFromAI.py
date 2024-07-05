from random import choice
# import g4f
# import g4f.client


# contentList = [
#     "give me a 30-60 seconds amazing facts on a random topic, make sure to make it interesting",
#     "give me a 40-60 seconds script on a single real mystifying marvels of enginerring , make sure to make it interesting",
# ]

# positiveParameters = "give a list of 4 keywords to search for bit sized video clips from pexels. Return plain text output in the given format: output: output than keywords: csv of keywords. make keyword comma seperated"

# def getQuoteListFromAI(topic=None):
#     '''
#     This function generates a list of quotes or facts from the AI.

#     Args:
#         topic (str): The topic to generate the quotes on. Default is None.

#     Returns:
#         list: The list of quotes or facts.
#     '''

#     if (topic == None):
#         topic = choice(contentList)
#     else:
#         topic = topic
#     # outputs string of text
#     engine = g4f.client.Client()

#     completion = engine.chat.completions.create(
#         model="gpt-4",
#         # model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": topic + "." + positiveParameters}])

#     output = completion.choices[0].message.content
#     return output


def cleanTextOut(inputTextList):
    '''
    This function formates the text output from the AI.

    Args:
        inputTextList (list): The list of text output from the AI.

    Returns:
        output (str): The cleaned and formatted text output.
        keyword (list): The list of keywords.
    '''
    # inputTextList is a list
    inputTextList = "".join(inputTextList)
    inputTextList = inputTextList.strip().replace("*", "")
    inputTextList = inputTextList.replace("\n", "")
    try:
        output = inputTextList.split(
            "Output:")[1].split("Keywords:")[0].strip()
        keyword = inputTextList.split("Keywords:")[1].strip().split(",")
    except:
        output = inputTextList.split(
            "output:")[1].split("keywords:")[0].strip()
        keyword = inputTextList.split("keywords:")[1].strip().replace(
            '"', '').replace("'", "").split(",")

    # output is a array of 2 items fact, keyword
    # keyword is a list of keywords
    return output, keyword
