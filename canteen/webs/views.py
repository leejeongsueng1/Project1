from django.shortcuts import render, redirect
from accounts.models import User
import pymysql
import pandas as pd
from sqlalchemy import create_engine, text
from django.http import HttpResponse


## DB connection
#Connetion info
DB_user = 'bigdata2'
DB_pw = 'Bigdata123!!'
host = '192.168.56.101'
port = '3306'
DB_name = 'project1'

# Create your views here.


#메인 인덱스 페이지 호출
def index(request):
    # 세션키를 통해 유저아이디 탐색
    session_id = request.session.session_key
    print('1')
    user_id = request.session.get('user')
    try:
        users = User.objects.filter(user_id = user_id)
        for u in users:
            user_name = u.user_name 
            user_loct = u.user_loct
        context = { 'map': 'map',
                    'user_id': user_id,
                    'session_key':session_id,
                    'user_name': user_name,
                    'user_loct':user_loct}
        print(context)
        return render(request,'main.html', context)
    except:
        users = None
        context = {'map':'map2'}
    return render(request,'main.html',context)
    
# 맵 렌더링시키는 함수
def map(request):
    
    #----------------사용자 세션확인---------------------
    session_id = request.session.session_key
    user_id = request.session.get('user')
    # try:
    #사용자가 존재할 때 사용자의 등록 거주지 정보를 기반으로 marker생성정보를 만들고 context에 저장
    try:
        
        users = User.objects.filter(user_id = user_id)
        for u in users:
            user_name = u.user_name
            user_loct = u.user_loct
        stmt = f"SELECT * FROM canteenu WHERE 소재지도로명주소 LIKE '%{user_loct}%'; "

        #DB연결
        engine = create_engine(f'mysql+pymysql://{DB_user}:{DB_pw}@{host}:{port}/{DB_name}')
        conn = engine.connect()
        data = pd.read_sql(text(stmt), conn)
        

        # 데이터 선택 로직
        ct_name = data.drop(['소재지도로명주소', '소재지지번주소', '운영기관명', '전화번호', '급식장소', '급식대상', '급식시간','급식요일', '운영시작일자', '운영종료일자', '위도', '경도', '데이터기준일자', '제공기관코드', '제공기관명'],axis=1 )
        ct_name = ct_name.loc[:,:].values.tolist()
        ct_name_list = []
        for i in ct_name:
            ct_name_list.append(i[0])

        # 데이터 프레임을 리스트로 변환
        ct_loct = data['소재지도로명주소']
        ct_loct = ct_loct.to_list()
        ct_tel = data['전화번호']
        ct_tel = ct_tel.to_list()
        ct_lat = data['위도']
        ct_lat = ct_lat.to_list()
        ct_lon = data['경도']
        ct_lon = ct_lon.to_list()
        ct_info1 = data['급식대상']
        ct_info1 = ct_info1.to_list()
        ct_info2 = data['급식시간']
        ct_info2 = ct_info2.to_list()
        ct_info3 = data['급식요일']
        ct_info3 = ct_info3.to_list()
        ct_info4 = data['운영종료일자']
        ct_info4 = ct_info4.to_list()
        ct_info5 = data['제공기관명']
        ct_info5 = ct_info5.to_list()

        #딕셔너리로 context생성후 전달
        context = {'ct_name' : ct_name_list,
                    'ct_loct' : ct_loct,
                    'ct_tel' : ct_tel,
                    'ct_lat' : ct_lat,
                    'ct_lon' : ct_lon,
                    'ct_info1' : ct_info1,
                    'ct_info2' : ct_info2,
                    'ct_info3' : ct_info3,
                    'ct_info4' : ct_info4,
                    'ct_info5' : ct_info5}
        return render(request,'map.html', context)
    # except:
    #사용자가 존재하지 않으면 빈맵을 rendering
    except:
        return render(request,'map2.html')



def map2(request):
    
    #----------------사용자 세션확인---------------------
    session_id = request.session.session_key
    user_id = request.session.get('user')
    try:
        state = request.GET['user_loct_state']
        city = request.GET['user_loct_city']
        loct = state + ' ' + city
        stmt = f"SELECT * FROM canteenu WHERE 소재지도로명주소 LIKE '%{loct}%'; "

        #DB연결
        engine = create_engine(f'mysql+pymysql://{DB_user}:{DB_pw}@{host}:{port}/{DB_name}')
        conn = engine.connect()
        data = pd.read_sql(text(stmt), conn)
        

        # 데이터 선택 로직
        ct_name = data.drop(['소재지도로명주소', '소재지지번주소', '운영기관명', '전화번호', '급식장소', '급식대상', '급식시간','급식요일', '운영시작일자', '운영종료일자', '위도', '경도', '데이터기준일자', '제공기관코드', '제공기관명'],axis=1 )
        ct_name = ct_name.loc[:,:].values.tolist()
        ct_name_list = []
        for i in ct_name:
            ct_name_list.append(i[0])

        # 데이터 프레임을 리스트로 변환
        ct_loct = data['소재지도로명주소']
        ct_loct = ct_loct.to_list()

        ct_tel = data['전화번호']
        ct_tel = ct_tel.to_list()
        ct_lat = data['위도']
        ct_lat = ct_lat.to_list()
        ct_lon = data['경도']
        ct_lon = ct_lon.to_list()
        ct_info1 = data['급식대상']
        ct_info1 = ct_info1.to_list()
        ct_info2 = data['급식시간']
        ct_info2 = ct_info2.to_list()
        ct_info3 = data['급식요일']
        ct_info3 = ct_info3.to_list()
        ct_info4 = data['운영종료일자']
        ct_info4 = ct_info4.to_list()
        ct_info5 = data['제공기관명']
        ct_info5 = ct_info5.to_list()
        
        #딕셔너리로 context생성후 전달
        context = {'ct_name' : ct_name_list,
                    'ct_loct' : ct_loct,
                    'ct_tel' : ct_tel,
                    'ct_lat' : ct_lat,
                    'ct_lon' : ct_lon,
                    'ct_info1' : ct_info1,
                    'ct_info2' : ct_info2,
                    'ct_info3' : ct_info3,
                    'ct_info4' : ct_info4,
                    'ct_info5' : ct_info5}
        print(context)
        
        return render(request,'map.html',context)
    except:
        return render(request,'map2.html')
        


def about_us(request):
    #----------------사용자 세션확인---------------------
    session_id = request.session.session_key
    user_id = request.session.get('user')

    try:
        users = User.objects.filter(user_id = user_id)
        for u in users:
            user_name = u.user_name 
            user_loct = u.user_loct
        context = {'user_id':user_id,
                    'session_key':session_id,
                    'user_name': user_name,
                    'user_loct':user_loct}
        return render(request,'about_us.html', context)
    except:
        users = None
    
    return render(request,'about_us.html')


def dashboard(request):
    #----------------사용자 세션확인---------------------
    session_id = request.session.session_key
    user_id = request.session.get('user')

    try:
        users = User.objects.filter(user_id = user_id)
        for u in users:
            user_name = u.user_name 
            user_loct = u.user_loct
        context = {'user_id':user_id,
                    'session_key':session_id,
                    'user_name': user_name,
                    'user_loct':user_loct}
        return render(request,'dashboard.html', context)
    except:
        users = None
    
    return render(request,'dashboard.html')

    
