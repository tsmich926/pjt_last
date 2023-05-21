import json

# with open('movie_data_credits_test.json', 'r', encoding='UTF8') as f:

#     json_data = json.load(f)
# print(json_data)
# print(type(json_data))
# genreset=set()
# for i in json_data:
#     # print(i.get('genre_ids'))
#     genreset.update(tuple(i.get('genre_ids')))
#     print()
# print(genreset)
# aaaa=dict()

# sample_dict = {
#     '수학':80,
#     '국어':90, 
#     '영어':95
# }
# aaaa['fields']=sample_dict
# print(aaaa)
# print(sample_dict)
 
# del sample_dict['영어']
# print(sample_dict)

with open('genre_base.json', 'r', encoding='UTF8') as f:

    json_data = json.load(f)

genre_data=list()
cast_data_set=set()
for genre in json_data['genres']:
    # print(genre)
    # genre_idx={'model':"movies.genre",'pk':genre['id']}
    # genre_idx['fields']={'name':genre['name']}
    genre_data.append({'model':"movies.genre",'pk':genre['id'],'fields':{'name':genre['name']}})
    print("############")
    print(genre_data)

with open('genres.json', 'w', encoding='utf-8') as file:
    json.dump(genre_data, file, indent=4, ensure_ascii=False)