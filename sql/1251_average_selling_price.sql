SELECT
    u.product_id,
    round(sum(price * units) / sum(units), 2) AS average_price
FROM
    unitssold u
JOIN
    prices p
    ON
    p.product_id = u.product_id
    AND
    u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY
    product_id;