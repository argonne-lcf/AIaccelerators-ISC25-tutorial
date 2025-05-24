# GPT on Sambanova

##### Create and and move to the following directory.

```bash
mkdir ~/apps/nlp/Gpt1.5B_single
cd ~/apps/nlp/Gpt1.5B_single
```

##### Copy script to Compile and Run


<!-- cp /data/ANL/scripts/Gpt1.5B_base_single_compile.sh .
cp /data/ANL/scripts/Gpt1.5B_base_single_run.sh . -->

```bash
cp /data/ANL/scripts/1.23.5-46/legacy_models/Gpt1.5B_base_single_compile.sh ~/apps/nlp/Gpt1.5B_single/
cp /data/ANL/scripts/1.23.5-46/legacy_models/Gpt1.5B_base_single_run.sh ~/apps/nlp/Gpt1.5B_single/

chmod +x Gpt1.5B_base_single_compile.sh
chmod +x Gpt1.5B_base_single_run.sh
```

##### Run the script to Compile and Run

```bash
./Gpt1.5B_base_single_compile.sh 32
```
