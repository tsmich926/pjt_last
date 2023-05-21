# 사용방법

# requirements.txt 로 모듈 설치
pip install -r requirements.txt

# DB생성
python manage.py makemigrations
python manage.py migrate

# 데이터 로드
python manage.py loaddata movies/actors.json movies/movies.json movies/directors.json movies/genres.json



