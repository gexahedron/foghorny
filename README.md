# GPT-2 for telegram dialogues

# 0. Attributions

gpt2 model and code for training (run_generation.py, run_lm_finetuning.py, bpe/\*) is taken from https://github.com/mgrankin/ru_transformers

# 1. Download model

```bash
pip install awscli
aws s3 sync --no-sign-request s3://models.dobro.ai/gpt2/ru/unfreeze_all gpt2
```

Folders with ```s_``` prefix contain Small (124M) model, ```m_``` - for Medium (355M) model. 

# 2. Download your Telegram dialogue

2.1. Download Telegram Desktop.
2.2. Go to Menu -> Settings -> Advanced -> Export Telegram data, choose "Personal chats" and "Machine-readable JSON".
2.3. Click Export and wait.

# 3. Prepare data for training

Use script convert_json_into_plaintext.py, stdout is used for training, stderr for validation.

# 4. Finetune GPT-2 to your data.

Take a look at train.sh script.

# 5. Deploy tg bot

This is a TODO part at the moment, but we have a preliminary script for posting tg messages, like an auto-replier, stay tuned!
