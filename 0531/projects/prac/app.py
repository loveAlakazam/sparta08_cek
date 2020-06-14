from flask import Flask
app = Flask(__name__) #현재파일을 플라스크 서버파일로 만들겠다. / 이 파일을 서버로 설정하겠다.

@app.route('/') # api를 정의한다.  => 각페이지의 기능을 의미한다.
#=> 서버와 클라이언트와 통신
# url을 가지고 기능을 구분한다.

def home():
    # 브라우저에게 리턴해준다.
    return 'This is Hometown! 방가워요~' 

# 터미널로 실행할때 먼저 실행한다.
if __name__ == '__main__':
    # 서버를 실행하겠다. 포트번호를 5000번으로 한다.
    # 하나의 컴퓨터에서 여러개 프로그램 실행할때, 어떤 프로그램을 실행할지를 구분
    # (ip주소):(포트번호)
    # debug: 정보요청이 들어왔을때 그 정보에 대해서 디테일을 출력해주겠다. (개발할때만 디버그옵션을 참으로 함.)

    # 웹서버는 사용자가 끄지않는이상 계속 동작한다.
    # localhost:5000 으로 홈페이지를 접근한다. 
    # 플라스크종료: ctrl+c / (mac) ctrl +c
    app.run('0.0.0.0',port=5000,debug=True)