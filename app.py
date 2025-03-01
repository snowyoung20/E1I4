from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# 맥 사용자는 풀어서 사용하세요 - 본인 mongoDB로 변경하기
# import certifi
# ca = certifi.where()

# mongoDB는 김장원 - 본인 mongoDB로 변경하기
from pymongo import MongoClient
# 김장원mongoDB
client = MongoClient('mongodb+srv://sparta:test@cluster0.rsr8xyc.mongodb.net/?retryWrites=true&w=majority')
# 김희석mongoDB
# client = MongoClient('mongodb+srv://sparta:test@cluster0.txlb0px.mongodb.net/?retryWrites=true&w=majority',tlsCAFile =ca')
# 이은비mongoDB
# client = MongoClient('mongodb+srv://sparta:test@cluster0.ziorpfn.mongodb.net/?retryWrites=true&w=majority',tlsCAFile = ca')
# 이현경mongoDB
# client = MongoClient('mongodb+srv://sparta:test@cluster0.w1iiuru.mongodb.net/?retryWrites=true&w=majority')
# 임수영mongoDB
# client = MongoClient('')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

# 임수영님 서브 페이지 동작 관련 코드
@app.route("/myprofile/new", methods=["GET"])
def post_profile():
    return render_template('sub.html', member_id = id)

@app.route('/sub1')
def sub1():
    return render_template('sub1.html')

@app.route('/sub2')
def sub2():
    return render_template('sub2.html')

@app.route('/sub3')
def sub3():
    return render_template('sub3.html')

@app.route('/sub4')
def sub4():
    return render_template('sub4.html')

@app.route('/sub5')
def sub5():
    return render_template('sub5.html')

# 1김희석
# 데이터 보내기
@app.route("/subA1", methods=["GET"])
def subA1():
    profiles_data = list(db.profiles.find({'name':"김희석"},{'_id':False}))
    return jsonify({'result': profiles_data})

# 2이은비
# 데이터 보내기
@app.route("/subA2", methods=["GET"])
def subA2():
    profiles_data = list(db.profiles.find({'name':"이은비"},{'_id':False}))
    return jsonify({'result': profiles_data})

# 3이현경
# 데이터 보내기
@app.route("/subA3", methods=["GET"])
def subA3():
    profiles_data = list(db.profiles.find({'name':"이현경"},{'_id':False}))
    return jsonify({'result': profiles_data})

# 4김장원
# 데이터 보내기
@app.route("/subA4", methods=["GET"])
def subA4():
    profiles_data = list(db.profiles.find({'name':"김장원"},{'_id':False}))
    return jsonify({'result': profiles_data})

# 5임수영
# 데이터 보내기
@app.route("/subA5", methods=["GET"])
def subA5():
    profiles_data = list(db.profiles.find({'name':"임수영"},{'_id':False}))
    return jsonify({'result': profiles_data})

# 김희석 -----------------------------------------------------------------
# 방명록 저장하는 곳(김희석)
@app.route('/guestbook', methods=['POST'])
def guestbook_post():
   name_receive = request.form['name_give']
   comment_receive = request.form['comment_give']
   doc = {
       'name'  :name_receive,
       'comment' : comment_receive
   }
   db.guestbook_comments.insert_one(doc)
   return jsonify({'msg': '방명록이 등록되었습니다!'})

# 방명록 mongDB에서 index.html로 데이터 전송(김희석)
@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    all_comments = list(db.guestbook_comments.find({},{'_id':False}))
    #db.user.find 에서 users 바꿔야한다 일단 강의대로 fan으로 저장함
    #fan -> guestbool_comments 로 변경
    return jsonify({'result': all_comments})

# mac 사용자는 포트5001로 변경하세요.
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)