{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "import string\n",
    "\n",
    "class TextCleaner():\n",
    "\n",
    "    \"\"\"\n",
    "    this class cleans up a text.\n",
    "    \"\"\"\n",
    "\n",
    "    def __init__(self):\n",
    "        self.noisePattern = re.compile(\"|\".join([\"http\\S+\", \"\\@\", \"\\#\", '\"']))\n",
    "        self.remove_ellipsis_re = re.compile(r'\\.\\.\\.')\n",
    "        self.punctuationPattern = re.compile('[%s]' % re.escape(string.punctuation))\n",
    "        self.pricePattern = re.compile(r\"\\d+\\.\\d\\d\")\n",
    "        self.numberPattern = re.compile(r\"\\d+\")\n",
    "\n",
    "    def cleanTweetText(self, text):\n",
    "        \"\"\"\n",
    "        this function will take a text and try to cleanup it.\n",
    "        Parameters\n",
    "        ----------\n",
    "        text: str\n",
    "              the text will be cleaned\n",
    "        Returns\n",
    "        -------\n",
    "        text_cleaned: str\n",
    "                         cleaned up version of the raw text\n",
    "        \"\"\"\n",
    "\n",
    "        text_cleaned = text.lower()\n",
    "        text_cleaned = re.sub(self.noisePattern, '', text_cleaned)\n",
    "        text_cleaned = re.sub(self.pricePattern, 'PRICE', text_cleaned)\n",
    "        text_cleaned = re.sub(self.remove_ellipsis_re, '', text_cleaned)\n",
    "        text_cleaned = re.sub(self.punctuationPattern, '', text_cleaned)\n",
    "        text_cleaned = re.sub(self.numberPattern, 'NUM', text_cleaned)\n",
    "\n",
    "        return text_cleaned"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
