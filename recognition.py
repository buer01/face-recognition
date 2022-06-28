import json

from PIL import Image

from facenet import Facenet

model = Facenet()
threshhold = "0.71"
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
        print(i[0],end=" ")
    print("")
    probability_min = min(result)
    index = result.index(probability_min)
    print(probability_min)
    if(probability_min<threshhold):
        print(db_list[index]["id"])
        return db_list[index]["id"]
    else:
        print("not found")
        return 0

if __name__ =="__main__":
    path = input("img_path")
    recognition_face(path)
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
