# -*- coding: utf-8 -*-
from flask import Flask, request
import json
from flask import render_template
app = Flask(__name__,static_url_path='/static')

# -*- coding: utf-8 -*-
from flask import render_template
@app.route('/')
def index():
   ## index=3
    ##f = open('Files/map.txt', 'r')
    ##posts=json.loads(f.readline())
    result_click=[]
    posts=[{"value": "sos1", "index": 1, "class": "b1",'idd':'(1;1)','people':0},
           {"value": "sos2", "index": 2, "class": "b1",'idd':'(1;2)','people':0},
           {"value": "sos3", "index": 3, "class": "b1",'idd':'(1;3)','people':0},
           {"value": "sos4", "index": 4, "class": "b1",'idd':'(1;4)','people':0},
           {"value": "sos4", "index": 5, "class": "b1", 'idd': '(1;5)', 'people': 0},
           {"value": "sos4", "index": 6, "class": "b1", 'idd': '(1;6)', 'people': 0},
           {"value": "sos4", "index": 7, "class": "b1", 'idd': '(1;7)', 'people': 0},
           {"value": "sos4", "index": 8, "class": "b1", 'idd': '(1;8)', 'people': 0},
           {"value": "sos4", "index": 9, "class": "b1", 'idd': '(1;9)', 'people': 0},
           {"value": "sos4", "index": 10, "class": "b1", 'idd': '(1;10)', 'people': 0},
           {"value": "sos4", "index": 11, "class": "b1", 'idd': '(1;11)', 'people': 0},
           {"value": "sos4", "index": 12, "class": "b1", 'idd': '(1;12)', 'people': 0},
           {"value": "sos4", "index": 13, "class": "b1", 'idd': '(1;13)', 'people': 0},
           {"value": "sos4", "index": 14, "class": "b1", 'idd': '(1;14)', 'people': 0},
           {"value": "sos4", "index": 15, "class": "b1", 'idd': '(1;15)', 'people': 0},
           {"value": "sos4", "index": 16, "class": "b1", 'idd': '(1;16)', 'people': 0},
           {"value": "sos4", "index": 17, "class": "b1", 'idd': '(1;17)', 'people': 0},
           {"value": "sos4", "index": 18, "class": "b1", 'idd': '(1;18)', 'people': 0},
           {"value": "sos4", "index": 19, "class": "b1", 'idd': '(1;19)', 'people': 0},
           {"value": "sos4", "index": 20, "class": "b1", 'idd': '(1;20)', 'people': 0},
           {"value": "sos4", "index": 21, "class": "b1", 'idd': '(1;21)', 'people': 0},
           {"value": "sos4", "index": 22, "class": "b1", 'idd': '(1;22)', 'people': 0},
           {"value": "sos4", "index": 23, "class": "b1", 'idd': '(1;23)', 'people': 0},
           {"value": "sos4", "index": 24, "class": "b1", 'idd': '(1;24)', 'people': 0},
           {"value": "sos4", "index": 25, "class": "b1", 'idd': '(1;25)', 'people': 0},
           {"value": "sos4", "index": 26, "class": "b2", 'idd': '(1;26)', 'people': 0},
           {"value": "sos4", "index": 27, "class": "b1", 'idd': '(1;27)', 'people': 2},
           ]
    return render_template('button.html',index_line=index,posts=posts,result_click=result_click)

@app.route("/waiting", methods=['POST'])
def echo():
    result_click = []
    posts = [{"value": "sos1", "index": 1, "class": "b1", 'idd': '(1;1)', 'people': 0},
                {"value": "sos2", "index": 2, "class": "b1", 'idd': '(1;2)', 'people': 0},
                {"value": "sos3", "index": 3, "class": "b1", 'idd': '(1;3)', 'people': 0},
                {"value": "sos4", "index": 4, "class": "b1", 'idd': '(1;4)', 'people': 0},
                {"value": "sos4", "index": 5, "class": "b1", 'idd': '(1;5)', 'people': 0},
                {"value": "sos4", "index": 6, "class": "b1", 'idd': '(1;6)', 'people': 0},
                {"value": "sos4", "index": 7, "class": "b1", 'idd': '(1;7)', 'people': 0},
                {"value": "sos4", "index": 8, "class": "b1", 'idd': '(1;8)', 'people': 0},
                {"value": "sos4", "index": 9, "class": "b1", 'idd': '(1;9)', 'people': 0},
                {"value": "sos4", "index": 10, "class": "b1", 'idd': '(1;10)', 'people': 0},
                {"value": "sos4", "index": 11, "class": "b1", 'idd': '(1;11)', 'people': 0},
                {"value": "sos4", "index": 12, "class": "b1", 'idd': '(1;12)', 'people': 0},
                {"value": "sos4", "index": 13, "class": "b1", 'idd': '(1;13)', 'people': 0},
                {"value": "sos4", "index": 14, "class": "b1", 'idd': '(1;14)', 'people': 0},
                {"value": "sos4", "index": 15, "class": "b1", 'idd': '(1;15)', 'people': 0},
                {"value": "sos4", "index": 16, "class": "b1", 'idd': '(1;16)', 'people': 0},
                {"value": "sos4", "index": 17, "class": "b1", 'idd': '(1;17)', 'people': 0},
                {"value": "sos4", "index": 18, "class": "b1", 'idd': '(1;18)', 'people': 0},
                {"value": "sos4", "index": 19, "class": "b1", 'idd': '(1;19)', 'people': 0},
                {"value": "sos4", "index": 20, "class": "b1", 'idd': '(1;20)', 'people': 0},
                {"value": "sos4", "index": 21, "class": "b1", 'idd': '(1;21)', 'people': 0},
                {"value": "sos4", "index": 22, "class": "b1", 'idd': '(1;22)', 'people': 0},
                {"value": "sos4", "index": 23, "class": "b1", 'idd': '(1;23)', 'people': 0},
                {"value": "sos4", "index": 24, "class": "b1", 'idd': '(1;24)', 'people': 0},
                {"value": "sos4", "index": 25, "class": "b1", 'idd': '(1;25)', 'people': 0},
                {"value": "sos4", "index": 26, "class": "b2", 'idd': '(1;26)', 'people': 0},
                {"value": "sos4", "index": 27, "class": "b1", 'idd': '(1;27)', 'people': 2},
                ]
    t=request.form[str(request.form['text'])]

    f = open('Files/data.txt', 'a')
    f.write(t)
    f.write('\n')
    f.close()
    f = open('Files/data.txt', 'r')
    if(len(f.readlines())<=2):

       print(len(f.readlines()))
       f.close()
       return render_template('result.html')
    else:
       f.close()
       f = open('Files/data.txt', 'w')
       f.close()
       return render_template('button.html', index_line=index, posts=posts, result_click=result_click)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)