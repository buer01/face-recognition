import json
import os
import time

import sys
sys.path.append("..")

from flask import Flask, request, render_template
from recognition import rec


app = Flask(__name__)
rec = rec()

@app.route('/reg')
def reg():  # put application's code here
    # return 'Hello World!'
    return render_template("reg.html")

@app.route('/up')
def up():  # put application's code here
    # return 'Hello World!'
    return render_template("up.html")


@app.route('/register', methods=['POST'])
def register():
    img = request.files.get('img')  # 从post请求中获取图片数据
    print(img.filename)
    suffix = '.' + img.filename.split('.')[-1]  # 获取文件后缀名
    # basedir = os.path.abspath(os.path.dirname(__file__))  # 获取当前文件路径
    save_name = str(int(time.time())) + suffix
    photo = "../img/db/" + save_name  # 拼接相对路径
    img_path = photo  # 拼接图片完整保存路径,时间戳命名文件防止重复
    img.save(img_path)  # 保存图片
    print(img_path)

    # 其他参数用request.form字典获取
    id = request.form.get('stuid', '')
    print(id)

    with open("../img/db.json") as f:
        content = json.load(f)
    dit = {"id":id,"path":"../img/db/"+save_name}
    content.append(dit)
    with open("../img/db.json","w") as f_new:
        json.dump(content,f_new)

    return "success"


@app.route('/recognition', methods=['POST'])
def recognition():
    img = request.files.get('img')  # 从post请求中获取图片数据
    # print(img.filename)
    suffix = '.' + img.filename.split('.')[-1]  # 获取文件后缀名
    # basedir = os.path.abspath(os.path.dirname(__file__))  # 获取当前文件路径
    save_name = str(int(time.time())) + suffix
    photo = "../img/temp/" + save_name  # 拼接相对路径
    img_path = photo  # 拼接图片完整保存路径,时间戳命名文件防止重复
    img.save(img_path)  # 保存图片
    print(img_path)
    result = rec.recognition_face(img_path)

    return result

if __name__ == '__main__':
    app.run(host="0.0.0.0")
