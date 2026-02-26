-- Applicants ranking by exam score.
-- Table: examination(id, scores)

SELECT
    id,
    scores,
    DENSE_RANK() OVER (ORDER BY scores DESC) AS position
FROM examination
ORDER BY scores DESC, id;
