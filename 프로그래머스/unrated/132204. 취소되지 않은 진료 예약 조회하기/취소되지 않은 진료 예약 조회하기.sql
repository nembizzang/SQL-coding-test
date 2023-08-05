# JOIN KEY : p.pt_no = a.pt_no / a.mddr_id = d.dr_id AND a.mcdp_cd = d.mcdp_cd
# 문제 조건
# 1) 2022-04-13 : a.apnt_ymd LIKE '2022-04-13%'
# 2) 취소되지않은 : a.apnt_cncl_yn = 'N'
# 3) 흉부외과(CS) : a.mcdp_cd = 'CS'
# 4) 출력 : a.apnt_no 진료예약번호, p.pt_name 환자이름, p.pt_no 환자번호,
#          a.mcdp_cd 진료과코드, d.dr_name 의사이름, a.apnt_ymd 진료예약일시
SELECT ad.apnt_no 진료예약번호, p.pt_name 환자이름, p.pt_no 환자번호,
       ad.mcdp_cd 진료과코드, ad.dr_name 의사이름, ad.apnt_ymd 진료예약일시
  FROM patient p
  INNER JOIN (SELECT a.apnt_ymd, a.apnt_no, a.pt_no, a.mcdp_cd, a.mddr_id,
                     a.apnt_cncl_yn, a.apnt_cncl_ymd, d.dr_name
                FROM appointment a
                INNER JOIN doctor d
                        ON a.mddr_id = d.dr_id AND a.mcdp_cd = d.mcdp_cd) ad
          ON p.pt_no = ad.pt_no
  WHERE ad.apnt_ymd LIKE '2022-04-13%' AND
        ad.apnt_cncl_yn = 'N' AND
        ad.mcdp_cd = 'CS'
  ORDER BY 진료예약일시;