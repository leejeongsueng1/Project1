from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

# 회원가입
def signup(request):
    # 맨처음 화면로드시 GET방식으로 통신
    if request.method == 'GET':
        print('안된다')
        return render(request, 'accounts/signup.html')
    # signup의 form 의 method가 POST방식이므로 sign up 버튼을 클릭시 POST방식의 HTTP request발생
    elif request.method == 'POST':
        # POST.get으로 가져오면 값이 없을경우 None을 저장해줌
        user_id = request.POST.get('user_id')
        user_name =request.POST.get('user_name')
        user_password1 = request.POST.get('password1')
        user_password2 = request.POST.get('password2')
        user_loct_state = request.POST.get('user_loct_state')
        user_loct_city = request.POST.get('user_loct_city')
        user_cert = request.POST.get('user_cert')

        res_data = {}

        # 값 입력을 확인하는 로직
        # 모든값을 입력하지 않으면 에러를 발생시키고 화면에 렌더링
        # 비밀번호1 과 비밀번호2가 일치하지 않으면 에러를 발생시키고 화면에 렌더링
        # 모든값이 입력되고 비밀번호가 일치하면 저장하고 모델에 입력후 save

        if not (user_id and user_name and user_password1 and user_password2 and user_cert):
            res_data['error'] = '모든 값을 입력해야합니다.'
            return render(request,'accounts/signup.html', res_data)
        elif user_password1 != user_password2:
            res_data['error'] = '비밀번호 입력이 일치하지 않습니다.'
            return render(request,'accounts/signup.html', res_data)
        else:
            
            # user_id : 유저 아이디, 정규식을 통해서 cert할 예정
            # user_pw :  유저 비밀번호, 역시 정규식 비교를 통해 cert할 예정
            # user_name : 유저 이름, 외국인 케이스를 고려해 max_length를 15로 설정
            # user_cert : 유저 관리번호, 이 칼럼을 통해 등급을 고려할 예정
            # user_loct : 유저 주소, 도/시,군 정도만 입력해 비교를 쉽게 할 예정
            user_data = User()
            user_data.user_id = user_id
            user_data.user_name = user_name
            user_data.user_pw =  make_password(user_password1)
            user_data.user_loct = user_loct_state + ' ' + user_loct_city
            user_data.user_cert = user_cert
            # 모델 인스턴스를 SAVE
            user_data.save()
        #메인 화면으로 redirect함 추후 session을 추가할 예정
        return redirect('/main/')


# 로그인
def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    elif request.method == 'POST':
        userid = request.POST.get('user_id')
        password = request.POST.get('password')

        res_data = {}
        if not (userid and password):
            res_data['error'] = '모든 값을 입력해야합니다.'
        else:
            user = User.objects.get(user_id=userid)
            if check_password(password, user.user_pw):
                request.session['user'] = user.user_id
                # res_data['error']= '로그인 성공'

                return redirect('/main')
            else:
                res_data['error'] = '비밀번호가 틀렸습니다.'

        return render(request, 'accounts/login.html', res_data)

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/main')






