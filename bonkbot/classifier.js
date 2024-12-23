
// classifier.js
const natural = require('natural');
const stopword = require('stopword');
const tokenizer = new natural.WordTokenizer();
const classifier = new natural.BayesClassifier();

// Train the classifier with a larger set of sample questions
classifier.addDocument('what map are we on', 'current_map');
classifier.addDocument('which map are we playing on', 'current_map');
classifier.addDocument('current map', 'current_map');
classifier.addDocument('map name', 'current_map');

classifier.addDocument('who is the host', 'host');
classifier.addDocument('who is hosting', 'host');
classifier.addDocument('host', 'host');

classifier.addDocument('how many players are in the game', 'player_count');
classifier.addDocument('number of players', 'player_count');
classifier.addDocument('players in the game', 'player_count');

classifier.addDocument('what game mode are we playing', 'game_mode');
classifier.addDocument('current game mode', 'game_mode');
classifier.addDocument('game mode', 'game_mode');

classifier.addDocument('what level is', 'player_level');
classifier.addDocument('what level is {player_name}', 'player_level');
classifier.addDocument('which level is {player_name}', 'player_level');
classifier.addDocument('level of {player_name}', 'player_level');
classifier.addDocument('what is the level of {player_name}', 'player_level');

classifier.train();

// Function to preprocess the question
function preprocessQuestion(question) {
    // Convert to lowercase
    let processed = question.toLowerCase();
    // Tokenize the question
    processed = tokenizer.tokenize(processed);
    // Remove stop words
    processed = stopword.removeStopwords(processed);
    // Join the processed words back into a string
    processed = processed.join(' ');
    return processed;
}

function classifyQuestion(question) {
    const processedQuestion = preprocessQuestion(question);
    return classifier.classify(processedQuestion);
}

module.exports = {
    classifyQuestion
};
