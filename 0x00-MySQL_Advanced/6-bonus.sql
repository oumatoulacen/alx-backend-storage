-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student
-- Context: Write code in SQL is a nice level up!
DELIMITER $$
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    -- Procedure AddBonus is taking 3 inputs
    DECLARE project_id VARCHAR(255);

    -- Check if the project exists
    SELECT id INTO project_id FROM projects WHERE name = project_name;

    -- Project doesn't exist, create it
    if (project_id IS NULL) THEN
        INSERT INTO projects (name) VALUES (project_name);
        -- Get the project_id after inserting
        SET project_id = LAST_INSERT_ID();
    END IF;
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END;
$$
DELIMITER ;
