#!/bin/bash

# This script automates the database setup and migration process.

# Load database configuration
source ./database/database_config.py

# Function to run SQL commands
run_sql() {
    PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -U $DB_USER -d $DB_NAME -f $1
}

# Create the database if it doesn't exist
echo "Creating database if it doesn't exist..."
createdb -h $DB_HOST -U $DB_USER $DB_NAME

# Run schema migration
echo "Running schema migration..."
run_sql ./database/schema.sql

# Run any additional migrations if needed
# Uncomment and add additional migration files as necessary
# run_sql ./database/migrations/migration_file.sql

echo "Database migration completed successfully."