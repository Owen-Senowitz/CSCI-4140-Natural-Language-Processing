# Part 2 Answers

## A

The pretrained model learned patterns in text during pretraining (like associations between names and places), so it started finetuning with useful knowledge. The non pretrained model started from scratch with random weights and didn’t have enough data during finetuning to learn good associations.

## B

Reason 1:
Users might trust a wrong answer because the output looks confident and real.
Example: A voice assistant says “John was born in Paris,” but the model made it up — the user believes it’s true.

Reason 2:
Systems using this model might spread false or biased information without realizing it.
Example: An automated biography generator lists fake birthplaces for historical figures, which gets copied by news or educational tools.

## C

The model might guess based on similar looking names or common training set patterns.
For example, if it sees “Miguel,” it might default to a Spanish speaking country like “Mexico.”

Ethical concern:
This could lead to cultural stereotyping or biased assumptions reinforcing false links between names and places, which can offend or misrepresent people.
