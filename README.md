# Experiment: Reactions to Different Payment Structures in Obese and Vegan Diet Groups
Finding demographic characteristics and linking them to payment preference.

*This is my coursework for the Seminar "Programming for Experimental Economics" in Heidelberg University 2023 Summer Semester, supervised by Mr. Tamas Olah.*

## Introduction
This project connects the subject’s demographic information on eating habits, such as BMI and vegan eating style, with the choice of delayed or probable payment. Using experimental methods, subjects’ personal information and their preference for future payment will be collected and their future payment preferences will be calculated with exponential methods.

This project only contains the methodology and the design codes for this experiment. The experiment uses `oTree` to execute and operate, you may want to read more about the [official website](https://www.otree.org/) or [GitHub page](https://github.com/oTree-org/oTree/) of `oTree` and `python`.


## Methodology

### Sample
- **Target:** Approximately 1000 participants from diverse backgrounds.
- **Requirements:** Participants must be over 18 years old and know their precise heights and weights for BMI calculations.

### Procedure
- Participants complete a questionnaire on a computer in a controlled environment.
- Data collected includes age, gender, academic background, diet, and BMI.
- The experiment involves 21 questions with a time limit and a confirmation page for each response.
- Incentives include a fixed compensation for participation and additional rewards based on eligibility for analysis.

### Question Structure
- Each question presents a scenario with an initial wealth amount and three payment options: immediate, delayed, or probabilistic.
- Participants choose the option they find most appealing without planning.

## Data Analysis
- We use an exponential formula to calculate mental discounting rates based on participants' choices.
- The experiment calculates average discounting rates and provides demographic information and individual responses.

## References
Bickel, W.K., Wilson, A.G., Franck, C.T., Mueller, E.T., Jarmolowicz, D.P., Koffarnus, M.N. and Fede, S.J., 2014. Using crowdsourcing to compare temporal, social temporal, and probability discounting among obese and non-obese individuals. *Appetite, 75*, pp.82-89.

## Theoretical Background and Intuition
Please see the file in the main branch `Report.pdf` for further information. This file introduces the procedures and theoretical backgrounds of the experiment.
