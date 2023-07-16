-- Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
-- Import this table dump: metal_bands.sql.zip
-- Column names must be: origin and nb_fans
SELECT origin, fans as nb_fans from metal_bands ORDER BY fans DESC;