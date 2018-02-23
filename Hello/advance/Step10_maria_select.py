#-*- coding:utf-8 -*-

import mysql.connector

# DB 접속 정보를 dict type 으로 준비한다.
config={
        'user':'root',      # 계정
        'password':'maria', # password
        'host':'127.0.0.1', # ip 주소
        'database':'mingu', # database 명
        'port':3306         # 기본적 3306 maria,mysql 
    }

if __name__ == '__main__':
    
    try:
        # Maria DB 연결 객체
        conn=mysql.connector.connect(**config) # dict type 을 풀어서 전달
        
        # PreparedStatement <= jdbc (java)
        # query 문을 수행해줄 객체
        cursor=conn.cursor() # Python
        
        # SELECT 된 row 하나당 tuple 1개 생성  / row 갯수만큼 tuple생성
        # 실행할 query 문
        # sql="SELECT num,name,addr FROM member ORDER BY num DESC"
        
        # sql 문을 여러줄로 표현하고싶을때
        sql="""
              SELECT num,name,addr 
              FROM member 
              WHERE num=%s
              ORDER BY num DESC
        """           # 주석이아닌 문자열로 인식함
        
        # query 문 수행
        cursor.execute(sql, (2,))
        
        # fetchall() 하면 tuple 이 순서대로 들어 있는 list 이다.
        result=cursor.fetchall() # result <=> ResultSet(java)
        
        for tmp in result :
            num=tmp[0] # query 문 순서 num,name,addr 잘보셈
            name=tmp[1]
            addr=tmp[2]
            print u"번호 :{} 이름:{}  주소:{}"\
                .format(num, name, addr)
    
    except Exception, e:
        print e
    finally:
        conn.close()
    
    
    
    print " 메인 메소드가 종료 됩니다. "