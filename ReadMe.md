This is a word classification project.
The project is done using 1020 audio files here: https://drive.google.com/drive/folders/1uNPiOeo2vaZ29iGPybJEeWtgt4QOTE6o?usp=sharing

steps of the project:
1. The audio files are related to 255 people and 4 paragraphs that each indivisual reads all paragraphs, so the total number of audio files is 1020. The first step was to create the audio files for classification. So in order to create the files we had to clip the audios and cut the parts which the speaker was spelling those words. For this purpose we could use 'Praat' or 'Wavepad' softwares which comparing their user interfaces, I have preferred to use 'wavepad'.

2. Data Augmentation: the clipped words have different lengths and also most of them only contain the word without any silence parts. so in order to make the dataset larger, I have wrote a code named 'Creating one sec length files.py' which adds silence parts to the beginning and end of the files. In fact for each of the words, it creats 3 different '.wav' fils which the first one is silence+word, second one is silence+word+silence and the third one is word+silence in a way that all this 3 formets have a 1 second length.

3. 'Training Code.py' is a code that uses the audio files to train a 
