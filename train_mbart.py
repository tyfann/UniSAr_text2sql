import subprocess
import argparse
import os


def run_command(bash_command):
    process = subprocess.Popen(bash_command.split())
    output, error = process.communicate()
    print(error)
    print(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_path", type=str, default="", help="dataset path")
    parser.add_argument("--exp_name", type=str, default="", help="test")
    parser.add_argument("--models_path", type=str, default="", help="models path")
    parser.add_argument("--bart_model_path", type=str, default="", help="bart init models path")
    parser.add_argument("--total_num_update", type=int, default=200000)
    parser.add_argument("--max_tokens", type=int, default=4096)
    parser.add_argument("--tensorboard_path", type=str, default="", help="tensorboard path")
    args = parser.parse_args()

    print("START training")
    run_command("printenv")

    restore_file = os.path.join(args.bart_model_path, "model.pt")
#     restore_file = args.bart_model_path
    # if not os.path.exists(args.tensorboard_path):
    #     os.mkdir(args.tensorboard_path)
    # print("writing logs to {}".format(args.tensorboard_path))
    # --tensorboard-logdir {args.tensorboard_path} \
    cmd = f"""
    fairseq-train {args.dataset_path} \
    --save-dir {args.models_path}/{args.exp_name} \
    --restore-file {restore_file} \
    --arch mbart_large  \
    --task translation_from_pretrained_bart  \
    --encoder-normalize-before \
    --decoder-normalize-before \
    --layernorm-embedding \
    --criterion label_smoothed_cross_entropy  \
    --source-lang src  \
    --target-lang tgt  \
    --truncate-source  \
    --label-smoothing 0.1  \
    --max-tokens {args.max_tokens}  \
    --update-freq 4  \
    --max-update {args.total_num_update}  \
    --required-batch-size-multiple 1  \
    --dropout 0.1  \
    --attention-dropout 0.1  \
    --relu-dropout 0.0  \
    --weight-decay 0.05  \
    --optimizer adam  \
    --adam-eps 1e-08  \
    --clip-norm 0.1  \
    --lr-scheduler polynomial_decay  \
    --lr 2.5e-05  \
    --total-num-update {args.total_num_update}  \
    --warmup-updates 5000  \
    --ddp-backend no_c10d  \
    --num-workers 20  \
    --reset-meters  \
    --reset-optimizer \
    --reset-dataloader \
    --share-all-embeddings \
    --share-decoder-input-output-embed  \
    --skip-invalid-size-inputs-valid-test  \
    --log-format json  \
    --log-interval 10  \
    --save-interval-updates	500 \
    --validate-interval-updates 500 \
    --validate-interval	10 \
    --save-interval	10 \
    --patience 200 \
    --no-last-checkpoints \
    --no-save-optimizer-state \
    --report-accuracy \
    --langs ar_AR,cs_CZ,de_DE,en_XX,es_XX,et_EE,fi_FI,fr_XX,gu_IN,hi_IN,it_IT,ja_XX,kk_KZ,ko_KR,lt_LT,lv_LV,my_MM,ne_NP,nl_XX,ro_RO,ru_RU,si_LK,tr_TR,vi_VN,zh_CN
    """

    print("RUN {}".format(cmd))
    run_command(cmd)