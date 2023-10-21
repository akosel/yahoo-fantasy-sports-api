# yahoo-fantasy-sports

### Setup

You'll need to create an OAuth application to get the required `CLIENT_ID` and `CLIENT_SECRET`. Go [here](https://developer.yahoo.com/apps/create/) to do that. Application name and description can be anything. I set redirect uri to localhost:8000, just because it's required, but this won't be important. Then select 'Confidential Client' and then check 'Fantasy Sports'.

### Environment Variables

- `YAHOO_CLIENT_ID` - Client ID for your OAuth application
- `YAHOO_CLIENT_SECRET` - Client Secret for your OAuth application
- `YAHOO_LEAGUE_ID` - League ID which can be obtained from the URL for your league (e.g. https://football.fantasysports.yahoo.com/f1/123456, where 123456 is the league id)

### Usage

```
yfs = YahooFantasySports()

response = yfs.get_standings()
```
