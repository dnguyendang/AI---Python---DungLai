# Chatbot for answering summer intern recruitment questions


# Methdology
# 1. Convert training questions into document term matrix (sparse matrix with 1s and 0s)
# 2. Match the matrix of each training question with its corresponding answer to form a training matrix
# 3. Train SVM model with the training matrix
# 4. Propose a testing quesiton
# 5. Convert the testing question into document term matrix (sparse matrix with 1s and 0s)
# 6. Merge the testing DTM with training DTM, with testing DTM 1s for all terms and training DTM 0s for all terms
# 7. Predict the answer with the trained SVM model

# ask more ram to handle 
memory.limit(24000)

# read data
library(readxl)
data = read.csv('C:/Users/dungd/OneDrive/Documents/Python_DungLai/VirtualAssistant/complexVersion/conversationo.csv')

# create factrs 
data$answers <- factor(c(data$answers));

# 1. Convert training questions into document term matrix (sparse matrix with 1s and 0s)
#clean the text
library(SnowballC)
library(tm)
corpus = VCorpus(VectorSource(data$questions))
corpus = tm_map(corpus, content_transformer(tolower))
corpus = tm_map(corpus, removeNumbers)
corpus = tm_map(corpus, removePunctuation)
# corpus = tm_map(corpus, removeWords, stopwords())
corpus = tm_map(corpus, stemDocument)
corpus = tm_map(corpus, stripWhitespace)
# convert to DTM
dtm = DocumentTermMatrix(corpus)
# convert to dataframe
dataset = as.data.frame(as.matrix(dtm))

# 2. Match the matrix of each training question with its corresponding answer to form a training matrix
data_train= cbind(data['answers'], dataset)

# 3. Train SVM model with the training matrix
library("e1071")
svmfit = svm(answers ~., data_train, kernel = "linear", cost = 100, scale = FALSE)


# 4. Propose a testing quesiton and build the prediction function
pred = function(x){
  
  # 5. Convert the testing question into document term matrix (sparse matrix with 1s and 0s)
  #clean the text
  corpus = VCorpus(VectorSource(x))
  corpus = tm_map(corpus, content_transformer(tolower))
  corpus = tm_map(corpus, removeNumbers)
  corpus = tm_map(corpus, removePunctuation)
  # corpus = tm_map(corpus, removeWords, stopwords())
  corpus = tm_map(corpus, stemDocument)
  corpus = tm_map(corpus, stripWhitespace)
  # convert to DTM
  dtm = DocumentTermMatrix(corpus)
  # convert to dataframe
  data_test = as.data.frame(as.matrix(dtm))
  
  # 6. Merge the testing DTM with training DTM, with testing DTM 1s for all terms and training DTM 0s for all terms
  add_data = dataset[1,]
  add_data[add_data == 1] = 0
  data_test=cbind(data_test,add_data)
  
  # 7. Predict the answer with the trained SVM model
  p = predict(svmfit, data_test)
  answer = as.character(p)
  # Predict
  paste("Answer:", answer)
}

# Predict
pred("hey")

