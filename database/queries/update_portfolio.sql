UPDATE portfolio
SET balance = balance + $1, 
    last_updated = NOW()
WHERE user_id = $2;