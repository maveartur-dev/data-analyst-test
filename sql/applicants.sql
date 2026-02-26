-- Рейтинг абитуриентов по набранным баллам.
-- Таблица: examination(id, scores)

SELECT
    id,
    scores,
    DENSE_RANK() OVER (ORDER BY scores DESC) AS position
FROM examination
ORDER BY scores DESC, id;
