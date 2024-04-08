SELECT 	b.*
FROM
	salzburg_buildings AS b,
	(SELECT geom FROM salzburg_buildings WHERE name = 'Glockenturm') AS g
WHERE 
	st_distance(b.geom,g.geom) < 500; ---From the chosen location---SELECT 	b.*FROM	salzburg_buildings AS b,	(SELECT geom FROM salzburg_buildings WHERE name = 'Raiffeisen Lagerhaus Technik') AS gWHERE 	st_distance(b.geom,g.geom) < 500; 
