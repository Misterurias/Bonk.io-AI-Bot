const dotenv = require('dotenv');
dotenv.config();

const OpenAI = require('openai');
const readline = require('readline');

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

const userInterface = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

async function getChatbotResponse(input) {
  const response = await openai.chat.completions.create({
    model: "gpt-3.5-turbo",
    messages: [{ role: "user", content: input }],
  });
  return response.choices[0].message.content;
}

userInterface.prompt();
userInterface.on("line", async (input) => {
  const response = await getChatbotResponse(input);
  console.log(response);
  userInterface.prompt();
});

module.exports = {
  getChatbotResponse,
};
