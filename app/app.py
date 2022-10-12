from flask import Flask, redirect, url_for, request

try:
    from .tkitTextSegmentaion.text_segmentation import textSegmentation,text_segmentation
except ImportError:
    from tkitTextSegmentaion.text_segmentation import textSegmentation,text_segmentation
import os
if os.path.isfile ("data/word2vec.6B.bin"):

    glove_file="data/word2vec.6B.bin"
else:
    glove_file="/code/app/data/word2vec.6B.bin"

# # seg_obj=textSegmentation(glove_file)
# def auto(text,k):

#     if os.path.isfile ("data/word2vec.6B.bin"):

#         glove_file="data/word2vec.6B.bin"
#     else:
#         glove_file="/code/app/data/word2vec.6B.bin"

#     seg_obj=textSegmentation(glove_file)
#     # print("text",text)
#     return seg_obj.auto(str(text),k=int(k))
app = Flask(__name__)

@app.route('/')
def hello():
    return """
        分段
        api '/text_segmentation'
        {
        "text": "It’s all-too-tempting to recreate that Lady and the Tramp scene with your pup, sharing a plate of pasta and almost smooching their adorable nose. It undoubtedly makes for a cute photo, but is pasta actually safe for them to eat? It turns out, the answer isn’t crystal clear.    While some veterinarians say it’s perfectly fine for your dog to eat a moderate amount of pasta, others disagree. The amount of pasta given to a dog and the pasta’s ingredients play a large role. And, like with all foods, you should first make sure your pet isn’t allergic to pasta or its ingredients before you give them a heaping plate of spaghetti.",
        "k": 3
        }
"""


@app.route("/text_segmentation",methods = ['POST'])
def text_segmentation():
    """
    The text_segmentation function takes a text string and returns a list of paragraphs.
    The paragraph is defined as the longest sequence of characters without any newline.



        {
        "text": "It’s all-too-tempting to recreate that Lady and the Tramp scene with your pup, sharing a plate of pasta and almost smooching their adorable nose. It undoubtedly makes for a cute photo, but is pasta actually safe for them to eat? It turns out, the answer isn’t crystal clear.    While some veterinarians say it’s perfectly fine for your dog to eat a moderate amount of pasta, others disagree. The amount of pasta given to a dog and the pasta’s ingredients play a large role. And, like with all foods, you should first make sure your pet isn’t allergic to pasta or its ingredients before you give them a heaping plate of spaghetti.",
        "k": 3
        }



    :param item:Item: Used to Pass the item to the function.
    :return: A dictionary with the key 'paragraph' and a value that is a list of strings.

    :doc-author: Trelent
    """

    # print("text_segmentation")
    # print(item)
    # print(item.text)
    # out =auto(item.text,item.k)


    if request.is_json:
        # name = request.json.get('name')
        # age = request.json.get('age') # auto type casting depending on the json format
        data=request.json
        print(data)
    else:
        return {}
    # print("text",text)
    # out=seg_obj.auto(str(data['text']),k=int(data['k']))

    if os.path.isfile ("data/word2vec.6B.bin"):

        glove_file="data/word2vec.6B.bin"
    else:
        glove_file="/code/app/data/word2vec.6B.bin"
    out=auto_segmentation(text=str(data['text']),k=int(data['k']),glove_file)


    return {"paragraph":list(out)}
    # return {}
    # return {}
if __name__ == '__main__':
   app.run(debug = True)