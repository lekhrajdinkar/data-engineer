- [Top 50](https://leetcode.com/problems/rising-temperature/?envType=study-plan-v2&envId=top-sql-50)

```sql
where b.bonus  is null
where b.bonus  = null ❌

No, COUNT(col1) in PostgreSQL does not count NULLs.

-- ✔️ no on condition in "cross join"
FROM Weather yesterday CROSS JOIN Weather today 
-- A CROSS JOIN does not require a join condition. 
-- It returns the Cartesian product of the two tables

SELECT * FROM products CROSS JOIN colors;

SELECT * FROM products INNER JOIN colors; 
This is technically valid SQL, but without a join-condition, it acts like  CROSS JOIN ⬅️


→ This returns every combination of products × colors.
    avoid On large datasets
    use with - Without a filter/where condition


-- ✔️ DATE or TIMESTAMP fields diff
WHERE today.recordDate - yesterday.recordDate = 1 
WHERE today.recordDate - yesterday.recordDate = INTERVAL '1 day'

-- ✔️ rouding of timestanp
ROUND(AVG(EXTRACT(EPOCH FROM (a2.timestamp - a1.timestamp))), 3) AS processing_time

```