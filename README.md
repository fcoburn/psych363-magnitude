# Magnitude Estimation - PSYCH 363 - S2023

This is the github repository for the final project for PSYCH 363 in Summer 2023.

## Key Assets in this Repository

The following files are the main artefacts in this repository:

- Group7-MagnitudeEstimation-WriteUp.org
- Group7-MagnitudeEstimation-References.bib
- Group7-MagnitudeEstimation-Experiment.py

The experiment itself was programmed in psychopy can be be run by executingthe following command in a terminal window:

```
python3 Group7-MagnitudeEstimation-Experiment.py
```

When run the program will produce a .csv file within the same directory. Files from repeated experiment runs can be combined with the shell script "combine-files.sh"

## Generate PDF

To generate a PDF report from the .org file Group7-MagnitudeEstimation-WriteUp.org:


- Open .file "Group7-MagnitudeEstimation-WriteUp.org" in emacs with org mode installed
- Generate .tex file using the emacs commands: C-c, C-e, l, l
- Run the following terminal commands to generate .pdf file with Bibliography section

```
pdflatex magnitudeEstimationWriteUp.tex
bibtex magnitudeEstimationWriteUp
pdflatex magnitudeEstimationWriteUp.tex
```
