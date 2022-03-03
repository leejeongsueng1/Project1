from django.db import models

# Create your models here.

# 회원정보를 저장하는 모델 클래스 생성
# 회원정보의 각각 필드가 타입을 알려주므로 타입은 생략
# user_id : 유저 아이디, 정규식을 통해서 cert할 예정
# user_pw :  유저 비밀번호, 역시 정규식 비교를 통해 cert할 예정
# user_name : 유저 이름, 외국인 케이스를 고려해 max_length를 15로 설정
# user_cert : 유저 관리번호, 이 칼럼을 통해 등급을 고려할 예정
# user_loct : 유저 주소, 도/시,군 정도만 입력해 비교를 쉽게 할 예정
# 
class User(models.Model):

    user_id = models.CharField(max_length=30, verbose_name='유저 아이디')
    user_pw = models.CharField(max_length=128, verbose_name='유저 비밀번호')
    user_name = models.CharField(max_length=15, verbose_name='유저 이름')
    user_cert = models.CharField(max_length=12, unique=True, verbose_name='유저 관리번호' )
    user_loct = models.CharField(max_length=15, verbose_name='유저 주소')
    
    
    

    # 반환값을 self의 user_name으로 사용자 이름을 반환하도록 설정
    def __str__(self):
        return {'user_name':self.user_name, 'user_loct':self.user_loct, 'user_id':self.user_id}

    class Meta:
        # 테이블명 지정 옵션
        db_table = 'user'
        # 해당 테이블의 닉네임
        verbose_name = '유저'
        # 유저s와 같이 복수형 표시를 방지하기 위해서 verbose_name과 같이 설정해서 방지
        verbose_name_plural = '유저'




