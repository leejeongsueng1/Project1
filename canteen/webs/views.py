from django.shortcuts import render, redirect
from accounts.models import User
import pymysql
import pandas as pd
from sqlalchemy import create_engine, text
from django.http import HttpResponse
from .loadingContext import *

## DB connection
#Connetion info
DB_user = 'bigdata'
DB_pw = 'Bigdata123!!'
host = '192.168.56.101'
port = '3306'
DB_name = 'project1'

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
        data = load_data(stmt,conn)
        
        return render(request,'map.html',data)
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

    
