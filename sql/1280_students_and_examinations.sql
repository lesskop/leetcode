SELECT
    st.student_id,
    st.student_name,
    su.subject_name,
    COUNT(e.subject_name) AS attended_exams
FROM
    students st
JOIN
    subjects su
LEFT JOIN
    examinations e
    ON
    st.student_id = e.student_id
    AND
    su.subject_name = e.subject_name
GROUP BY
    st.student_id,
    su.subject_name
ORDER BY
    student_id,
    subject_name;