-- list all shows with at least one genre linked from hbtn_0d_tvshows
SELECT b.title, a.genre_id
FROM tv_show_genres a
LEFT JOIN tv_shows b
ON a.show_id = b.id
ORDER BY b.title, a.genre_id ASC;
