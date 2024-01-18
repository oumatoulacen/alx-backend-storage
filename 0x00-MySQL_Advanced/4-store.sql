-- SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
-- Quantity in the table items can be negative.
-- Context: Updating multiple tables for one action from your application can generate
-- issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!
DELIMITER //
CREATE TRIGGER trigger_on_add AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    DECLARE item_quantity INT;
    -- Get the current quantity of the item
    SELECT quantity INTO item_quantity FROM items WHERE name = NEW.item_name;
    UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
END;
//
DELIMITER ;
