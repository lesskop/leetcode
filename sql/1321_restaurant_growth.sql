SELECT
    c1.visited_on,
    SUM(c2.amount) / COUNT(DISTINCT c1.name) AS amount,
    ROUND(
        SUM(c2.amount) / COUNT(DISTINCT c1.name) / 7
        , 2) AS average_amount
FROM
    customer c1
JOIN
    customer c2
    ON
    DATEDIFF(c1.visited_on, c2.visited_on) BETWEEN 0 AND 6
GROUP BY
    c1.visited_on
HAVING
    COUNT(DISTINCT c2.visited_on) = 7
ORDER BY
    c1.visited_on;