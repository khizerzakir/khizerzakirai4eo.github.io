---Query to estimate distance from chosen location---
SELECT 
	b.*,
	st_distance(
	b.geom,
	g.geom) AS distance
FROM
	salzburg_buildings AS b,
	(SELECT geom FROM salzburg_buildings 
	WHERE
	name = 'Raiffeisen Lagerhaus Technik') AS g;
------Query to estimate distance from city centre---
SELECT 
	b.*,
	st_distance(
	b.geom,
	g.geom) AS distance_centre
FROM
	salzburg_buildings AS b,
	(SELECT geom FROM salzburg_buildings 
	WHERE
	name = 'Glockenturm') AS g