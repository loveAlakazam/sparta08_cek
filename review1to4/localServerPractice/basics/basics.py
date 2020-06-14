# flask server
from flask import Flask, render_template
app=Flask(__name__)

# 클라이언트(브라우저)가 localhost:5000/ 라는 url 을 요청하면
# 서버는 home() 함수를 실행한다.
# home()함수는 index.html을  반환한다.
# render_template()란 html을 리턴시킨다.
@app.route('/')
def home():
    return render_template('index.html')


# 클라이언트(브라우저)가 localhost:5000/test/get 이라는 url을 요청하면
# 서버는 test_get() 함수를 실행하는데, 데이터전달방식은 GET방식
# GET방식이란, 데이터를 읽는 역할이다. 데이터가 url에 노출된다.
@app.route('/test/get', methods=['GET'])
def test_get():
    title_receive=request.args.get('title_give')
    print(title_receive)

    # jsonify(...) == response
    # 페이지 요청에 대한 응답메시지이다.
    return jsonify({'result': 'success', 'msg': '이 요청은 GET방식이다.'})


# 클라이언트(브라우저)가 localhost:5000/test/post 라는 url을 요청하면
# 서버는 test_post()라는 함수를 실행하는데, 데이터 전달방식은 POST방식이다.
# POST방식이란, 데이터를 수정하고, 변경하고, 삭제하고, 추가(Create Update Delete)
@app.route('/test/post', methods=['POST'])
def test_post():
    title_receive=request.form['title_give']
    print(title_receive)

    # 클라이언트의 페이지 요청에대한 응답메시지를 json화 시킨다.
    return jsonify({'result': 'success', 'msg': '이 요청은 POST방식이다.'})


if __name__ =='__main__':
    app.run('0.0.0.0', port=5000, debug=True)