from konlpy.tag import Kkma
from konlpy.tag import Twitter
import requests
from tts import make_tts

from bs4 import BeautifulSoup
import re

def all_list():
  all_list = {'food': ['가락지빵',
  '가래떡',
  '가루우유',
  '가지나물',
  '간고등어',
  '간장',
  '갈비',
  '갈비탕',
  '감자튀기',
  '감자튀김',
  '강정',
  '개장',
  '건빵',
  '경편',
  '계란',
  '계란덮밥',
  '계란말이',
  '고기',
  '고기겹빵',
  '고량주',
  '고로케',
  '고추가루',
  '고추장',
  '고춧가루',
  '곤밥',
  '골동반',
  '곰',
  '곰국',
  '공갈빵',
  '과자',
  '광동요리',
  '구멍국수',
  '구야시',
  '국',
  '국물',
  '국밥',
  '국수',
  '국수발',
  '국수오리',
  '국숫발',
  '규돈',
  '기름밥',
  '기름사탕',
  '김',
  '김밥',
  '김초밥',
  '김치',
  '김치찌개',
  '까까',
  '껌',
  '꼬부랑국수',
  '꿀',
  '꿀타래',
  '꿔바로우',
  '나박김치',
  '날김치',
  '날맥주',
  '냉면',
  '녹차',
  '단디',
  '단맛감',
  '단무지',
  '단물얼음',
  '단얼음',
  '달걀',
  '달걀덮밥',
  '달걀말이',
  '닭갈비',
  '닭강정',
  '닭개장',
  '닭고기',
  '닭고기덮밥',
  '닭꼬치',
  '닭튀김',
  '대굿국',
  '덮밥',
  '도넛',
  '돈가스',
  '동치미',
  '돼지고기',
  '된장',
  '된장찌개',
  '두부',
  '디저트',
  '땅콩과자',
  '떡',
  '떡국',
  '떡꼬치',
  '떡볶이',
  '뜨더국',
  '라면',
  '라바슈',
  '라볶이',
  '레모네이드',
  '레몬수',
  '마가린',
  '마른반찬',
  '마른오징어',
  '마멀레이드',
  '마요네즈',
  '마카로니',
  '마키',
  '마파두부',
  '막걸리',
  '막대사탕',
  '만두',
  '만두기',
  '맘마',
  '맥주',
  '머스터드',
  '머스터드소스',
  '면발',
  '묵',
  '미숫가루',
  '미음',
  '밀가루',
  '밀국수',
  '밀크커피',
  '바게트',
  '바비큐',
  '바삭과자',
  '박고지',
  '밥',
  '밥감주',
  '배추김치',
  '배춧국',
  '백설탕',
  '백포도주',
  '버터',
  '보드카',
  '보르시',
  '보리밥',
  '보리차',
  '보신탕',
  '보쌈김치',
  '볶음밥',
  '부대찌개',
  '부침개',
  '분유',
  '분탕',
  '불고기',
  '브랜디',
  '블랙커피',
  '비빔',
  '비빔밥',
  '빙수',
  '빠다',
  '빵',
  '삐짜',
  '사이다',
  '사탕',
  '사탕가루',
  '삼겹살',
  '삼계탕',
  '삼두음',
  '삼정과',
  '삼합미음',
  '새우튀김',
  '샌드위치',
  '샐러드',
  '생강주',
  '생강즙',
  '생강차',
  '생김치',
  '생맥주',
  '생선묵',
  '생선전',
  '생선회',
  '생황장',
  '샤실리크',
  '샴팡',
  '샴페인',
  '석식',
  '설탕',
  '셔벗',
  '셰이크',
  '소갈비',
  '소금',
  '소만두',
  '소맥',
  '소면',
  '소불고기',
  '소시지',
  '소젖',
  '소주',
  '송편',
  '송화다식',
  '송화밀수',
  '쇠고기',
  '쇠고기덮밥',
  '수란',
  '수프',
  '순대',
  '순두부찌개',
  '술',
  '스시',
  '스테이크',
  '스파게티',
  '식빵',
  '식초',
  '식품',
  '식혜',
  '쌀',
  '쌀떡',
  '쌀라드',
  '쌈',
  '썩장',
  '아욱국',
  '아이스커피',
  '아이스크림',
  '알찌개',
  '알코올음료',
  '알탕',
  '압생트',
  '애기젖가루',
  '야구르트',
  '약과',
  '양갱',
  '양고기',
  '양로쵈',
  '양식',
  '양장피',
  '어묵',
  '얼럭밥',
  '얼음보숭이',
  '에스프레소',
  '염소젖',
  '염장',
  '엿',
  '오렌지주스',
  '오리알',
  '오미자차',
  '오색경단',
  '오크로시카',
  '옥수수빵',
  '올리브유',
  '와사비',
  '와인',
  '요구르트',
  '우동',
  '우유',
  '위스키',
  '유부',
  '육개장',
  '육회',
  '이크라',
  '인삼차',
  '인절미',
  '일식',
  '자장면',
  '잡채',
  '잡탕밥',
  '장어덮밥',
  '잼',
  '적',
  '적포도주',
  '젓갈',
  '젖가공품',
  '조미료',
  '조식',
  '주스',
  '죽',
  '중식',
  '쥐포',
  '즉석요리',
  '지지개',
  '짜장면',
  '짬뽕',
  '쨈',
  '찐빵',
  '차',
  '찰밥',
  '청국장',
  '초밥',
  '초콜릿',
  '총각김치',
  '추탕',
  '치즈',
  '치킨',
  '카레',
  '칵테일',
  '칼국',
  '칼국수',
  '캐비어',
  '커피',
  '컵라면',
  '케이크',
  '코코아',
  '콜라',
  '콩밥',
  '콩우유',
  '콩자반',
  '쿠키',
  '크래커',
  '크루아상',
  '크림',
  '타래떡',
  '탕수육',
  '토스트',
  '통구이',
  '통닭',
  '튀기',
  '튀김',
  '트르들로',
  '파김치',
  '파메산',
  '파스타',
  '파전',
  '팔보채',
  '팬케이크',
  '펠메니',
  '편',
  '포도주',
  '폭탄주',
  '푸딩',
  '푸른차',
  '풍선껌',
  '프라이드치킨',
  '플로프',
  '피자',
  '피짜',
  '필라프',
  '한식',
  '핫도그',
  '해산물',
  '햄버거',
  '호떡',
  '홍차',
  '회',
  '회덮밥',
  '흑설탕',
  '희아리'],
 'taste': ['달곰하다',
  '달콤하다',
  '달달하다',
  '있다달콤하다',
  '들큼하다',
  '달큼하다',
  '달짝지근하다',
  '감미롭다',
  '달보드레하다',
  '달곰쌉쌀하다',
  '달곰삼삼하다',
  '달곰씁쓸하다',
  '달콤새콤하다',
  '달곰새금하다',
  '들부드레하다',
  '달착지근하다',
  '들쩍지근하다',
  '있다들척지근하다',
  '들큼하다',
  '달다새큼달큼하다',
  '맵다',
  '맵디맵다',
  '매콤하다',
  '매큼하다',
  '맵싸하다',
  '맵짜다',
  '매옴하다',
  '매움하다',
  '신랄하다',
  '얼큰하다',
  '아리다',
  '아릿하다',
  '알알하다',
  '알싸하다',
  '칼칼하다',
  '짭짤하다',
  '찝찔하다',
  '간간하다',
  '건건하다',
  '짐짐하다',
  '시다',
  '시디시다',
  '시지근하다',
  '새곰하다',
  '있다새금하다',
  '새콤하다',
  '새큼하다',
  '시금하다',
  '시다시금시금',
  '시큼시큼',
  '느낌새척지근하다',
  '시다시척지근하다',
  '새곰새곰',
  '느낌새금새금',
  '새콤달콤하다',
  '새콤새콤',
  '새콤새콤하다',
  '새큼새큼',
  '쓰다',
  '쓰디쓰다',
  '쌉쌀하다',
  '씁쓰름하다',
  '씁쓰레하다',
  '쌉싸래하다',
  '떨떠름하다',
  '떠름하다',
  '삽삽하다',
  '싱겁다',
  '밍밍하다',
  '맹맹하다',
  '덤덤하다',
  '심심하다',
  '삼삼하다',
  '있다개심심하다',
  '슴슴하다',
  '비리다',
  '비릿하다',
  '비리척지근하다',
  '노리다',
  '누리다',
  '노릿하다',
  '누릿하다',
  '고리다',
  '고릿하다',
  '꾀리하다',
  '고다',
  '구스다',
  '고소하다',
  '구뜰하다',
  '구수하다',
  '엇구뜰하다',
  '엇구수하다',
  '어꾸수하다',
  '꼬소롬하다',
  '담백하다',
  '산뜻하다시원하다',
  '담담하다',
  '개운하다',
  '상큼하다',
  '맛깔스럽다',
  '사근사근하다',
  '있다',
  '나다',
  '바특하다',
  '바따라지다',
  '배틀하다',
  '있다비틀하다',
  '삼빡하다',
  '느끼하다',
  '닝닝하다',
  '타분하다',
  '탑탑하다',
  '모름하다',
  '텁지근하다']}
  return all_list


