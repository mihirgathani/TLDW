# Examples
This folder contains the files for various demonstrations including:
- [Running the website ](https://github.com/JoobeeJung/TLDW/edit/main/examples/README.md#L13)
    - [Clone the Git Repo](https://github.com/JoobeeJung/TLDW/edit/main/examples/README.md#L15)
    - [Install required packages and libraries](https://github.com/JoobeeJung/TLDW/edit/main/examples/README.md#L21)
    - [Get and input the Gemini API key](https://github.com/JoobeeJung/TLDW/edit/main/examples/README.md#L24)
    - [Run the application](https://github.com/JoobeeJung/TLDW/edit/main/examples/README.md#L29)
- [Website Deployment](https://github.com/JoobeeJung/TLDW/edit/main/examples/README.md#L35)
- [Website Application] (https://github.com/JoobeeJung/TLDW/edit/main/examples/README.md#L39) 



## Running the website locally

### **1. Clone the Git Repo**
Clone the repository on your local machine using the following command on terminal
```
git clone https://github.com/JoobeeJung/TLDW.git
```

### **2. Install required packages and libraries**
Refer [requirements.txt](https://github.com/JoobeeJung/TLDW/blob/main/requirements.txt) for more information on required library/package installments

### **3. Get and input the Gemini API key**
Before running the application it is important to generate a Gemini [API Key](https://aistudio.google.com/app/apikey). The API key needs to be placed under TLDW/ in a .env file, assigned to the variable **GEMINI_API_KEY**.

![Structure of the .env file where the API credentials needs to be stored](https://github.com/JoobeeJung/TLDW/blob/main/examples/images/env.png)

### **4. Run the application**
Use the following command on your terminal to open up our website on your browser. Make sure you are in the TLDW/TLDW directory
```
streamlit run streamlit run streamlit_app.py 
```

## Deployment

The program was deployed using [Streamlit Sharing](https://share.streamlit.io/). For more informtion, one can visit the [Public Website](nothing.streamlit.app).

## Web Application

- Click here for a walk through [demonstration](https://github.com/JoobeeJung/TLDW/blob/main/examples/images/Recording_final.mp4) video of our website.
- Click here for a text demonstration [demonstration](https://github.com/JoobeeJung/TLDW/blob/main/examples/website_navigation.md) of our vide0.
