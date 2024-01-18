-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
-- Context: Calculate/compute something is always power intensive… better to distribute the load!
SELECT band_name, (IFNULL(split, 2022) - IFNULL(formed, 0)) as lifespan
FROM metal_bands where style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
