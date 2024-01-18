-- Write a SQL script that creates an index idx_name_first on the table names and the first letter of name.
-- Context: Index is not the solution for any performance issue, but well used, it’s really powerful!
CREATE INDEX idx_name_first ON names(name(1))
