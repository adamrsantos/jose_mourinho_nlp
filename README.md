# Jose Mourinho Press Conference and Interview Analysis

The purpose of this project is to examine the career of Jose Mourinho through the lens of his interviews and press conferences. At the time of the project (maybe for not much longer), he is the manager of Manchester United. He has coached other teams such as Chelsea, Real Madrid, and Inter Milan. He is renowned for playing a defensive, pragmatic style and has won many trophies. He is also renowned for outlandish quotes and playing games with the media during press conferences. For this reason, I thought he would be an interesting way to test out my newly acquired NLP skills.

Process:
1) Obtain youtube ids for videos resulting from a search for different Jose Mourniho related phrases using selenium
2) Scrape youtube captions for these videos
3) Obtain metadata for these videos through the youtube api
4) Clean and filter video captions and data
5) Obtain word counts and frequencies using count and tfidf vectorizers
6) Use LDA and NMA to reduce dimensionality of vectors and obtain topics for topic models
7) Analyze topics over time compared with team results and press conference sentiments
8) Create visualizations to present findings
9) Create a flask app to generate Jose Mourinho quotes using topics and user defined game scores
10) [Presentation](https://docs.google.com/presentation/d/1u9GSS0hBagihcbB2OA9TURmze0bg9KOhId7KLT3FQGk/edit?usp=sharing)
