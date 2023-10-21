# 조건 : 2022년 4월 13일 취소되지 않은 CS 진료 예약 내역
# 레코드 : apnt_no(a), pt_name(p), pt_no(p), mcdp_cd(a), dr_name(d), apnt_ymd(a)

# SELECT a_d.apnt_no, p.pt_name, p.pt_no, a_d.mcdp_cd, a_d.dr_name, a_d.apnt_ymd 
#     FROM (SELECT a.apnt_no, a.pt_no, a.mcdp_cd, a.apnt_ymd, dr_name
#         FROM (SELECT apnt_no, pt_no, mcdp_cd, apnt_ymd, mddr_id
#               FROM appointment
#               WHERE apnt_ymd LIKE '2022-04-13%' AND mcdp_cd = 'CS' AND apnt_cncl_yn = 'N') a
#         LEFT OUTER JOIN doctor d
#                      ON a.mddr_id = d.dr_id) a_d
#     LEFT OUTER JOIN patient p
#                  ON a_d.pt_no = p.pt_no
#     ORDER BY a_d.apnt_ymd DESC;













# # JOIN KEY : p.pt_no = a.pt_no / a.mddr_id = d.dr_id
# # 문제 조건
# 1) 2022-04-13 : a.apnt_ymd LIKE '2022-04-13%'
# 2) 취소되지않은 : a.apnt_cncl_yn = 'N'
# 3) 흉부외과(CS) : a.mcdp_cd = 'CS'
# 4) 출력 : a.apnt_no 진료예약번호, p.pt_name 환자이름, p.pt_no 환자번호,
#          a.mcdp_cd 진료과코드, d.dr_name 의사이름, a.apnt_ymd 진료예약일시
SELECT ad.apnt_no 진료예약번호, p.pt_name 환자이름, p.pt_no 환자번호,
       ad.mcdp_cd 진료과코드, ad.dr_name 의사이름, ad.apnt_ymd 진료예약일시
  FROM patient p
  INNER JOIN (SELECT a.apnt_ymd, a.apnt_no, a.pt_no, a.mcdp_cd,
                     a.apnt_cncl_yn, a.apnt_cncl_ymd, d.dr_name
                FROM appointment a
                INNER JOIN doctor d
                        ON a.mddr_id = d.dr_id) ad
          ON p.pt_no = ad.pt_no
  WHERE ad.apnt_ymd LIKE '2022-04-13%' AND
        ad.apnt_cncl_yn = 'N' AND
        ad.mcdp_cd = 'CS'
  ORDER BY 진료예약일시;