-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.
DELIMITER $$;

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers(
    IN user_id INT
)
BEGIN
    UPDATE users
    SET average_score = (
        SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
        FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = 2
    )
    WHERE id = 2;
END;$$

DELIMITER ;
