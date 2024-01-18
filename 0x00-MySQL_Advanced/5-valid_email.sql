-- Write a SQL script that creates a trigger that resets the attribute valid_email
-- only when the email has been changed.
-- Context: Nothing related to MySQL, but perfect for user email validation -
-- distribute the logic to the database itself!
DELIMITER //
CREATE TRIGGER trigger_before_email_change_only BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN -- <> same as !=
         -- Reset valid_email if the email is changed
        SET NEW.valid_email = 0;
    END IF;
END;
//
DELIMITER ;
