from django.shortcuts import render, redirect
from accounts.models import User
from .loadingContext import *
from .graph import *

# Create your views here.


#메인 인덱스 페이지 호출
def index(request):
    
    # 세션키를 통해 유저아이디 탐색
    user_data = check_sessions(request)

    if user_data:
        return render(request,'main.html', user_data)
    else:
        context = {'map':'map2'}
    return render(request,'main.html',context)
    
# 맵 렌더링시키는 함수
def map(request):
    
    #----------------사용자 세션확인---------------------
    user_data = check_sessions(request)
    # try:
    #사용자가 존재할 때 사용자의 등록 거주지 정보를 기반으로 marker생성정보를 만들고 context에 저장
    if user_data:
        stmt = f"SELECT * FROM canteenu WHERE 소재지도로명주소 LIKE '%{user_data['user_loct']}%'; "

        #DB연결
        conn = load_db_connection()
        data = load_data(stmt,conn)

        return render(request,'map.html', data)
    # except:
    #사용자가 존재하지 않으면 빈맵을 rendering
    else:
        return render(request,'map2.html')



def map2(request):
    
    try:
        state = request.GET['user_loct_state']
        city = request.GET['user_loct_city']
        loct = state + ' ' + city
        stmt = f"SELECT * FROM canteenu WHERE 소재지도로명주소 LIKE '%{loct}%'; "

        #DB연결
        conn = load_db_connection()
        if load_data(stmt,conn):
            data = load_data(stmt,conn)
            
            return render(request,'map.html',data)
        else:
            return render(request,'map2.html')
    except:
        return render(request,'map2.html')
        


def about_us(request):
    #----------------사용자 세션확인---------------------
    user_data = check_sessions(request)

    if user_data:
        return render(request,'about_us.html', user_data)
    else:
        return render(request,'about_us.html')


def dashboard(request):
    #----------------사용자 세션확인---------------------
    user_data = check_sessions(request)

    if user_data:
        return render(request,'dashboard.html', user_data)
    else:
        return render(request,'dashboard.html')


def graph(request):
    user_data = check_sessions(request)
    try:
        print(request)
        state = request.GET.get('user_loct_state')
        print('A')
        print(state)
        city = request.GET.get('user_loct_city')
        print('B')
        print(city)
        loct = state + ' ' + city
        print('C')
        draw_graph(loct)
        print('D')
        return render(request,'graph.html')
    except:
        try:
            print('E')
            loct = user_data['user_loct']
            print('F')
            #DB연결
            draw_graph(loct)
            print('G')
            return render(request,'graph.html')
        except:
            print('H')
            loct = "서울특별시 금천구"
            draw_graph(loct)
            return render(request,'graph.html')

 
        

    
