# Text-Generator

## Overview
<p> This script was done as part of JetBrains Academy's Python Core track, as an implementation of one of
it's educational projects (Text Generator). </p>


## Project Description
</p> The task was to implement a script that generates ten random sentences from a given text file(corpus),
and each sentence should be:
1. No less than five words
2. Starts with a capital <b>letter</b>
3. Ends with a sentence-ending punctuation(?, ., !)
4. On a separate line. </p>


## Solution Approach
<p> Using a WhitespaceTokenizer the text is split into a list of words, which will be fed to the model that creates <I>trigrams</I>; from every three consecutive words in the corpus; the model maps the first two words(head) as one token with the third word (tail) as the second token, the model will also store how often every trigram has appeared. Then the first word of each sentence is chosen randomly from the list of heads, according to the rules mentioned in the project description. Then the following words will be selected also randomly but based on the previous word in the sentence considering the frequency of the trigram  as the weight of this trigram in the corpus. A sentence that has ended with sentence-ending punctuation and is less than 5 words in length will be discarded to avoid an infinite loop as a valid sentence won't be found. </p>


## How to run
<p>Type: <code> python text_generator.py </code> in the terminal then type the text file name.</p>
