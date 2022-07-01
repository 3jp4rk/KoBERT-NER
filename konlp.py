txt ="""파리 소리 들린다.
여기다, 여기! 이~!
정말? 어디. 저기다, 저기!
이~이얍, 이얍, 이얍!
여기인가? 이~ 얍! 얍!
"""


txt = "밥 먹고싶다 근데 너는 어디서 뭐하다 이제와 미쳤냐"

# import kss
# print("------KSS-----")
# sents = kss.split_sentences(txt)
# for index, sent in enumerate(sents):
#     print(index, sent)


from konlpy.tag import Kkma
print("------Kkma-----")
sents = Kkma().sentences(txt)
for index, sent in enumerate(sents):
    print(index, sent)