# 🔔 Altcoin Announcements Tracker
A straightforward Python script designed to scrape the latest altcoin announcements from the [Bitcoin Forum](https://bitcointalk.org/index.php) and deliver them straight to your inbox, keeping you updated effortlessly.

* Target Boards:
    * [Announcements (Altcoins)](https://bitcointalk.org/index.php?board=159.0)
    * [Tokens (Altcoins)](https://bitcointalk.org/index.php?board=240.0)
* Email Preview

![alt text](preview.jpg)

## 🚀 Getting Started

### 1. Download the Project

```
git clone https://github.com/OwenLittleWhite/new-altcoin-notification.git
```

```
cd new-altcoin-notification
```

### 2. Install Dependencies

```
pip install requests beautifulsoup4
```

### 3. Configuration

* Copy the sample configuration file and tweak it to your liking:
```
cp config_sample.py config.py
```
* Customize `config.py` according to your preferences.

### 4. Run the Script

Set up a cron job to execute the script every 5 minutes:
```
*/5 * * * * python3 /path/to/new-altcoin-notification/post_list.py > /path/to/new-altcoin-notification/log.txt 2>&1
```
With these steps, you'll be receiving the freshest altcoin announcements from the Bitcoin Forum directly in your mailbox! Stay informed without lifting a finger.




