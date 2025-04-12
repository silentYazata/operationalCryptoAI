CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE trades (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    token VARCHAR(50) NOT NULL,
    trade_type VARCHAR(10) NOT NULL, -- 'buy' or 'sell'
    amount DECIMAL(18, 8) NOT NULL,
    price DECIMAL(18, 8) NOT NULL,
    trade_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE portfolios (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    token VARCHAR(50) NOT NULL,
    amount DECIMAL(18, 8) NOT NULL,
    average_price DECIMAL(18, 8) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE dao_votes (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    proposal_id INT NOT NULL,
    vote BOOLEAN NOT NULL, -- TRUE for 'yes', FALSE for 'no'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE token_authenticity (
    id SERIAL PRIMARY KEY,
    token VARCHAR(50) NOT NULL UNIQUE,
    is_verified BOOLEAN NOT NULL,
    verification_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE volume_data (
    id SERIAL PRIMARY KEY,
    token VARCHAR(50) NOT NULL,
    volume DECIMAL(18, 8) NOT NULL,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sentiment_scores (
    id SERIAL PRIMARY KEY,
    token VARCHAR(50) NOT NULL,
    score DECIMAL(5, 2) NOT NULL,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE arbitrage_opportunities (
    id SERIAL PRIMARY KEY,
    token VARCHAR(50) NOT NULL,
    price_difference DECIMAL(18, 8) NOT NULL,
    exchange_1 VARCHAR(50) NOT NULL,
    exchange_2 VARCHAR(50) NOT NULL,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE moonshot_predictions (
    id SERIAL PRIMARY KEY,
    token VARCHAR(50) NOT NULL,
    predicted_price DECIMAL(18, 8) NOT NULL,
    prediction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);