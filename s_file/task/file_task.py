# 파일의 단어의 빈도수 구하기

# alice.txt

# 오로지 알파벳만 검사하기
# 대소문자 구문없이 비교
# 글자수 2개 이상인 단어만 카운트 하기
# 빈도수 100회 이상인 단어만 카운트


# def


alice = open("alice.txt", "r", encoding="utf-8")

word_count = {}
for line in alice.readlines():
    word_with_space = ""
    for letter in line.strip().upper():

        if 'A' <= letter <= 'Z':

            word_with_space += letter
        else:

            word_with_space += " "

    words = word_with_space.split(" ")

    for word in words:

        if word.__len__() < 2:
            continue
        else:
            if word in word_count.keys():
                word_count[word] = word_count[word] + 1
            else:
                word_count[word] = 1

#100회 이상인 단어 추출
word_count_gt_100 = {}

for word, count in word_count.items():
    if count >= 100:
        word_count_gt_100[word] = count



#카운트 많은 순서대로 정렬
values = list(set(list(word_count_gt_100.values())))
values.sort(reverse=True)

#중복제거


word_count_gt_100_sorted ={}


for count in values:
    for word,real_count in word_count_gt_100.items():
        if count == real_count:
            word_count_gt_100_sorted[word] = count


print(word_count_gt_100_sorted)

alice.close()

"""
[출력예]
the 1642
and 872
to 729
it 595
she 553
of 514
said 462
you 411
alice 398
in 369
...
"""
