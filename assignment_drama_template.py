# ==========================
# assignment_drama_template.py (학생용 템플릿)
# 조건: 함수/조건문/반복문 금지. 변수 선언과 input(), print()만 사용.
# ==========================

drama1 = {
    "제목": "폭싹속았수다",            
    "장르": "로맨스 드라마",            
    "주제": "제주 바닷가 작은 마을을 배경으로 세월을 뛰어넘어 피어나는 사랑 이야기.",            
    "방영기간": "2025-03-07 ~ 2025-03-28",         
    "배우": ["아이유", "박보검"],            
    "명대사": "\"학~씨!\""           
}

drama2 = {
    "제목": "부부의세계",            
    "장르": "막장",           
    "주제": "사랑이라고 믿었던 부부의 연이 배신으로 끊어지면서 복수의 소용돌이에 빠지는 이야기",            
    "방영기간": "2020-03-27~2020-05-16",         
    "배우": ["김희애", "박해준"],            
    "명대사": "\"사랑에_빠진게_죄는_아니잖아!\""  
}

new_title = input("새 드라마 제목: ")  

new_genre = input("새 드라마 장르: ")                          
new_theme = input("새 드라마 주제: ")                          
new_period = input("새 드라마 방영기간(ex : 2024-00-00): ")                         
new_actors_input = input("새 드라마 배우들(쉼표구분): ")                   
new_quote_raw = input("인상적인 명대사(따옴표없이): ")                      

new_actors = new_actors_input.split(",")
new_quote = f"\"{new_quote_raw}\""

drama3 = {
    "제목": new_title,
    "장르": new_genre,
    "주제": new_theme,
    "방영기간": new_period,
    "배우": new_actors,
    "명대사": new_quote
}


upd_title = input("수정(덮어쓰기)할 제목(대상: drama2): ")  
upd_genre = input("수정할 장르: ")       
upd_theme = input("수정할 주제: ")                         
upd_period = input("수정할 방영기간(ex : 2024-00-00): ")                        
upd_actors_input = input("수정할 배우들(쉼표구분): ")                  
upd_quote_raw = input("수정할 인상적인 명대사(따옴표없이): ")                     

upd_actors = upd_actors_input.split(",")
upd_quote = f"\"{upd_quote_raw}\""

drama2["제목"] = upd_title
drama2["장르"] = upd_genre
drama2["주제"] = upd_theme
drama2["방영기간"] = upd_period
drama2["배우"] = upd_actors
drama2["명대사"] = upd_quote

print("\n[드라마 1]")
print(f"제목: {drama1['제목']}")
print(f"장르: {drama1['장르']}")
print(f"주제: {drama1['주제']}")
print(f"방영기간: {drama1['방영기간']}")
print(f"배우: {drama1['배우']}")
print(f"명대사: {drama1['명대사']}")

print("\n[드라마 2]  # 수정 후")
print(f"제목: {drama2['제목']}")
print(f"장르: {drama2['장르']}")
print(f"주제: {drama2['주제']}")
print(f"방영기간: {drama2['방영기간']}")
print(f"배우: {drama2['배우']}")
print(f"명대사: {drama2['명대사']}")

print("\n[드라마 3]  # 새로 추가")
print(f"제목: {drama3['제목']}")
print(f"장르: {drama3['장르']}")
print(f"주제: {drama3['주제']}")
print(f"방영기간: {drama3['방영기간']}")
print(f"배우: {drama3['배우']}")
print(f"명대사: {drama3['명대사']}")
