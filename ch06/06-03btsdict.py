bts1={'그룹명': '방탄소년단', '인원수': 7, '리더': '김남준'}
bts1['소속사']='빅히트 엔터테인먼트';
print(bts1)
bts2=dict([['그룹명', '방탄소년단'], ['인원수', 7]])
print(bts2)
bts3=dict((('리더', '김남준'), ('소속사', '빅히트 엔터테인먼트')))
print(bts3)

bts=dict(그룹명='방탄소년단', 인원수=7, 리더='김남준', 소속사='빅히트 엔터테인먼트')
#구성원 추가
bts['구성원']=['RM', '진', '슈가', '제이홉', '지민', '뷔', '정국']

print(bts) #전체 출력
print(bts['구성원']) #구성원 출력
