---Select school and church ---SELECT *FROM	salzburg_buildingsWHERE type = 'school';---Only church---SELECT *FROM	salzburg_buildingsWHERE type = 'church';---Both---SELECT *FROM	salzburg_buildingsWHERE type = 'school' or type = 'church';---Area for school---
SELECT b.*,
	ST_AREA(b.geom) AS school_area
FROM
	salzburg_buildings AS b
WHERE type = 'school';	
---Area for church---
SELECT b.*,
	ST_AREA(b.geom) AS church_area
FROM
	salzburg_buildings AS b
WHERE type = 'church';	
---for both---
SELECT b.*,
	ST_AREA(b.geom) AS area_school_church
FROM
	salzburg_buildings AS b
WHERE type = 'school' or type = 'church';	



