-- SQL script that creates a trigger that decreases the quantity
-- of an item after adding a new order.
CREATE TRIGGER dec_quantity BEFORE INSERT ON orders
       FOR EACH ROW UPDATE items
       SET quantity = quantity - NEW.number
       where items.name = NEW.item_name;
