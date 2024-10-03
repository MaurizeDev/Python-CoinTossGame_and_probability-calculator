# Coin Toss Game

## Introduction
This project simulates a theoretical scenario inspired by the stock market: Are successful investors like Warren Buffett and Ray Dalio exceptionally skilled, or could their success simply be a statistical outlier in a large population? 

In large populations, even highly improbable events become almost certain. The goal of this program is to simulate a tournament where millions of people toss coins, and we observe how many toss only heads, highlighting the inevitability of statistical outliers.

## Concept
The core idea is based on the statistical probability of a coin landing on heads or tails. If a large enough population participates in a coin toss tournament, it is statistically inevitable that some participants will always toss heads (or tails), despite the low probability of this event happening. This project demonstrates that even with an incredibly low probability (such as 0.0000000931323%, or 1 in a billion), someone will eventually toss heads consistently in a large enough population.

For example, with 300 million people tossing coins 30 times, there is still a 25% chance that someone will have tossed 30 heads in a row. The program simulates coin tosses for a given number of players and tosses, and summarizes the results.

## Features
- Simulates a specified number of players tossing coins a given number of times.
- Tracks how many players tossed only heads or only tails.
- Displays results for individual players or overall statistics.
- Uses Python's `random` module to simulate unbiased coin tosses.
- Displays runtime and performance metrics.

## Usage

### Prerequisites
This program requires Python 3. Make sure you have it installed on your system.

### Running the program
You can modify the number of players and coin tosses by changing the variables in the script:

```python
number_of_players = 1_000_000
number_of_tosses = 20
```

### Sample Output
```
───────────────────────────────────────────────────────────────
	Total Result with 20 tosses
───────────────────────────────────────────────────────────────

Number of players:                 100,000,000
Total number of coin tosses:       2,000,000,000
Total heads tosses:                1,000,123,852 (50.00619%)
Total tails tosses:                999,876,148 (49.99380%)
Players only tossed heads:         98 (Probability: 0.000098%)
Players only tossed tails:         102 (Probability: 0.000102%)
Program runtime:                   40:34 min
```
