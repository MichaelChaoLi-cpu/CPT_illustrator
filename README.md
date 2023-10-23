# CPT_illustrator
This is the repo to build CPT illustrator for deploying CPT

Turn on cpt_illustrator vm:

## Using CPT-illustrator
To the public user:
```
su - cpt_illustrator
```
Password:
```
cpt
```

Activate the env
```
conda activate tf
```

Data Transfer by gcloud cli
```
gcloud compute scp Downloads/annual-report-2022.pdf cpt_illustrator@aiesg-cpt-v1-illustrator:/home/cpt_illustrator/RunPDF/GoldmanSachs2022.pdf --zone=asia-southeast1-b
```
"Downloads/annual-report-2022.pdf" this is the file address on your computer.
"GoldmanSachs2022.pdf" this is filename on the VM.


begin the analysis
```
ls RunPDF
INPUT_FILE=$(ls RunPDF)
FILENAME=$(basename "$INPUT_FILE" .pdf)
echo "$FILENAME"
ADDRESS="ResultToDownload/$FILENAME"
echo $ADDRESS
python run.py
```
result location
```
echo $ADDRESS
```
copy this output

download results
```
gcloud compute scp --recurse cpt_illustrator@aiesg-cpt-v1-illustrator:/home/cpt_illustrator/'echo $ADDRESS' Downloads/Results --zone=asia-southeast1-b
```
'echo $ADDRESS' copy the ouptut of this line code to this place.
"Downloads/Results", this this result location.


**shut down that vm**

**CAUTION this VM is expensive!!!**
