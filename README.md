<div  align = "center">
  <img src="https://github.com/RanitManik/TelegamGPT/assets/138437760/bc591d8b-b7f2-43b4-829a-5f2838d941bd" height="100">
  <h1>TelegramGPT Chatbot</h1>
</div>

# Overview

TelegramGPT is a Telegram chatbot powered by OpenAI's GPT-3.5 Turbo model created using Python. It reads messages from a specified chat file and responds to user messages in Telegram using the GPT-3.5 Turbo model.

# Features

- Seamless integration with Telegram
- Configurable chat file selection
- Utilizes OpenAI GPT-3.5 Turbo for natural language understanding
- Easy-to-use and extendable

# Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/RanitManik/TelegamGPT.git
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```
   
# Usage

### 1. Set up Telegram Bot
  
  1. Create a Telegram bot on the [Telegram BotFather](https://core.telegram.org/bots#botfather).
  
  2. Copy the bot token.
  
  3. Replace `Your Telegram Bot Token Goes here` in the `.env` file with the actual bot token.

### 2. Create an OpenAI Account
    
  1. Visit the OpenAI website: [https://beta.openai.com/](https://beta.openai.com/)
  
  2. Sign up for an account if you don't have one. Follow the registration process.

### 3. Access the OpenAI API Section

  1. Once you're logged in, navigate to the OpenAI API section.
    
     - On the OpenAI dashboard, click on your account name in the top right corner.
     - Select "API" from the dropdown menu.

### 4. Create a New API Key

  1. In the API section, you'll find the option to create a new API key.
    
  2. Click on the "Create API Key" button.
    
  3. Give your API key a meaningful name related to your project (e.g., "TelegramGPT").
    
  4. Copy the generated API key. It will look something like this: `sk-xxxxxx-xxxxxxxxxxxxxx`.
    
  5. Open the `.env` file in your TelegramGPT project directory.
    
  6. Replace the placeholder `Your openAI API key goes here` with the actual API key you obtained from OpenAI:
  
     ```plaintext
     TELEGRAM_TOKEN=your_telegram_bot_token
     OPENAI_API_KEY=sk-xxxxxx-xxxxxxxxxxxxxx
     ```

### 5. Save and Run

  1. Save the changes to the `.env` file.
  
  2. Now, when you run your TelegramGPT bot, it will use the OpenAI GPT-3.5 Turbo model with the specified API key.

### 6. Verify Functionality
  
  1. Start a chat with your Telegram bot.
  
  2. Use the `/setfile` command to set the chat file (e.g., `/setfile 1`).
  
  3. Send messages to the bot and confirm that it generates responses using the GPT-3.5 Turbo model.
  
  By following these steps, you've successfully created an OpenAI GPT-3.5 Turbo API key and integrated it into your TelegramGPT project. This key allows your bot to communicate with the OpenAI API and generate natural language responses.

# Configuration

You can configure the bot by modifying the following variables in `main.py`:

- `fileNumber`: Change the chat file by setting this variable to 1, 2, or 3 before `/setfile` flag and send it to bot.
- `model`: Specify the GPT model to be used (default is "gpt-3.5-turbo").
- Adjust other parameters like `temperature`, `max_tokens`, `top_p`, `frequency_penalty`, and `presence_penalty` as needed.

# Chat Files

- `chats/chat1.txt`: [Sample chat file 1](chats/chat1.txt) — describe your chat content
- `chats/chat2.txt`: [Sample chat file 2](chats/chat2.txt) — describe your chat content
- `chats/chat3.txt`: [Sample chat file 3](chats/chat3.txt) — describe your chat content

# Contributing

1. Clone the repository:

   ```bash
   git clone https://github.com/RanitManik/TelegamGPT.git
   ```

2. **Add This repo as Remote**:

   ```bash
   git remote add origin https://github.com/RanitManik/TelegamGPT.git
   ```

3. **Create a New Branch** for your feature or bugfix:

   ```bash
   git checkout -b feature/{your_feature} or bugfix/{issue_number}
   ```

4. **Commit** your changes:

   ```bash
   git commit -m "Your meaningful commit message here"
   ```

5. **Push** your changes to the repository:

   ```bash
   git push origin feature/{your_feature} or bugfix/{issue_number}
   ```

Feel free to contribute to the project by opening issues or pull requests. Any feedback or improvements are appreciated.

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Contact

- Name - [Your Name](https://github.com/your-username)
- Email - your.email@example.com
- Project Link - [https://github.com/RanitManik/TelegamGPT](https://github.com/RanitManik/TelegamGPT)

---

<p align="center"> If you like my work, maybe consider buying me a coffee/tea <img src="https://media.giphy.com/media/lRSeZ2ddNwhZ5AgIvk/giphy.gif" width="25">

<p align="center"><a href="https://www.buymeacoffee.com/your-username" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" width="150"></a>
