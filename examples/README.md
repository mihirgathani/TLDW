## Running the website locally

### **1. Clone the Git Repo**
Clone the repository on your local machine using the following command on terminal
```
git clone https://github.com/JoobeeJung/TLDW.git
```

### **2. Install required packages and libraries**
Refer libraries.md for more information on required library/package installments

### **3. Get the Gemini API key**
Before running the application it is important to generate a Gemini [API Key](https://aistudio.google.com/app/apikey). The API key needs to be placed under TLDW/ in a .env file, assigned to the variable **GEMINI_API_KEY**.

![Structure of the .env file where the API credentials needs to be stored](https://github.com/JoobeeJung/TLDW/blob/main/examples/images/env.png)

### **4. Running the application**
Use the following command on your terminal to open up our website on your browser. Make sure you are in the TLDW/TLDW directory
```
streamlit run streamlit run streamlit_app.py 
```

## Deployment

The program was deployed using [Streamlit Sharing](https://share.streamlit.io/). For more informtion, one can visit the [Public Website](nothing.streamlit.app).

## Web Application

- Click here for a walk through demonstration of our website.
