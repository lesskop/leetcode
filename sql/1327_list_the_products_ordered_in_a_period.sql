SELECT
    p.product_name,
    SUM(o.unit) AS unit
FROM
    products p
JOIN
    orders o
    ON
    p.product_id = o.product_id
WHERE
    o.order_date LIKE '2020-02-__'

--    YEAR(o.order_date) = '2020'
--    AND
--    MONTH(o.order_date) = '02'

GROUP BY
    product_name
HAVING
    unit >= 100;