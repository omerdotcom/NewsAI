{
 "cells": [
  {
   "id": "a4a6516a-2074-4742-aa39-9e869a95485b",
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import re \n",
    "import nltk\n",
    "from nltk.corpus import stopwords"
   ]
  },
  {
   "id": "2acffb5f-7477-43c4-9ec1-0f348c8db595",
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package stopwords to /home/omer/nltk_data...\n",
      "[nltk_data]   Package stopwords is already up-to-date!\n"
     ]
    }
   ],
   "source": [
    "nltk.download('stopwords')\n",
    "stop = set(stopwords.words('english'))"
   ]
  },
  {
   "id": "3a86b2b9-fd14-4f11-8dc5-749383ff9802",
   "outputs": [],
   "source": [
    "model = pickle.load(open('model.pkl','rb'))\n",
    "vectorizer = pickle.load(open('vectorizer.pkl','rb'))"
   ]
  },
  {
   "id": "c78ce1b2-c8e8-499e-8d0d-c31bf1a095f4",
   "outputs": [],
   "source": [
    "def clean_text(text):\n",
    "    text = re.sub(r'[^a-zA-Z\\s]','',text)\n",
    "    text = text.lower()\n",
    "    return \" \".join([w for w in text.split() if w not in stop])"
   ]
  },
  {
   "id": "c00ade32-582a-4759-a715-4389398c7592",
   "outputs": [],
   "source": [
    "def predict_news(text):\n",
    "    clean = clean_text(text)\n",
    "    vec = vectorizer.transform([clean])\n",
    "    pred = model.predict(vec)[0]\n",
    "    proba = model.predict_proba(vec)[0]\n",
    "    label = 'REAL' if pred == 1 else 'FAKE'\n",
    "    confidence = round(max(proba)*100,2)\n",
    "    return f'{label}, confidence = {confidence}%'"
   ]
  },
  {
   "id": "aa3cf264-063d-4b33-8f84-15bd2ec13a42",
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-09-19 01:29:26.583 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-19 01:29:26.646 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /home/omer/.local/lib/python3.10/site-packages/ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-09-19 01:29:26.647 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-19 01:29:26.648 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-19 01:29:26.650 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-19 01:29:26.653 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-19 01:29:26.655 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-19 01:29:26.659 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-19 01:29:26.661 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-19 01:29:26.662 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-19 01:29:26.663 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-19 01:29:26.664 Session state does not function when running a script without `streamlit run`\n",
      "2025-09-19 01:29:26.666 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-19 01:29:26.667 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-19 01:29:26.670 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "st.title('Fake News Detector')\n",
    "st.write('Enter a news paraghraph or article, and the model will tell you if its REAL or FAKE')\n",
    "user_input = st.text_area('Paste your news text  here:')\n",
    "if st.button('Check'):\n",
    "    if user_input.strip() == '':\n",
    "        st.warning('Please enter some text.')\n",
    "    else:\n",
    "        result = predict_news(user_input)\n",
    "        st.success(result)"
   ]
  },
  {
   "id": "bb14bae9-d286-4c1b-be05-3024d70fd2cc",
   "outputs": [],
   "source": []
  }
 ],
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
   "version": "3.10.12"
  }
 }
