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

# 3. Install python libraries / setup conda environment
```bash
conda env create -f environment.yml
```
If library versions are wrong, then you would need to google the right versions, you can find one of the working configurations in the second message in pip_freeze.txt file here - https://github.com/mgrankin/ru_transformers/issues/9
If you need to reinstall libraries, then you need to remove gpt environment from anaconda2, smth like this:
```bash
rm -rf {PATH_TO_ANACONDA2_LIBRARIES}/anaconda2/envs/gpt/
conda env create -f environment.yml
```

Also add line "conda activate" (without quotemarks) to your ~/.bashrc.

# 4. Prepare data for training

Use script convert_json_into_plaintext.py, stdout is used for training, stderr for validation.

# 5. Finetune GPT-2 to your data.

Take a look at dialogue_train.sh script. Run like this:
```bash
cd foghorny (or folder name of this project, where the train script is located)
source ~/.bashrc
conda activate gpt
./dialogue_train.sh > out.txt 2> err.txt &
```
You can also monitor samples from time to time in out.txt file.
Wait about from 30 minutes to 1 hour for training to finish.

# 5. Deploy tg bot

This is a TODO part at the moment, but we have a preliminary script for posting tg messages, like an auto-replier, stay tuned!
