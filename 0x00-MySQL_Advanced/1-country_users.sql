-- sql  script that creates a table users following these requirements:
-- users(id, email, name, country)
CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                    email VARCHAR(255) NOT NULL UNIQUE,
                    name VARCHAR(255),
                    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
                    )
