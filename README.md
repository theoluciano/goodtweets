# goodtweets
### Instantly find quotes based on a prompt and post to Twitter

This program will take any prompt you give it and search Goodreads for quotes matching this prompt, and then return a random one, which will automatically be posted to your connected Twitter account. With a few changes, you can change the program to return a random quote only to the terminal, which can be useful as well.

Once you've cloned the repo, you'll need to install the necessary libraries that are required for the program to run. For this project, those are:
- Beautiful Soup
- Tweepy
- Pandas


You can do this from your terminal by using `pip`.

Execute the following command to install your libraries: `pip3 install beautifulsoup4 tweepy pandas`

Then you'll need to replace the placeholder tokens in the `tokens_template` file with your actual Twitter developer credentials. 

Note: you'll need a read and write level of access from Twitter for this program to work. More info here [https://developer.twitter.com/en/docs/apps/app-permissions]

Once you've made these changes, you'll be able to run the program.

----

The errors that are returned from Twitter's API and TweePy are fairly self-explanatory. 

If the error states '`186 - Tweet needs to be a bit shorter.`, then you'll need to run the program again to find a less wordy passage. 

If the error states `170 - Missing required parameter: status.`, then there are no results for that particular query. Try something else.

I haven't run into any problems beyond that, but if you find something, let me know or open up a PR!

Thanks and have a blessed day.

Sources:

These articles and sites helped in the development of this project:
https://github.com/elizabethsiegle/parse-html-for-top-goodreads-quotes-with-twilio-whatsapp
https://www.twilio.com/blog/parse-html-for-book-quotes-python-beautiful-soup-whatsapp
https://learningactors.com/how-to-scrape-multiple-pages-of-a-website-using-a-python-web-scraper/
