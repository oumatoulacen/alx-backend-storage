-- SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.
-- Requirements:
    -- You must create a function
    -- The function SafeDiv takes 2 arguments:
    -- a, INT
    -- b, INT
    -- And returns a / b or 0 if b == 0

DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    DECLARE total DECIMAL(10,2);
    IF b = 0 THEN
        RETURN 0;
    ELSE
        SET total = a / b;
        RETURN total;
    END IF;
END
$$
DELIMITER ;
