-- Клиенты, у которых сумма покупок за последний полный месяц < 5000
-- Без подзапросов и оконных функций
-- Таблицы: account, "transaction"

SELECT
    a.client_id
FROM account AS a
LEFT JOIN "transaction" AS t
    ON t.account_id = a.id
   AND t.type = 'PUR'  -- покупки
   AND t.transaction_date >= date_trunc('month', current_date) - INTERVAL '1 month'
   AND t.transaction_date <  date_trunc('month', current_date)
GROUP BY a.client_id
HAVING COALESCE(SUM(t.amount), 0) < 5000;
