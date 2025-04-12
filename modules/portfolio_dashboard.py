from flask import Flask, render_template
from database.database_config import get_db_connection

app = Flask(__name__)

@app.route('/portfolio')
def portfolio_dashboard():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Fetch portfolio data from the database
    cursor.execute("SELECT * FROM portfolio")
    portfolio_data = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('portfolio_dashboard.html', portfolio=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)