import requests
import json

# TMDb API 키
api_key = '4df7ab026552454751d28aad32ea63aa'


### 데이터 새로 만들때 사용할 것

# # 가져올 페이지 수
# num_pages = 5

# # 각 페이지에서 가져올 결과 수
# results_per_page = 20

# # 영화 데이터를 저장할 리스트
# movie_data = []

# # 페이지 반복
# for page in range(1, num_pages + 1):
#     # TMDb API 엔드포인트 URL
#     url = 'https://api.themoviedb.org/3/movie/popular'

#     params = {
#         'api_key': '4df7ab026552454751d28aad32ea63aa',
#         'region': 'KR',
#         'language': 'ko',
#         'page': page
#     }

#     # 영화 정보 요청
#     response = requests.get(url, params=params)

#     # 요청이 성공했을 경우
#     if response.status_code == 200:
#         page_data = response.json()
#         results = page_data['results']

#         # 각 영화 결과를 리스트에 추가
#         movie_data.extend(results)

#         print(f"페이지 {page}의 영화 정보를 가져왔습니다.")
#     else:
#         print(f"페이지 {page}에서 영화 정보를 가져오는데 실패했습니다.")

###  ---끝---


 # 감독과 영화 배우 정보 가져오기


with open('movie_data_exam.json', 'r', encoding='UTF8') as f:

    movie_data = json.load(f)
print(movie_data)
print(type(movie_data))

director_data =list()
director_data_set=set()
cast_data=list()
cast_data_set=set()
for movie in movie_data:
    movie_id = movie['id']
    credits_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
    credits_params = {
        'api_key': api_key,
        'language':'ko',
    }
    credits_response = requests.get(credits_url, params=credits_params)

    if credits_response.status_code == 200:
        credits_data = credits_response.json()
        movie['director_id'] = [crew['id'] for crew in credits_data['crew'] if crew['job'] == 'Director']
        movie['cast_id'] = [cast['id'] for cast in credits_data['cast']]
        # director data를 추출
        for crew in credits_data['crew']:
            if crew['job']=='Director':
                if crew['id'] in director_data_set:
                    pass
                else:
                    director_data_set.add(crew['id'])
                    idx={'pk':crew['id'],'name':crew['name'],"profile_path":crew['profile_path']}
                    director_data.append(idx)
        # cast data를 추출
        for crew in credits_data['cast']:
            if crew['id'] in cast_data_set:
                pass
            else:
                cast_data_set.add(crew['id'])
                idx={'pk':crew['id'],'name':crew['name'],"profile_path":crew['profile_path'],"gender":crew['gender'] }
                cast_data.append(idx)
        # # 배우의 이름과 감독의 이름을 저장하는 것 (아래는)
        # movie['director'] = [crew['name'] for crew in credits_data['crew'] if crew['job'] == 'Director']
        # movie['cast'] = [cast['name'] for cast in credits_data['cast']]

# 영화 데이터를 JSON 파일로 저장
with open('movie_data_detail_test.json', 'w', encoding='utf-8') as file:
    json.dump(movie_data, file, indent=4, ensure_ascii=False)

print("영화 정보가 성공적으로 저장되었습니다.")

# with open('movie_data_credits_test.json', 'w', encoding='utf-8') as file:
#     json.dump(credits_response.json(), file, indent=4, ensure_ascii=False)

# 감독 데이터를 JSON 파일로 저장
with open('movie_data_director_test.json', 'w', encoding='utf-8') as file:
    json.dump(director_data, file, indent=4, ensure_ascii=False)

print("감독 정보가 성공적으로 저장되었습니다.")

# 배우 데이터를 JSON 파일로 저장
with open('movie_data_cast_test.json', 'w', encoding='utf-8') as file:
    json.dump(cast_data, file, indent=4, ensure_ascii=False)

print("배우 정보가 성공적으로 저장되었습니다.")