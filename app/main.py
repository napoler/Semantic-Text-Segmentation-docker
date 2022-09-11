from typing import Union

from fastapi import FastAPI
from .tkitTextSegmentaion import text_segmentation
from pydantic import BaseModel
import os
if os.path.isfile ("data/word2vec.6B.bin"):

    glove_file="data/word2vec.6B.bin"
else:
    glove_file="/code/app/data/word2vec.6B.bin"
seg_obj=text_segmentation(glove_file)
app = FastAPI()
class Item(BaseModel):
    text: str # 原始文本
    k: int # 分段数目

@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}



@app.post("/text_segmentation")
def text_segmentation(item: Item):
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
    # print(item.text)
    out =seg_obj.auto(str(item.text),k=3)
    # print(out)
#     out=['It ’ s all-too-tempting to recreate that Lady and the Tramp scene with your pup , sharing a plate of pasta and almost smooching'
#  'their adorable nose . It undoubtedly makes for a cute photo , but is pasta actually safe for them to eat ? It turns out , the answer isn ’ t crystal clear . While some veterinarians say it ’ s perfectly fine for your dog to eat a moderate amount of pasta , others disagree . The amount of pasta given to a dog and the pasta ’ s ingredients play a large role . And , like with all foods , you should first make'
#  'sure your pet isn ’ t allergic to pasta or its ingredients before you give them a heaping plate of spaghetti .']
    print(out)
    return {"paragraph":list(out)}
    # return {}
