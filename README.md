# Get Started

## discord botの作成

discord botを作成し、アクセストークンを発行してください。

アクセストークンを環境変数(DISCORD_TOKEN)に設定しておいてください。

    export DISCORD_TOKEN=<YOUR_DISCORD_BOT_TOKEN>

また、discordグループへのbotの招待を完了しておきます。

## Botの実行

    docker build -t deckcode-bot .
    docker run -e DISCORD_TOKEN deckcode-bot

## Botの利用方法

チャットでデッキコードを含む以下のような発言をすると、それを検知してデッキ画像を貼り付けます。

    /ideck CICACAYGBAAQGBIQAMAQKEZRGUCQEBQEDIOSMOQEAEAQKHIBAIDASAIEAYFACBIFBYAQEAIFAEQA