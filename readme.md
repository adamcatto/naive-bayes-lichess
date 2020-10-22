# Naive Bayes Classifier on Lichess database

Made a naive Bayes classifier to classify elo bin, using local patterns in stockfish evaluations as indicators, modulated by game type and way in which the game ended.

Had 518 samples. The idea was to see if there might be a correlation between jumps in stockfish evaluations of consecutive positions and the average elo of the players.

This is still ongoing – the feature engineering was mostly hacked together as a proof-of-concept (most emphasis was on ETL preprocessing); I will experiment with different features and learning algorithms (and more data!).
