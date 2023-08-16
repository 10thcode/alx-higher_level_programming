-- converts hbtn_0c_0 database to UTF8
ALTER DATABASE hbtn_0c_0 CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
ALTER TABLE first_table CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
ALTER TABLE first_table ALTER COLUMN name CHARSET utf8mb4 COLLATE utf8mb4_unicode_ci;