def tagging(input):
    t = Twitter()
    pos = t.pos(input)
    vaild = [p[0] for p in pos if p[1]=='Noun' or p[1]=='Verb']
    rtn = {}
    rtn['food'] = []; rtn['taste'] = []
    for v in vaild:
        for k in all_list().keys():
            for l in all_list().get(k):
                if v in l:
                    rtn[k] = v
    return rtn

def get_recipe(food):
    r = requests.get("http://www.10000recipe.com/recipe/list.html?q="+food)
    s = BeautifulSoup(r.content,"html.parser")
    food_list = s.find("div",{"class":"col-xs-4"}).find("a", {"class":"thumbnail"})['href']
    r = requests.get('http://www.10000recipe.com/'+food_list)
    print('http://www.10000recipe.com/'+food_list)
    s = BeautifulSoup(r.content,"html.parser")
    i = s.find("div",{"class":"ready_ingre3"})
    li = i.findAll("li")
    rtn = [l.text.replace('                                                ',' ').replace('\n','') for l in li]
    rtn = ' '.join(rtn)
    #print(str(rtn[0]))
    make_tts(str(rtn))
    print("=================end in get_recipe")
    return str(rtn)  

def get_recipe2(food):
    r = requests.get("http://www.10000recipe.com/recipe/list.html?q="+food)
    s = BeautifulSoup(r.content,"html.parser")
    food_list = s.find("div",{"class":"col-xs-4"}).find("a", {"class":"thumbnail"})['href']
    r = requests.get('http://www.10000recipe.com/'+food_list)
    s = BeautifulSoup(r.content,"html.parser")
    aa = s.find_all("div",{"class":"view_step"})[0]
    t=aa.find_all('div', id=re.compile('^stepDiv'))
    p = [f.text for f in t]
    recip=[l.replace('\n','') for l in p]
    #print(str(recip[0]))
    recip = ' '.join(recip)
    make_tts(str(recip))
    print("================end in get_recipe2")
    return str(recip)