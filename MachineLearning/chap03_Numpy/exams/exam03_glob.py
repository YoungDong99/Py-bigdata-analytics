'''
문3) ~/data/numpy 폴더에 포함된 전체 텍스트 파일(*.txt)을 읽어서 리스트에 저장하시오. 


    <힌트> text 파일 읽기 형식 
    file = open(file, mode='r', encoding='utf-8') 
'''


from glob import glob # 파일 검색 패턴 사용

# text file 경로 
path = r"C:\ITWILL\5_Python_ML\data\numpy" # 파일 기본 경로 


full_text = [] # 텍스트 저장 list 

for file in glob(path + '/*.txt') :
    #print(file) : text 파일 경로
    f = open(file, mode='r', encoding='utf-8')  # file 객체
    data = f.read()  # text 전체 읽기
    full_text.append(data)
    f.close()

print(full_text)
len(full_text) # 3





