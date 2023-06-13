SELECT
  r.contest_id,
  ROUND((
    COUNT(r.user_id) / (SELECT COUNT(user_id) FROM USERS)) * 100,
    2) AS percentage
FROM
  register r
JOIN
  users u
  ON
  u.user_id = r.user_id
GROUP BY
  r.contest_id
ORDER BY
  percentage DESC,
  r.contest_id;