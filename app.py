from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tweets = [
    {'id': 1, 'content': 'My first '},
    {'id': 2, 'content': 'Hungry'},
    {'id': 3, 'content': 'This is dope!'}
]

# Home page - displays all tweets
@app.route('/')
def home():
    return render_template('index.html', tweets=tweets)

# Create a new tweet
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Insert the tweet into the database
        tweet = {
            'id': len(tweets)+1, 'content':request.form['content']
        }
        # Append the new tweet to the list
        tweets.append(tweet)
        return redirect(url_for('home'))
    return render_template('create.html')

# Update a tweet
@app.route('/edit/<int:tweet_id>', methods=['GET', 'POST'])
def edit(tweet_id):
    # You can replace this with actual database code to fetch the tweet
    if request.method == 'POST':
        # You can replace this with actual database code to update the tweet
        new_content = request.form['content']
        # Update the tweet in the database
        for tweet in tweets:
            if tweet['id'] == tweet_id:
                tweet['content'] = new_content
                break
        return redirect(url_for('home'))
    for tweet in tweets:
        if tweet['id'] == tweet_id:    
            return render_template('edit.html', tweet=tweet)

# Delete a tweet
@app.route('/delete/<int:tweet_id>')
def delete(tweet_id):
    for tweet in tweets:
        if tweet['id'] == tweet_id:
            tweets.remove(tweet)
            break
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)