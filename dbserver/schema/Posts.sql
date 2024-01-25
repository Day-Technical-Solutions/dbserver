CREATE TABLE Posts (
  post_id INT PRIMARY KEY,
  title VARCHAR(255),
  selftext TEXT NOT NULL,
  processed BOOLEAN NOT NULL DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  subreddit VARCHAR(255),
  url VARCHAR(255)
);