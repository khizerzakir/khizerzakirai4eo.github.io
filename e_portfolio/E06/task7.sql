SELECT 
	AVG(
	st_area(b.geom)) AS avg_size
FROM
	salzburg_buildings AS b,
	(SELECT geom FROM salzburg_buildings 
	WHERE name = 'Raiffeisen Lagerhaus Technik') AS gWHERE	st_distance(b.geom,g.geom)<1000;