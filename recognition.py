import json

from PIL import Image

from facenet import Facenet

model = Facenet()

def recognition_face(image):
    result = []
    image_target = Image.open(image)
    with open("./img/db.json") as f:
        db_list = json.load(f)
    for db_dict in db_list:
        image2 = Image.open(db_dict['path'])
        probability = model.detect_image(image_target, image2)
        result.append(probability)
    for i in result:
        print(i,end=" ")
    print("*"*16)
    probability_max = max(result)
    index = result.index(probability_max)
    print(probability_max)
    print(db_list[index]["id"])

if __name__ =="__main__":
    # path = input("img_path")
    recognition_face("./img/1_001.jpg")
# if __name__ == "__main__":
#     model = Facenet()
#
#     while True:
#         image_1 = input('Input image_1 filename:')
#         try:
#             image_1 = Image.open(image_1)
#         except:
#             print('Image_1 Open Error! Try again!')
#             continue
#
#         image_2 = input('Input image_2 filename:')
#         try:
#             image_2 = Image.open(image_2)
#         except:
#             print('Image_2 Open Error! Try again!')
#             continue
#
#         probability = model.detect_image(image_1, image_2)
#         print(probability)
