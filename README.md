<div  align = "center">
  <img src="https://github.com/RanitManik/TelegamGPT/assets/138437760/bc591d8b-b7f2-43b4-829a-5f2838d941bd" height="100">
  <h1>TelegramGPT Chatbot</h1>
</div>

Welcome to the comprehensive setup guide for the ChatGPT Text Generation Service, a powerful tool that utilizes the state-of-the-art GPT-3.5 Turbo model to generate natural language text. Follow this step-by-step guide to set up the Text Generation Service and unlock the capabilities of ChatGPT.


## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
  - [Clone the Repository](#1-clone-the-repository)
  - [Install Required Packages](#2-install-required-packages)
- [Usage](#usage)
  - [Set up Telegram Bot](#1-set-up-telegram-bot)
  - [Create an OpenAI Account](#2-create-an-openai-account)
  - [Access the OpenAI API Section](#3-access-the-openai-api-section)
  - [Create a New API Key](#4-create-a-new-api-key)
  - [Save and Run](#5-save-and-run)
  - [Verify Functionality](#6-verify-functionality)
- [Configuration](#configuration)
- [Text Generation](#text-generation)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgment](#acknowledgment)

## Overview

TelegramGPT is a Telegram chatbot powered by OpenAI's GPT-3.5 Turbo model created using Python. It reads messages from a specified chat file and responds to user messages in Telegram using the GPT-3.5 Turbo model.

## Features

- Seamless integration with Telegram
- Configurable chat file selection
- Utilizes OpenAI GPT-3.5 Turbo for natural language understanding
- Easy-to-use and extendable

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/ChatGPT-Text-Generation
```

### 2. Install Required Packages

```bash
pip install -r requirements.txt
```
   
## Usage

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

## Configuration

You can configure the bot by modifying the following variables in `main.py`:

- `fileNumber`: Change the chat file by setting this variable to 1, 2, or 3 before `/setfile` flag and send it to bot.
- `model`: Specify the GPT model to be used (default is "gpt-3.5-turbo").
- Adjust other parameters like `temperature`, `max_tokens`, `top_p`, `frequency_penalty`, and `presence_penalty` as needed.

### Chat Files

- `chats/chat1.txt`: [Sample chat file 1](chats/chat1.txt) — my resume
- `chats/chat2.txt`: [Sample chat file 2](chats/chat2.txt) — whatsapp chat bwtween me and my friend
- `chats/chat3.txt`: [Sample chat file 3](chats/chat3.txt) — a simple AI generated friends chat

## Text Generation

Experiment with the service by sending text prompts and receiving generated responses. Adjust configuration parameters for different text generation styles.

## Contributing

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

<table>
  <tr>
    <th></th>
    <th>Social Media</th>
    <th>Username</th>
    <th>Link</th>
  </tr>
  <tr>
    <td><img src="https://cdn4.iconfinder.com/data/icons/social-media-logos-6/512/112-gmail_email_mail-512.png" width="20" /></td>
    <td>Email</td>
    <td><code>ranitmanik.dev@gmail.com</code></td>
    <td><a href="mailto:ranitmanik.dev@gmail.com" target="_blank">Email</a></td>
  </tr>
  <tr>
    <td><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/480px-LinkedIn_logo_initials.png" width="20" /></td>
    <td>LinkedIn</td>
    <td><code>Ranit Manik</code></td>
    <td><a href="https://www.linkedin.com/in/ranit-manik/" target="_blank">LinkedIn</a></td>
  </tr>
  <tr>
    <td><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/600px-Instagram_icon.png" width="20" /></td>
    <td>Instagram</td>
    <td><code>ranit_manik_</code></td>
    <td><a href="https://www.instagram.com/ranit_manik_/" target="_blank">Instagram</a></td>
  </tr>
  <tr>
    <td><img src="https://upload.wikimedia.org/wikipedia/commons/6/6c/Facebook_Logo_2023.png" width="20" /></td>
    <td>Facebook</td>
    <td><code>RanitKumarManik</code></td>
    <td><a href="https://www.facebook.com/RanitKumarManik/" target="_blank">Facebook</a></td>
  </tr>
  <tr>
    <td><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Logo_of_Twitter.svg/512px-Logo_of_Twitter.svg.png" width="20" /></td>
    <td>Twitter</td>
    <td><code>RANIT_MANIK</code></td>
    <td><a href="https://twitter.com/RANIT_MANIK" target="_blank">Twitter</a></td>
  </tr>
</table>

## Acknowledgment

I want to express my gratitude to [CodeWithHarry](https://www.youtube.com/c/CodeWithHarry) for his insightful tutorial on creating the [myGPT Discord Chatbot using OpenAI's GPT-3.5 Turbo model](https://youtu.be/BP-w99ZINTc?si=tcUeGGh3MKCYODuk), which served as a crucial guide. Special thanks to contributors and the open-source community for enhancing the project. The inspiration behind TelegramGPT arose from the need for an advanced Telegram chatbot leveraging OpenAI's GPT-3.5 Turbo.

Best regards, Ranit Manik
