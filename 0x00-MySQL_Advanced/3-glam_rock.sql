-- SQL script that lists all bands with Glam rock as their main style,
-- ranked by their longevity
SELECT band_name, COALESCE(split, 2022) - formed AS lifespan
FROM metal_bands
Where style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
