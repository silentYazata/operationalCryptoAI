INSERT INTO dao_votes (user_id, token_address, vote, timestamp) 
VALUES (%s, %s, %s, NOW());