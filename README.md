**Running the File**

Download and unzip the .ZIP file of this repository. Add the text file to the unzipped folder that you want to use to generate similar text from. 
Then, open terminal and type in the following commands:

*ipython*
*cd Downloads*
*cd Markov-Text-Generation-master*
*run textgenerator.py*

**The Idea**

English is a language with a lot of structure, and words have a tendency to appear only in certain sequences.
Even without knowing the formal rules of English, or the meaning of English words, we can get an idea of what word combinations are legal simply by looking at well-formed English text and noting the combinations of words that tend to occur in practice. Then, based on our observations, we could generate new sentences by randomly selecting words according to commonly occurring sequences of these words.
This algorithm uses a kth-order Markov process to generate text that follows general word sequences of the original text.
