-- Write a query to display total number of unique users, and sum of total amount spent for each game and install source
SELECT
    game,
    install_source,
    COUNT(DISTINCT user_id) AS unique_users,
    SUM(total_amount_spent) AS total_amount
FROM GAMERS
GROUP BY game, install_source;

-- Write a query that returns the top 3 spenders (users with positive amount spent) by country that are installed from ‘ua’.
SELECT
    country,
    user_id,
    SUM(amount) AS total_amount
FROM GAMERS
WHERE total_amount_spent > 0 and install_source = 'ua'
group by user_id, country
order by total_amount desc
limit 3;

-- Write a query that gives the daily average revenue per game, with daily average revenue = sum of total revenue spent in that day / total unique players in that day
SELECT
    game,
    install_date,
    SUM(total_amount_spent) / COUNT(DISTINCT user_id) AS daily_average_revenue
FROM GAMERS
GROUP BY game, install_date;


-- last two questions
-- The last two questions use Windows functions.
-- I don't use these more advanced queries on a daily basis, but I could have found the solutions if I'd had more time.
-- Instead, I skipped these two questions and concentrated on the rest, which still seemed long.