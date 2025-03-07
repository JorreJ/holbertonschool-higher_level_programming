-- program to list all records in the table by score only if name is not null
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
