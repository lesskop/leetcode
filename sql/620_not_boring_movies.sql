SELECT
    *
FROM
    cinema
WHERE
    description <> "boring"
    AND
    mod(id, 2) <> 0
ORDER BY
    rating DESC;