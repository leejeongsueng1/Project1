from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from webs.loadingContext import *

# Create your views here.

# 회원가입
def signup(request):
    # 맨처음 화면로드시 GET방식으로 통신
    if request.method == 'GET':
        #이미 로그인이 되어있는지 확인
        user_data = check_sessions(request)

        if user_data:
            return render(request,'accounts/already_login.html', user_data)
        else:
            return render(request,'accounts/signup.html')

    # signup의 form 의 method가 POST방식이므로 sign up 버튼을 클릭시 POST방식의 HTTP request발생
    elif request.method == 'POST':
        # POST.get으로 가져오면 값이 없을경우 None을 저장해줌
        user_id = request.POST.get('user_id')
        user_name =request.POST.get('user_name')
        user_password1 = request.POST.get('password1')
        user_password2 = request.POST.get('password2')
        user_loct_state = request.POST.get('user_loct_state')
        user_loct_city = request.POST.get('user_loct_city')
        user_cert = ''

        res_data = {}

        # 값 입력을 확인하는 로직
        # 모든값을 입력하지 않으면 에러를 발생시키고 화면에 렌더링
        # 비밀번호1 과 비밀번호2가 일치하지 않으면 에러를 발생시키고 화면에 렌더링
        # 모든값이 입력되고 비밀번호가 일치하면 저장하고 모델에 입력후 save

        if not (user_id and user_name and user_password1 and user_password2):
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
       #이미 로그인이 되어있는지 확인
        user_data = check_sessions(request)

        if user_data:
            return render(request,'accounts/already_login.html', user_data)
        else:
            return render(request,'accounts/login.html')
    elif request.method == 'POST':
        userid = request.POST.get('user_id')
        password = request.POST.get('password')

        res_data = {}
        if not (userid and password):
            res_data['error'] = '모든 값을 입력해야합니다.'
        else:
            try:
                user = User.objects.get(user_id=userid)
                if check_password(password, user.user_pw):
                    request.session['user'] = user.user_id
                    # res_data['error']= '로그인 성공'

                    return redirect('/main')
                else:
                    res_data['error'] = '비밀번호가 틀렸습니다.'
            except:
                res_data['error'] = '존재하지 않는 아이디입니다.'

        return render(request, 'accounts/login.html', res_data)

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
        request.session.flush()
    return redirect('/main')


def mypage(request):
    # 맨처음 화면로드시 GET방식으로 통신
    if request.method == 'GET':
        #이미 로그인이 되어있는지 확인
        user_data = check_sessions(request)

        if user_data:
            return render(request,'accounts/mypage.html', user_data)
        else:
            return render(request,'accounts/no_user.html')

    # POST방식으로 
    elif request.method == 'POST':
        # POST.get으로 가져오면 값이 없을경우 None을 저장해줌
        user_id = request.session.get('user')
        users = User.objects.filter(user_id = user_id)
        context={}
        user_data = check_sessions(request)
        context['map'] = user_data['map']
        context['user_id'] = user_data['user_id']
        context['session_key'] = user_data['session_key']
        context['user_name'] = user_data['user_name']
        context['user_loct'] = user_data['user_loct']

        if request.POST.get('loct_ch'):
            for u in users:
                user_loct_state = request.POST.get('user_loct_state')
                user_loct_city = request.POST.get('user_loct_city')
                u.user_loct = user_loct_state + ' ' + user_loct_city
                u.save()
            return redirect('/main/')
        if request.POST.get('change'):
            for u in users:
                real_password = u.user_pw
                password1 = request.POST.get('password1')
                newpassword = request.POST.get('newpassword')
                newpassword2 = request.POST.get('newpassword2')
                if check_password(password1,real_password):
                    if newpassword == newpassword2:
                        u.user_pw = make_password(newpassword2)
                        u.save()
                        del(request.session['user'])
                        request.session.flush()
                        return redirect('/main/')
                    else:
                        context['error'] = '변경할 비밀번호가 서로 다릅니다.'
                        return render(request, 'accounts/mypage.html',context)
                else:
                    context['error'] = '기존 비밀번호 입력이 틀렸습니다.'
                    return render(request, 'accounts/mypage.html',context)
        if request.POST.get('delete'):
            for u in users:
                real_password = u.user_pw
            password1 = request.POST.get('password1')
            if check_password(password1,real_password):
                users.delete()
                del(request.session['user'])
                request.session.flush()
                return redirect('/main/')
            else:
                context['error'] = '기존 비밀번호 입력이 틀렸습니다.'
                return render(request, 'accounts/mypage.html',context)







