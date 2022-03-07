from django.shortcuts import render, redirect
from accounts.models import User
import pymysql
import pandas as pd
from sqlalchemy import create_engine, text
from django.http import HttpResponse


#-----------------custom python logic-------------------------------


def load_db_connection():
    ## DB connection
    #Connetion info
    DB_user = 'bigdata'
    DB_pw = 'Bigdata123!!'
    host = '127.0.0.1'
    port = '3306'
    DB_name = 'project1'

    engine = create_engine(f'mysql+pymysql://{DB_user}:{DB_pw}@{host}:{port}/{DB_name}')
    conn = engine.connect()
    return conn



def load_data(stmt,conn):
    data = pd.read_sql(text(stmt),conn)
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
    loct_data = {'ct_name' : ct_name_list,
                'ct_loct' : ct_loct,
                'ct_tel' : ct_tel,
                'ct_lat' : ct_lat,
                'ct_lon' : ct_lon,
                'ct_info1' : ct_info1,
                'ct_info2' : ct_info2,
                'ct_info3' : ct_info3,
                'ct_info4' : ct_info4,
                'ct_info5' : ct_info5}
    return loct_data



def check_sessions(request):
    session_id = request.session.session_key
    # 만약 세션이 부여되면
    if  session_id:
        #모델에서 유저 아이디를 불러옴
        user_id = request.session.get('user')
        users = User.objects.filter(user_id = user_id)
        #유저정보 로딩
        for u in users:
            user_name = u.user_name
            user_loct = u.user_loct
        user_data = { 'map': 'map',
                'user_id': user_id,
                'session_key':session_id,
                'user_name': user_name,
                'user_loct':user_loct}
        
        return user_data
    else:
        return None

        

