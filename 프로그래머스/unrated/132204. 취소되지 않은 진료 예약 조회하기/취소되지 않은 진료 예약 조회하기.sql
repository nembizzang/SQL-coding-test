SELECT a_d.apnt_no, p.pt_name, p.pt_no, a_d.mcdp_cd, a_d.dr_name, a_d.apnt_ymd
FROM patient p
JOIN (SELECT d.dr_name, d.dr_id, d.mcdp_cd, a.apnt_ymd, a.apnt_no, a.pt_no, a.apnt_cncl_yn
      FROM doctor d
      JOIN appointment a
      ON d.dr_id = a.mddr_id AND d.mcdp_cd = a.mcdp_cd) a_d
ON p.pt_no = a_d.pt_no
WHERE DATE_FORMAT(apnt_ymd, '%y-%m-%d')='22-04-13' AND apnt_cncl_yn = 'N' AND mcdp_cd = 'CS'
ORDER BY apnt_ymd