---for apartment
SELECT 
b.*,
st_area(b.geom) AS apt_area
FROM salzburg_buildings AS b
WHERE 
	type = 'apartments'
---for house---
SELECT 
b.*,
st_area(b.geom) AS house_area
FROM salzburg_buildings AS b
WHERE 
	type = 'house'
---for apartment & house---
SELECT 
b.*,
st_area(b.geom) AS house_apt_area
FROM salzburg_buildings AS b
WHERE 
	type = 'house' or type = 'apartments'


	