# Examples
This folder contains the files for various demonstrations including:
- [Running the website ](https://github.com/JoobeeJung/TLDW/edit/main/examples/README.md#L13)
    - [Clone the Git Repo](https://github.com/JoobeeJung/TLDW/edit/main/examples/README.md#L15)
    - [Install required packages and libraries](https://github.com/JoobeeJung/TLDW/edit/main/examples/README.md#L21)
    - [Get and input the Gemini API key](https://github.com/JoobeeJung/TLDW/edit/main/examples/README.md#L24)
    - [Run the application](https://github.com/JoobeeJung/TLDW/edit/main/examples/README.md#L29)
- [Website Deployment](https://github.com/JoobeeJung/TLDW/edit/main/examples/README.md#L35)
- [Website Application Demo](https://github.com/JoobeeJung/TLDW/edit/main/examples/README.md#L39) 



## Running the website locally

### **1. Clone the Git Repo**
Clone the repository on your local machine using the following command on terminal
```
git clone https://github.com/JoobeeJung/TLDW.git
```

### **2. Environment**
Our application is built on various Python packages with specific version requirements. Installing these packages individually can cause conflicts and require dependencies in your workspace. To fix this issue, it is recommended to use a virtual environment in `conda` with all the necessary packages of our application. A list of necessary packages and libraries can be found in our [environment.yml](https://github.com/JoobeeJung/TLDW/blob/main/environment.yml) file and our [requirements.txt](https://github.com/JoobeeJung/TLDW/blob/main/requirements.txt) file.

To create a new `TLDW` Conda environment, run the following command:

```
conda env create -f environment.yml
```

Once the Conda environment is created, it can be activated by:

```
conda activate TLDW
```

The environment can be deactivated with the command:

```
conda deactivate
```

### **3. Application**
We developed this application using the open-source `streamlit` package. A local application can be generated with the code:

```
conda activate TLDW
cd TLDW/TLDW
```

### **4. Get and input the Gemini API key**
Before running the application it is important to generate a Gemini [API Key](https://aistudio.google.com/app/apikey). The API key needs to be placed under TLDW/ in a .env file, assigned to the variable **GEMINI_API_KEY**. If you are an authorized user (Professors/TAs/in our group) please refer to this [Google Drive](https://drive.google.com/file/d/1BO4r8aet1pkxneqkwDYSnGjORephlPWr/view) to download a .env file to use in your cloned repository. 

![Structure of the .env file where the API credentials needs to be stored](https://github.com/JoobeeJung/TLDW/blob/main/examples/images/env.png)

### **5. Run the application**
Use the following command on your terminal to open up our website on your browser. Make sure you are in the TLDW/TLDW directory
```
streamlit run streamlit_app.py 
```

## Deployment

The program was deployed using [Streamlit Sharing](https://share.streamlit.io/). For more informtion, one can visit the [Public Website](nothing.streamlit.app).

## Web Application Demo

- Click here for a walk through [demonstration](https://github.com/JoobeeJung/TLDW/blob/main/examples/images/Recording_final.mov) video of our website.
- Click here for a text demonstration [demonstration](https://github.com/JoobeeJung/TLDW/blob/main/examples/website_navigation.md) of our video.
