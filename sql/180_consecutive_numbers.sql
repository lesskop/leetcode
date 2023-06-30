SELECT DISTINCT
    l1.num AS ConsecutiveNums
FROM
    logs l1,
    logs l2,
    logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.num = l2.num
    AND l2.num = l3.num;