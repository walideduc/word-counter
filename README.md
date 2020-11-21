# Word's Counter
## How to use ?
### Prerequisite
Please make sure that you have docker installed on your machine and clone the project.
### Run the application
1. Run the following command form the root folder to build the docker image.
```
docker build -f infrastructure/Dockerfile -t test/word-counter .
```
2. You can pass the sentence as environment variable to the application using `--env` flag when running a container form the image as follow
```
docker run --env SENTENCE="word1 word2 word3 word1 word2 word2 word2 word3" test/word-counter
```