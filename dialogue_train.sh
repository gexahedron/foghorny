export TRAIN_FILE=dialogue_data/train.txt
export TEST_FILE=dialogue_data/test.txt

export CUDA_VISIBLE_DEVICES=1
export OUTPUT=dialogue_models/s
export BS=1
export LR=3e-5

# training script

python run_lm_finetuning.py \
    --output_dir=$OUTPUT \
    --model_type=gpt2 \
    --model_name_or_path=$OUTPUT \
    --do_train \
    --train_data_file=$TRAIN_FILE \
    --per_gpu_train_batch_size $BS \
    --save_steps=10000 \
    --logging_steps=1 \
    --warmup_samples 16000 \
    --learning_rate $LR \
    --overwrite_output_dir \
    --tokenizer_class YTEncoder \
    --tokenizer_name bpe/yt.model \
    --do_eval \
    --evaluate_during_training \
    --eval_steps 1000 \
    --eval_data_file=$TEST_FILE \
    --per_gpu_eval_batch_size $BS \
    --save_total_limit 30 \
    --num_train_epochs 15 \
    --unfreeze_level -1

