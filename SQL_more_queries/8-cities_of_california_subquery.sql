-- lists all cities of california from hbtn_0b_usa
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name="California")
ORDER BY id ASC;