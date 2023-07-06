SELECT
    person_name
FROM
    (SELECT
        person_name,
        weight,
        turn,
        SUM(weight) OVER(order BY turn) AS weight_sum
    FROM
        queue) temp
WHERE
    weight_sum <= 1000
ORDER BY
    turn DESC
    LIMIT 1;

--SELECT
--    q1.person_name
--FROM
--    queue q1
--JOIN
--    queue q2
--    ON
--    q1.turn >= q2.turn
--GROUP BY
--    q1.turn
--HAVING
--    SUM(q2.weight) <= 1000
--ORDER BY
--    SUM(q2.weight) DESC
--    LIMIT 1;