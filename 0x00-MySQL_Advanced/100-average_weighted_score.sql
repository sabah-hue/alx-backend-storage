-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.

DELIMITER $$;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    SELECT AVG(corrections.score * projects.weight) / SUM(projects.weight) AS res
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    UPDATE users SET average_score = res WHERE id = user_id 
END;$$

DELIMITER;
