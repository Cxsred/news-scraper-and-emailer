<h1>News Scraper and Emailer</h1>

<p>This Python script fetches the latest news headlines from a leading global news website and sends them via email.</p>

<h2>Prerequisites</h2>

<ul>
  <li>Python 3.x</li>
  <li><code>requests</code> library</li>
  <li><code>beautifulsoup4</code> library</li>
  <li><code>smtplib</code> library</li>
</ul>

<h2>Installation</h2>

<ol>
  <li>Clone the repository:</li>
</ol>

<pre><code>git clone https://github.com/your-username/news-scraper-emailer.git</code></pre>

<ol start="2">
  <li>Change to the project directory:</li>
</ol>

<pre><code>cd news-scraper-emailer</code></pre>

<ol start="3">
  <li>Install the required libraries:</li>
</ol>

<pre><code>pip install requests beautifulsoup4 smtplib</code></pre>

<h2>Usage</h2>

<ol>
  <li>Open the <code>main.py</code> file.</li>
  <li>Replace the placeholders with your email account details:</li>
</ol>

<pre><code>sender_email = "your-email@example.com"
sender_password = "your-email-password"
receiver_email = "recipient-email@example.com"</code></pre>

<ol start="3">
  <li>Run the script:</li>
</ol>

<pre><code>python main.py</code></pre>

<ol start="4">
  <li>The script will fetch the latest news headlines and send them via email to the specified recipient email address.</li>
</ol>

<h2>Customization</h2>

<ul>
  <li>You can modify the <code>fetch_news()</code> function to scrape news from different websites. Inspect the HTML structure of the target website and adjust the code accordingly.</li>
  <li>Customize the email subject and body in the <code>send_email()</code> function according to your preferences.</li>
</ul>

<h2>Notes</h2>

<ul>
  <li>Make sure to comply with the terms of service of the websites you are scraping.</li>
  <li>If using Gmail, you may need to enable access to less secure apps or generate an app password.</li>
</ul>

<h2>License</h2>

<p>This project is licensed under the MIT License.</p>
