# Magnitude Estimation - PSYCH 363 - S2023

This is the github repository for the final project for PSYCH 363 in Summer 2023.

To generate PDF report from .org file:

- Open .org file in emacs
- Generate .tex file using the emacs commands: C-c, C-e, l, l
- Run the following commands to generate .pdf file with Bibliography

```
pdflatex magnitudeEstimationWriteUp.tex
bibtex magnitudeEstimationWriteUp
pdflatex magnitudeEstimationWriteUp.tex
```

Experiment was programmed in psychopy and can be found in file finalProject.py

