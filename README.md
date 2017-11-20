# yahoo-fantasy-sports

### Usage

```
credentials_file = '/path/to/credentials/file.json'
league_id = '123456' # put your real league id here
yfs = YahooFantasySports(credentials_file, league_id=league_id)

response = yfs.get_standings()
```
