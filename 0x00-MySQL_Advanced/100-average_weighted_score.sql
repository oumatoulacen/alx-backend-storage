-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

-- Requirements:
    -- Procedure ComputeAverageScoreForUser is taking 1 input:
        -- user_id, a users.id value (you can assume user_id is linked to an existing users)
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    -- declare the variables
    DECLARE final_average_score float;
    DECLARE total_score float;
    DECLARE total_weight float;

    -- get the full_score and the full_weight
    SELECT SUM(c.score * p.weight), SUM(p.weight) INTO total_score, total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    IF total_weight > 0 THEN
        SET final_average_score = total_score  / total_weight;
    ELSE
        SET final_average_score = 0;
    END IF;
    UPDATE users SET average_score = final_average_score WHERE users.id = user_id;
END //
DELIMITER ;
